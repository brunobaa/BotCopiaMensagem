# 🤖 Bot de Coleta de Mensagens do Discord

Este projeto consiste em um bot desenvolvido em Python que coleta mensagens de um canal específico do Discord e as organiza por usuário em um arquivo JSON.

O objetivo é permitir análise posterior (como avaliação de participação de alunos, engajamento, etc).

---

## 📌 Funcionalidades

- Conecta a um servidor do Discord via bot
- Lê todas as mensagens de um canal específico
- Agrupa mensagens por usuário
- Exporta os dados em formato JSON

---

## 🧱 Pré-requisitos

Antes de começar, você precisa ter instalado:

- Python 3.10+
- Git
- Conta no Discord
- Conta no Discord Developer Portal (para criar o bot)

---

## ⚙️ Configuração do Ambiente

### 1. Clonar o repositório

git clone https://github.com/brunobaa/BotCopiaMensagem.git


2. Criar ambiente virtual
   
python -m venv venv

3. Instalar dependências
pip install discord.py
🔐 Configuração do Bot

4. Criar bot no Discord
Acesse o Discord Developer Portal
Clique em "New Application"
Vá na aba Bot
Clique em Add Bot
Copie o TOKEN

5. Ativar permissões importantes

Na aba Bot, ative:

✅ MESSAGE CONTENT INTENT
6. Adicionar bot ao servidor

Use o link:

https://discord.com/oauth2/authorize?client_id=1494454596767322202&scope=bot&permissions=73728

7. Obter ID do canal
Ative o modo desenvolvedor no Discord:
Configurações → Avançado → Modo Desenvolvedor
Clique com botão direito no canal → Copiar ID
▶️ Executando o Projeto

8. Configure o arquivo bot.py

TOKEN = "SEU_TOKEN_AQUI"
CANAL_ID = 123456789012345678

9. Execute o bot

python bot.py
📂 Saída

O programa irá gerar um arquivo:

mensagens.json

Formato:

{
  "usuario1": ["mensagem1", "mensagem2"],
  "usuario2": ["mensagem1"]
}

👨‍💻 Autor:
Bruno Barbosa Andrade
