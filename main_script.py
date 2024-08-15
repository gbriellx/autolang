import subprocess
import time
import logging
import os
import sys

# Configuração do logging para exibir no terminal e gravar em arquivo
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('script_execution.log')
    ]
)

# Configurações dos scripts e pausas
disparos = [
    {"script": "disparo1.py", "pause": 10},
    {"script": "disparo2.py", "pause": 10},
    {"script": "disparo3.py", "pause": 10},
    {"script": "disparo4.py", "pause": 10},
]

def find_script(script_name):
    for root, dirs, files in os.walk('.'):
        if script_name in files:
            found_path = os.path.join(root, script_name)
            logging.info(f"Script {script_name} encontrado em: {found_path}")
            return found_path
    logging.error(f"Script {script_name} não encontrado após busca completa.")
    return None

def run_script(script_name):
    script_path = find_script(script_name)
    if not script_path:
        logging.error(f"O arquivo {script_name} não foi encontrado.")
        return

    try:
        logging.info(f"Iniciando execução de {script_name}...")
        result = subprocess.run([sys.executable, script_path], check=True, text=True, capture_output=True)
        logging.info(f"{script_name} executado com sucesso.")
        logging.info(f"Saída de {script_name}: \n{result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao executar {script_name}: {e}")
        logging.error(f"Saída de erro de {script_name}: \n{e.stderr}")

if __name__ == "__main__":
    for disparo in disparos:
        logging.info(f"Iniciando {disparo['script']}. Pausa de {disparo['pause']} minutos após a execução.")
        run_script(disparo["script"])
        pause_seconds = disparo["pause"] * 60
        logging.info(f"Esperando {disparo['pause']} minutos ({pause_seconds} segundos) antes do próximo script.")
        time.sleep(pause_seconds)
        logging.info(f"Continuando com o próximo script após {disparo['pause']} minutos de pausa.")
