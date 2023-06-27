"""
Alexandre Anspach - Installé Arthur
Bot Discord qui permet de lancer des dés et plus encore.
Dernière modification : 26/06/2023
pré-alpha
"""

from random import randint
from time import sleep
import asyncio
import discord
import discord.ext
from discord.ext import commands
from CONFIG import *
from os import getenv
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = getenv("DISCORD_TOKEN")

"""Définition de fonctions"""
def spacer(_list):
	spaced_str = ""
	for element in _list:
		spaced_str+=str(element)+" "
	return spaced_str + '\n'

def verif(xdy):
	xdy_list = xdy.split("d")
	if len(xdy_list) != 2:
		return False

	for element in xdy_list:
		try:
			int(element)
		except ValueError:
			return False

	if int(xdy_list[0]) > DICE_AMOUNT_LIMIT:
		return False

	return True

async def sendMessage(ctx, msg):
	n = len(msg)//2000
	for _ in range(n+1):
		await ctx.send(msg[:2000])
		msg = msg[2000:]
		sleep(MESSAGE_RATE)

# Code
bot = commands.Bot(command_prefix=COMMAND_PREFIX, description=DESCRIPTION, intents=discord.Intents.all())

@bot.event
async def on_ready():
	print("Ready !")

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Il manque un argument.")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
	elif isinstance(error, commands.CheckFailure):
		await ctx.send("Oups vous ne pouvez iutilisez cette commande.")
	elif isinstance(error.original, discord.Forbidden):
		await ctx.send("Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande")


@bot.command()
async def coucou(ctx):
	print("Coucou, tu veux voir ma bite ?")
	await ctx.send("Coucou, tu veux voir ma bite ?")


@bot.command()
async def lance(ctx, xdy, operation=None):
	if not verif(xdy):
		print("Erreur input")
		await ctx.send(f"Tu as fait une erreur. Un dé doit être décrit comme tel: \n \t\"xdy\"\n où x est le nombre de dés et y le nombre de faces du dé. X est limité à 1000.")
		return
	xy = xdy.split("d")
	await ctx.send("Les dés sont lancé !!!")
	res = []
	dice_amount = int(xy[0])
	for i in range(dice_amount):
		dice = randint(1, int(xy[1]))
		res.append(dice)

	res_str = spacer(res)
	message = f"Les résultats sont : {res_str}"
	if operation == "+":
		message = f"Le résultat est : {sum(res)}"
	print(message)
	await sendMessage(ctx, message)

"""
@bot.command()
async def kick(ctx, user: discord.User, *reason):
	print(reason)
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason=reason)
	await sendMessage(ctx, f"{user} à été détruit par le dés de dieux, si il revient cela donnera une preuve de plus qu'il est l'antéchrist.")



@bot.command()
async def ban(ctx, user: discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason=reason)
	await sendMessage(ctx, f"{user} à été ban pour la raison suivante : {reason}.")
"""

@bot.command()
async def serverInfo(ctx):
	print("servinfo")
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
	await sendMessage(ctx, message)


bot.run(DISCORD_TOKEN)
