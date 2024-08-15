import os
import requests

# Obtém o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o arquivo TXT
txt_path = os.path.join(script_dir, 'disparo1.txt')

# Lê o conteúdo do arquivo
with open(txt_path, 'r') as file:
    input_value = file.read().strip()  # Remove espaços em branco extras

# Define a URL da API e o cabeçalho
url = "https://langflow.mapadocliente.com.br/api/v1/run/f9775bc5-3808-4548-9d58-6feaa41f1760?stream=false"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "sk-dJTlVlAniDYUHGuheLW5abD8ng2Py2zRjSoeBLAPqQs"  # Substitua pela sua chave API
}

# Define os dados a serem enviados na solicitação
data = {
    "input_value": input_value,  # Usa o conteúdo do arquivo como input_value
    "output_type": "chat",
    "input_type": "chat",
    "tweaks": {
        "GroqModel-4hEfy": {},
        "TextOutput-K6kJ9": {},
        "SequentialTaskComponent-UAk98": {},
        "SequentialCrewComponent-PjyFd": {},
        "CrewAIAgentComponent-MCmhr": {},
        "SequentialCrewComponent-mqSeY": {},
        "SequentialTaskComponent-AWCvt": {},
        "CrewAIAgentComponent-Hyf1K": {},
        "ChatInput-6Wegn": {},
        "DynamicEmailDispatcher-72Cr9": {},
        "Prompt-5ybRu": {}
    }
}

# Faz a solicitação POST à API
response = requests.post(url, headers=headers, json=data)

# Verifica a resposta da API
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)
