import discord
from collections import defaultdict
import json

TOKEN = "COLOQUE_SEU_TOKEN_AQUI"
CANAL_ID = "COLOQUE_SEU_CANAL_ID_AQUI"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

mensagens_por_usuario = defaultdict(list)

@client.event
async def on_ready():
    print(f'Logado como {client.user}')

    canal = client.get_channel(CANAL_ID)

    async for msg in canal.history(limit=None):
        if msg.author.bot:
            continue
        
        mensagens_por_usuario[str(msg.author)].append({
            "mensagem": msg.content,
            "data": str(msg.created_at)
        })

    # salvar JSON (melhor pra IA depois)
    with open("mensagens.json", "w", encoding="utf-8") as f:
        json.dump(mensagens_por_usuario, f, ensure_ascii=False, indent=4)

    print("Mensagens salvas com sucesso!")
    await client.close()

client.run(TOKEN)