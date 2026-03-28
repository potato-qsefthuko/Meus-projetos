import discord
from discord import app_commands
from discord.ext import commands
from gemini import gemini_search
import os

# --- Configuração ---
class MyBot(commands.Bot):
    def __init__(self):
        perms = discord.Intents.default()
        perms.message_content = True
        perms.members = True
        # Mantemos o prefixo caso você queira usar ; no futuro, mas o foco é /
        super().__init__(command_prefix=';', intents=perms)

    async def setup_hook(self):
        # Isso sincroniza os comandos com o Discord assim que o bot liga
        await self.tree.sync()
        print(f"🚀 Comandos Slash sincronizados para {self.user}")

Bot = MyBot()

# --- Eventos ---
@Bot.event
async def on_ready():
    print(f'✅ Bot {Bot.user} está online!')

# --- Comandos Slash (/) ---

# 1. Comando Gemini
@Bot.tree.command(name="ia", description="Faça uma pergunta para a inteligência artificial")
@app_commands.describe(pergunta="O que você quer saber?")
async def ia(interaction: discord.Interaction, pergunta: str):
    await interaction.response.defer() # Faz o "Bot está pensando..."
    
    print(f"🤖 IA processando para {interaction.user}: {pergunta}")
    answer = gemini_search(pergunta)
    
    if answer:
        if len(answer) > 1950:
            answer = answer[:1950] + "... [Resposta muito longa]"
        await interaction.followup.send(f"### ✨ Resposta da IA\n\n{answer}")
    else:
        await interaction.followup.send("❌ Não consegui obter uma resposta agora.")

# 2. Comando Clear
@Bot.tree.command(name="clear", description="Apaga uma quantidade específica de mensagens")
@app_commands.describe(quantidade="Quantas mensagens devo apagar?")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, quantidade: int):
    if quantidade < 1:
        await interaction.response.send_message("A quantidade deve ser maior que 0.", ephemeral=True)
        return
    
    await interaction.response.defer(ephemeral=True) # Defer efêmero (só você vê)
    deleted = await interaction.channel.purge(limit=quantidade)
    await interaction.followup.send(f"**{len(deleted)}** mensagens foram apagadas!")

# 3. Comando ClearAll
@Bot.tree.command(name="clearall", description="Limpa o chat (limite de 1000 mensagens)")
@app_commands.checks.has_permissions(manage_messages=True)
async def clearall(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=1000)
    await interaction.followup.send(f"**{len(deleted)}** mensagens foram limpas do canal!")

# --- Tratamento de Erros de Permissão ---
@Bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("❌ Você não tem permissão para usar este comando!", ephemeral=True)

# --- Token ---
token_path = os.path.join(os.path.dirname(__file__), "token.txt")
with open(token_path, "r") as f:
    TOKEN = f.read().strip()

Bot.run(TOKEN)