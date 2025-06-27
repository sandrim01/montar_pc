import subprocess
import os

# Caminhos dos scripts de coleta
scripts_coleta = [
    'app/coletar_intel.py',
    'app/scraping_pichau.py'
]

# Script de importação (opcional)
scripts_import = [
    'app/importar_csv_banco.py'
]

venv_python = os.path.join('.venv', 'Scripts', 'python.exe')

def rodar_scripts(scripts):
    for script in scripts:
        print(f'Executando {script}...')
        result = subprocess.run([venv_python, script])
        if result.returncode != 0:
            print(f'Erro ao executar {script}!')
            break

def main():
    print('Iniciando coleta de todos os dados...')
    rodar_scripts(scripts_coleta)
    print('Coleta finalizada. Iniciando importação no banco de dados...')
    rodar_scripts(scripts_import)
    print('Processo completo!')

if __name__ == '__main__':
    main()
