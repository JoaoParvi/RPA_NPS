# Automação de Extração de NPS | Grupo Parvi

Este projeto tem como objetivo automatizar a extração diária de dados de NPS da plataforma utilizada, processar e salvar os dados em uma instância de banco de dados SQL Server do Grupo Parvi, e utilizá-los posteriormente em relatórios analíticos (BI).

---

## 🧠 Objetivo do Projeto

Automatizar um processo repetitivo de extração manual de dados, garantindo:
- Coleta padronizada e sem erros
- Atualização diária de indicadores de NPS por filial
- Agilidade na disponibilização de dados para o BI
- Redução de esforço manual por parte da equipe

---

## ⚙️ Tecnologias Utilizadas

- `Python 3.12`
- `Selenium` (para automação web)
- `Pandas` (para manipulação de dados)
- `SQLAlchemy` e `pyodbc` (para conexão com SQL Server)
- `Jenkins` (para automação e agendamento diário)
- `GitHub` (para versionamento de código)
- `Windows + Google Chrome`

## 🚀 Como Funciona

1. Jenkins executa diariamente o script Python (`NPS_Diaria.py`)
2. O Selenium acessa a plataforma IndeCX e realiza login automatizado
3. O sistema aplica filtros para selecionar o painel NPS anual
4. Os dados de NPS por filial são extraídos e estruturados em um DataFrame
5. O DataFrame é enviado diretamente para uma tabela no SQL Server
6. Após o envio, um relatório em Power BI pode se conectar ao banco e consumir os dados atualizados

---

## 🛠️ Pré-Requisitos

- Python 3.12 instalado e configurado no PATH
- Google Chrome instalado
- Jenkins instalado e configurado
- SQL Server acessível a partir da máquina local
- ODBC Driver 17 for SQL Server
- As credenciais da plataforma IndeCX

---

## ▶️ Execução Manual (para testes)

pip install -r requirements.txt
python NPS_Diario.py


## 📊 Integração com BI

Após a inserção dos dados no banco SQL, os relatórios no Power BI se conectam diretamente à tabela:
[NPS_Vendas_Diario_IndeCX]
Permitindo análises em tempo real sobre desempenho de filiais e evolução do NPS.

---

## 🔐 Segurança

As credenciais estão **temporariamente embutidas** no script para prototipagem.

> ⚠️ **Recomendação:**  
> Para ambientes de produção, utilize variáveis de ambiente, arquivos `.env`, ou serviços de cofres de segredo como Azure Key Vault, AWS Secrets Manager ou HashiCorp Vault.

---

## 📬 Contato

**Desenvolvedor:** Luiz Vinicius & João Gabriel
**Time de BI / RPA - Grupo Parvi**  
📧 luiz.ssilva@parvi.com.br
📧 joao.mendes@parvi.com.br 