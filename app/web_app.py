from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

pecas = {
    'Processador': [
        {'nome': 'Intel i5', 'preco': 1200, 'soquete': 'LGA1200'},
        {'nome': 'Intel i7', 'preco': 1800, 'soquete': 'LGA1200'},
        {'nome': 'AMD Ryzen 5', 'preco': 1100, 'soquete': 'AM4'},
    ],
    'Placa-mãe': [
        {'nome': 'ASUS Prime', 'preco': 800, 'soquete': 'LGA1200', 'ram': 'DDR4'},
        {'nome': 'Gigabyte Ultra', 'preco': 950, 'soquete': 'AM4', 'ram': 'DDR4'},
    ],
    'Memória RAM': [
        {'nome': '8GB DDR4', 'preco': 200, 'tipo': 'DDR4'},
        {'nome': '16GB DDR4', 'preco': 350, 'tipo': 'DDR4'},
    ],
    'Armazenamento': [
        {'nome': 'SSD 240GB', 'preco': 180},
        {'nome': 'HD 1TB', 'preco': 250},
    ],
    'Placa de vídeo': [
        {'nome': 'NVIDIA GTX 1660', 'preco': 1500},
        {'nome': 'AMD RX 580', 'preco': 1200},
    ],
    'Fonte': [
        {'nome': 'Corsair 500W', 'preco': 350},
        {'nome': 'EVGA 600W', 'preco': 400},
    ],
    'Gabinete': [
        {'nome': 'Cooler Master', 'preco': 300},
        {'nome': 'PCYes Fênix', 'preco': 250},
    ],
}
etapas = list(pecas.keys())

@app.route('/', methods=['GET', 'POST'])
def montar_pc():
    etapa_atual = session.get('etapa_atual', 0)
    selecoes = session.get('selecoes', {})
    categoria = etapas[etapa_atual]
    if request.method == 'POST':
        idx = int(request.form.get('opcao', 0))
        selecoes[categoria] = idx
        session['selecoes'] = selecoes
        if etapa_atual < len(etapas) - 1:
            session['etapa_atual'] = etapa_atual + 1
            return redirect(url_for('montar_pc'))
        else:
            return redirect(url_for('finalizar'))
    selecao = selecoes.get(categoria, 0)
    total = sum(pecas[cat][idx]['preco'] for cat, idx in selecoes.items())
    return render_template('montar_pc.html', etapas=etapas, etapa_atual=etapa_atual, categoria=categoria, pecas=pecas, selecao=selecao, selecoes=selecoes, total=total)

@app.route('/finalizar', methods=['GET', 'POST'])
def finalizar():
    selecoes = session.get('selecoes', {})
    if len(selecoes) < len(etapas):
        return redirect(url_for('montar_pc'))
    # Checagem de compatibilidade
    proc = pecas['Processador'][selecoes['Processador']]
    mb = pecas['Placa-mãe'][selecoes['Placa-mãe']]
    ram = pecas['Memória RAM'][selecoes['Memória RAM']]
    erros = []
    if proc['soquete'] != mb['soquete']:
        erros.append('Processador e Placa-mãe incompatíveis (soquete diferente).')
    if mb['ram'] != ram['tipo']:
        erros.append('Placa-mãe e Memória RAM incompatíveis (tipo diferente).')
    if erros:
        for erro in erros:
            flash(erro, 'danger')
        session['etapa_atual'] = 0
        return redirect(url_for('montar_pc'))
    total = sum(pecas[cat][idx]['preco'] for cat, idx in selecoes.items())
    return render_template('montar_pc.html', etapas=etapas, etapa_atual=len(etapas)-1, categoria=etapas[-1], pecas=pecas, selecao=selecoes.get(etapas[-1], 0), selecoes=selecoes, total=total, resumo=True)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('montar_pc'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
