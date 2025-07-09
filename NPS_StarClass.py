import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
from sqlalchemy import create_engine
import urllib

## Maneira de fazer o WebDriver Funcionar para nosso ambiente local ##
print("Inicializando o navegador...")
options = Options()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
caminho_driver = r"C:\Users\adm.luiz.vinicius\Downloads\chromedriver.exe"

print("Inicializando o navegador manualmente...")
navegador = webdriver.Chrome(
    service=Service(caminho_driver),
    options=options
)

## Definir a URL e as credenciais (Migrar para uma forma mais segura da utilização desses dados)##
url = 'https://www.app-indecx.com/'
login = "ericka.nascimento@parvi.com.br"
senha = "Ericka@123"

print("Navegando até a URL...")
navegador.get(url)
navegador.maximize_window()

print("Realizando login...")
campo_login = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#email")))
campo_login.send_keys(login)

campo_senha = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
campo_senha.send_keys(senha)

botaologin = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-block > span:nth-child(1)")))
botaologin.click()

print("Aplicando filtros...")
filtro = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > section > section > aside > div > ul > li:nth-child(2) > span > span")))
filtro.click()
time.sleep(12)

print("Selecionando NPS...")
cliqueNPS = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pdf-dashboard > div > div.session__side-bar > ul > li:nth-child(2) > span > span")))
cliqueNPS.click()
time.sleep(12)

print("Fechando filtro...")
Cliqueparafecharfiltro = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pdf-dashboard > div > div.session__side-bar > ul > li:nth-child(3) > span > span")))
Cliqueparafecharfiltro.click()
time.sleep(12)

neutro_boavista = WebDriverWait(navegador, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#panel-main")))
texto_extraido = neutro_boavista.text
time.sleep(8)

# Processar o texto extraído
linhas = texto_extraido.split('\n')  

# Lista de índices das linhas que queremos pegar
indices = [1, 6, 11, 16, 22, 27, 32, 37, 42, 47, 53, 59, 65, 71, 77]

# Lista de empresas conforme fornecido
empresas = [
    "BOA VISTA", "BRASILIA", "CAMPOS", "FLORIANO", "MANAUS", "NOSSA SENHORA", "TERESINA", "SÃO LUIS", 
    "SÃO GONÇALO", "TANGUA", "LUZIANA", "PALMARES", "PETROPOLIS", "URUÇUI", "NACIONAL"
]

notas = []

# Iterar sobre os índices desejados e capturar as notas
for i in range(len(indices)):
    index = indices[i]
    if index + 4 < len(linhas): 
        nota = linhas[index + 4].strip()  

        # Verificar se a nota é "Não há dados neste relatório" e substituir por 0
        if "Não há dados neste relatório" in nota:
            nota = '0'

        notas.append(nota)

# Criar um DataFrame com as notas e as empresas
data_atualizacao = date.today().strftime('%Y-%m-%d')  
df = pd.DataFrame({
    'Empresa': empresas[:len(notas)],  
    'Nota Filial NPS StarClass': notas,
    'data_atualizacao': data_atualizacao
})

print(df)