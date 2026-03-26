#Bibliotecas
import discord
from discord.ext import commands
import os
#Biblioteca-end

#Permissões
perms = discord.Intents.default()
perms.message_content = True
perms.members = True
Bot = commands.Bot(command_prefix=';', intents=perms)
#Permissões-end
#Comandos

@Bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    if amount < 1:
        await ctx.send("A quantidade deve ser maior que 0.")
        return
    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'{len(deleted) - 1} mensagens foram apagadas!', delete_after=5)


@Bot.command()
@commands.has_permissions(manage_messages=True)
async def clearall(ctx):
    await ctx.message.delete()
    deleted_total = 0
    while True:
        deleted = await ctx.channel.purge(limit=100)
        deleted_total += len(deleted)
        if len(deleted) < 100000:
            break
    await ctx.send(f'{deleted_total} mensagens foram apagadas!', delete_after=5)


#Comandos-end

#Eventos
@Bot.event
async def on_ready():
    print(f'Bot {Bot.user} está online!')
#Eventos-end
#Token
with open(os.path.join(os.path.dirname(__file__), "token.txt"), "r") as f:
    TOKEN = f.read().strip()

Bot.run(TOKEN)