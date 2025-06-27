from flask import Flask, render_template, request, redirect, url_for, flash
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selecoes = {}
        for categoria in pecas:
            idx = int(request.form.get(categoria, 0))
            selecoes[categoria] = idx
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
            return render_template('index.html', pecas=pecas, selecoes=selecoes)
        # Montar resumo
        total = 0
        resumo = []
        for categoria, idx in selecoes.items():
            item = pecas[categoria][idx]
            resumo.append(f"{categoria}: {item['nome']} (R$ {item['preco']})")
            total += item['preco']
        resumo.append(f"Preço total: R$ {total}")
        return render_template('index.html', pecas=pecas, selecoes=selecoes, resumo=resumo)
    return render_template('index.html', pecas=pecas)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
