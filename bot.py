import discord
import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNELS = os.getenv("DISCORD_CHANNELS").split(",")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

mensagens_por_usuario = {}
usuarios_que_falaram = set()

executado = False


@client.event
async def on_ready():

    global executado

    # Impede execução duplicada
    if executado:
        return

    executado = True

    print(f'Logado como {client.user}')

    guild = client.guilds[0]

    # Percorrer canais
    for canal_info in DISCORD_CHANNELS:

        nome_canal, canal_id = canal_info.split(":")

        canal = await client.fetch_channel(int(canal_id))

        print(f"\nColetando mensagens de: {canal.name}")

        # Ler mensagens do canal
        async for msg in canal.history(limit=None):

            if msg.author.bot:
                continue

            if not msg.content.strip():
                continue

            nome_usuario = str(msg.author)

            usuarios_que_falaram.add(msg.author.id)

            if nome_usuario not in mensagens_por_usuario:
                mensagens_por_usuario[nome_usuario] = []

            mensagens_por_usuario[nome_usuario].append({
                "canal": canal.name,
                "mensagem": msg.content,
                "data": str(msg.created_at)
            })

    # Salvar mensagens
    with open("mensagens.json", "w", encoding="utf-8") as f:
        json.dump(mensagens_por_usuario, f, ensure_ascii=False, indent=4)

    print("\nMensagens salvas com sucesso!")

    # Encontrar usuários sem mensagens
    usuarios_sem_mensagem = []

    async for membro in guild.fetch_members(limit=None):

        if membro.bot:
            continue

        if membro.id not in usuarios_que_falaram:

            usuarios_sem_mensagem.append({
                "nome": str(membro),
                "id": membro.id
            })

    # Salvar usuários sem mensagens
    with open("usuarios_sem_mensagem.json", "w", encoding="utf-8") as f:
        json.dump(usuarios_sem_mensagem, f, ensure_ascii=False, indent=4)

    print("Usuários sem mensagens salvos com sucesso!")

    await client.close()


client.run(TOKEN)