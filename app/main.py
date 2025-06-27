import tkinter as tk
from tkinter import ttk, messagebox

# Dados de exemplo para as peças
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

class MonteSeuPCApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Monte seu PC')
        self.geometry('600x500')
        self.selecoes = {}
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text='Monte seu PC!', font=('Arial', 18))
        label.pack(pady=10)
        self.comboboxes = {}
        for categoria in pecas:
            frame = ttk.Frame(self)
            frame.pack(pady=5, fill='x', padx=20)
            lbl = ttk.Label(frame, text=categoria, width=15)
            lbl.pack(side='left')
            valores = [f"{item['nome']} (R$ {item['preco']})" for item in pecas[categoria]]
            cb = ttk.Combobox(frame, values=valores, state='readonly')
            cb.current(0)
            cb.pack(side='left', padx=10)
            self.comboboxes[categoria] = cb
        btn = ttk.Button(self, text='Finalizar Montagem', command=self.finalizar)
        btn.pack(pady=20)
        self.resumo_label = ttk.Label(self, text='', font=('Arial', 12))
        self.resumo_label.pack(pady=10)

    def finalizar(self):
        # Verificar compatibilidade
        idx_proc = self.comboboxes['Processador'].current()
        idx_mb = self.comboboxes['Placa-mãe'].current()
        idx_ram = self.comboboxes['Memória RAM'].current()
        proc = pecas['Processador'][idx_proc]
        mb = pecas['Placa-mãe'][idx_mb]
        ram = pecas['Memória RAM'][idx_ram]
        erros = []
        if proc['soquete'] != mb['soquete']:
            erros.append('Processador e Placa-mãe incompatíveis (soquete diferente).')
        if mb['ram'] != ram['tipo']:
            erros.append('Placa-mãe e Memória RAM incompatíveis (tipo diferente).')
        if erros:
            messagebox.showerror('Incompatibilidade', '\n'.join(erros))
            return
        total = 0
        resumo = 'Configuração escolhida:\n'
        for categoria, cb in self.comboboxes.items():
            idx = cb.current()
            item = pecas[categoria][idx]
            resumo += f"{categoria}: {item['nome']} (R$ {item['preco']})\n"
            total += item['preco']
        resumo += f"\nPreço total: R$ {total}"
        self.resumo_label.config(text=resumo)

if __name__ == '__main__':
    app = MonteSeuPCApp()
    app.mainloop()
