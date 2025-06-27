from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import psycopg2
import math

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

def carregar_pecas_do_banco():
    url = os.environ.get('DATABASE_URL', 'postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway')
    conn = psycopg2.connect(url)
    categorias = [
        ('Processador', 'processadores'),
        ('Placa-mãe', 'placas_mae'),
        ('Memória RAM', 'memoria_ram'),
        ('Armazenamento', 'armazenamento'),
        ('Placa de vídeo', 'placa_de_video'),
        ('Fonte', 'fonte'),
        ('Gabinete', 'gabinete'),
    ]
    pecas = {}
    for nome_cat, tabela in categorias:
        try:
            with conn.cursor() as cursor:
                cursor.execute(f'SELECT * FROM {tabela}')
                colnames = [desc[0] for desc in cursor.description]
                pecas[nome_cat] = []
                for row in cursor.fetchall():
                    item = dict(zip(colnames, row))
                    item['nome'] = item.get('nome') or item.get('modelo') or item.get('descricao') or 'Sem nome'
                    item['preco'] = item.get('preco', 0)
                    if 'especificacoes' not in item or not item['especificacoes']:
                        especs = []
                        for k, v in item.items():
                            if k not in ['nome', 'preco', 'id']:
                                especs.append(f'{k.capitalize()}: {v}')
                        item['especificacoes'] = '\n'.join(especs)
                    pecas[nome_cat].append(item)
        except Exception as e:
            pecas[nome_cat] = []
    conn.close()
    return pecas

@app.route('/', methods=['GET', 'POST'])
@app.route('/montar_pc', methods=['GET', 'POST'])
def montar_pc():
    pecas = carregar_pecas_do_banco()
    etapas = list(pecas.keys())
    etapa_atual = session.get('etapa_atual', 0)
    selecoes = session.get('selecoes', {})
    # Permite navegação direta por query string
    etapa_param = request.args.get('etapa')
    if etapa_param is not None and etapa_param.isdigit():
        etapa_atual = int(etapa_param)
        session['etapa_atual'] = etapa_atual
    categoria = etapas[etapa_atual]

    # Busca e paginação
    busca = request.args.get('busca', '').strip().lower()
    pagina_atual = int(request.form.get('pagina', 1) if request.method == 'POST' else request.args.get('pagina', 1) or 1)
    try:
        pagina_atual = int(pagina_atual)
    except Exception:
        pagina_atual = 1
    itens_por_pagina = 8

    lista_itens = []
    for idx, item in enumerate(pecas.get(categoria, [])):
        item_copia = item.copy()
        item_copia['idx'] = idx
        if 'especificacoes' not in item_copia:
            especs = []
            for k, v in item_copia.items():
                if k not in ['nome', 'preco', 'idx']:
                    especs.append(f'{k.capitalize()}: {v}')
            item_copia['especificacoes'] = '\n'.join(especs)
        lista_itens.append(item_copia)

    if busca:
        lista_itens = [
            item for item in lista_itens
            if busca in item['nome'].lower() or busca in item.get('especificacoes', '').lower()
        ]

    total_itens = len(lista_itens)
    total_paginas = max(1, math.ceil(total_itens / itens_por_pagina))
    pagina_atual = max(1, min(pagina_atual, total_paginas))
    start = (pagina_atual - 1) * itens_por_pagina
    end = start + itens_por_pagina
    itens_paginados = lista_itens[start:end]

    if request.method == 'POST':
        if 'voltar' in request.form:
            if etapa_atual > 0:
                session['etapa_atual'] = etapa_atual - 1
            return redirect(url_for('montar_pc'))
        if 'remover' in request.form:
            if categoria in selecoes:
                selecoes.pop(categoria)
                session['selecoes'] = selecoes
            return redirect(url_for('montar_pc'))
        if 'pagina' in request.form:
            return redirect(url_for('montar_pc', etapa=etapa_atual, busca=busca, pagina=request.form['pagina']))
        idx = int(request.form.get('opcao', 0))
        selecoes[categoria] = idx
        session['selecoes'] = selecoes
        if etapa_atual < len(etapas) - 1:
            session['etapa_atual'] = etapa_atual + 1
            return redirect(url_for('montar_pc'))
        else:
            return redirect(url_for('finalizar'))

    selecao = selecoes.get(categoria, None)
    total = sum(pecas[cat][idx]['preco'] for cat, idx in selecoes.items() if cat in pecas and idx < len(pecas[cat]))
    # Monta mensagem para WhatsApp
    msg = 'Olá! Gostaria de uma consultoria para o seguinte PC:%0A'
    for cat, idx in selecoes.items():
        if cat in pecas and idx < len(pecas[cat]):
            msg += f"{cat}: {pecas[cat][idx]['nome']} (R$ {pecas[cat][idx]['preco']})%0A"
    msg += f"Total: R$ {total}"
    whatsapp_url = f"https://wa.me/+5528999928442?text={msg}"

    return render_template(
        'montar_pc.html',
        etapas=etapas,
        etapa_atual=etapa_atual,
        categoria=categoria,
        pecas=pecas,
        selecao=selecao,
        selecoes=selecoes,
        total=total,
        whatsapp_url=whatsapp_url,
        busca=busca,
        itens_paginados=itens_paginados,
        pagina_atual=pagina_atual,
        total_paginas=total_paginas
    )

@app.route('/finalizar', methods=['GET', 'POST'])
def finalizar():
    pecas = carregar_pecas_do_banco()
    etapas = list(pecas.keys())
    selecoes = session.get('selecoes', {})
    if len(selecoes) < len(etapas):
        flash('Por favor, selecione todas as peças antes de finalizar.', 'danger')
        return redirect(url_for('montar_pc'))
    try:
        proc = pecas['Processador'][selecoes['Processador']]
        mb = pecas['Placa-mãe'][selecoes['Placa-mãe']]
        ram = pecas['Memória RAM'][selecoes['Memória RAM']]
    except (KeyError, IndexError):
        flash('Seleção inválida detectada. Por favor, reinicie a montagem.', 'danger')
        session.clear()
        return redirect(url_for('montar_pc'))
    erros = []
    if proc.get('soquete') != mb.get('soquete'):
        erros.append('Processador e Placa-mãe incompatíveis (soquete diferente).')
    if mb.get('ram') != ram.get('tipo'):
        erros.append('Placa-mãe e Memória RAM incompatíveis (tipo diferente).')
    if erros:
        for erro in erros:
            flash(erro, 'danger')
        session['etapa_atual'] = 0
        return redirect(url_for('montar_pc'))
    total = sum(pecas[cat][idx]['preco'] for cat, idx in selecoes.items() if cat in pecas and idx < len(pecas[cat]))
    selecao = selecoes.get(etapas[-1], 0)
    return render_template('montar_pc.html', etapas=etapas, etapa_atual=len(etapas)-1, categoria=etapas[-1], pecas=pecas, selecao=selecao, selecoes=selecoes, total=total, resumo=True)
