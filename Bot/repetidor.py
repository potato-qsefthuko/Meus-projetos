#Bibliotecas
import discord
from discord.ext import commands
#Biblioteca-end

#Permissões
perms = discord.Intents.default()
perms.message_content = True
perms.members = True
Bot = commands.Bot(command_prefix=';', intents=perms)
#Permissões-end
#Comandos

#Comandos-end

#Eventos
@Bot.event
async def on_ready():
    print(f'Bot {Bot.user} está online!')
#Eventos-end
#Token
with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

Bot.run(TOKEN)