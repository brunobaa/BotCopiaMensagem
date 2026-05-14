import discord
from collections import defaultdict
import json
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNELS_RAW = os.getenv("DISCORD_CHANNELS")

print("TOKEN:", TOKEN)
print("CHANNELS:", CHANNELS_RAW)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

dados = {}

# Processa canais da ENV
canais = {}

for item in CHANNELS_RAW.split(","):

    item = item.strip()

    if not item or ":" not in item:
        continue

    nome, canal_id = item.split(":", 1)

    canais[nome.strip()] = int(canal_id.strip())

@client.event
async def on_ready():
    print(f'Logado como {client.user}')

    for nome_canal, canal_id in canais.items():

        print(f"\nColetando mensagens de: {nome_canal}")

        canal = client.get_channel(canal_id)

        if canal is None:
            print(f"Canal {nome_canal} não encontrado.")
            continue

        mensagens_por_usuario = defaultdict(list)

        async for msg in canal.history(limit=None):

            if msg.author.bot:
                continue

            mensagens_por_usuario[str(msg.author)].append({
                "mensagem": msg.content,
                "data": str(msg.created_at)
            })

        dados[nome_canal] = mensagens_por_usuario

    with open("mensagens.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    print("\nMensagens salvas com sucesso!")
    await client.close()


client.run(TOKEN)