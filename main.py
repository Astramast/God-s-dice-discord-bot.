"""
Alexandre Anspach
bote disord qui permet de lancer des dés et plus encore
dernière modification : 04/04/2021
pré-alpha (lol)
"""

from random import randint
from time import sleep
import youtube_dl
import asyncio
import discord
import discord.ext
from discord.ext import commands

"""Déffinition de fonction"""




def str_translate(liste):
    string = ""
    for i in range(len(liste)):
        string += (" " + str(liste[i]))

    return string


def verif(xdy):
    info = xdy
    a = 0
    liste1 = []
    liste2 = []
    chiffres = ["1", "2", "3", "4", "4", "5", "6", "7", "8", "9", "0"]
    for i in range(len(info)):
        if info[i] != "d":
            liste1.append(info[i])
        else:
            liste2.append(info[i])
    for j in range(len(liste1)):
        if liste1[j] in chiffres:
            a += 0
        else:
            a += 1
    print("a t1 :", a)
    print(liste1)
    print(liste2)
    if liste2 == ["d"]:
        a += 0
    else:
        a += 1
    print("a t2 :", a)
    return a


# code

bot = commands.Bot(command_prefix="?", description="propriété du Cap Stanton")
musics = {}
ytdl = youtube_dl.YoutubeDL()

@bot.event
async def on_ready():
    print("Ready !")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Oups vous ne pouvez iutilisez cette commande.")
    if isinstance(error.original, discord.Forbidden):
        await ctx.send("Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande")


@bot.command()
async def coucou(ctx):
    print("Coucou, tu veux voir ma bite ?")
    await ctx.send("Coucou, tu veux voir ma bite ?")


@bot.command()
async def lance(ctx, xdy, oppération):
    erreur = verif(xdy)
    str(oppération)
    if erreur == 0:
        print("lance")
        info = xdy
        if len(info) > 15:
            await ctx.send("Arrète de faire n'importe quoi petit faquin")
            info = "1d1"
        b = 0
        liste = ["", ""]
        for j in range(len(info)):
            if info[j] != "d":
                liste[b] += info[j]
            else:
                b += 1
        await ctx.send("Les dés sont lancé !!!")
        res = []
        c = liste[0]
        c = int(c)
        for i in range(c):
            a = randint(1, int(liste[1]))
            res.append(a)
            a = 0
        res_str = str_translate(res)
        if len(res_str) <= 1070 and len(oppération) == 0:
            message = f"Les résultats sont :{res_str}"
            print(message)
            await ctx.send(message)
        if len(res_str) > 1070 and len(oppération) == 0:
            message = f"Les résultats sont :{res_str[: 1070]}"
            await ctx.send(message)
            l = 1
            rang_str = len(res_str)
            n_messages = rang_str // 2000
            while l <= n_messages:
                sleep(1)
                n = l * 1070
                l += 1
                message = res_str[n: n + 1070]
                await ctx.send(message)
        else:
            if oppération == "somme":
                somme = 0
                for i in range(len(res_str) - 1):
                    somme += res_str[i]
                message = f"Le résultat est :{somme}"
                await ctx.send(message)
            if oppération[0] == "-":
                i = 1
                a = ""
                while i <= len(res_str) - 1 :
                    a += oppération[i]
                for i in range(len(res_str) - 1):
                    res_str[i] -= int(a)
                    message = f"Les résultats sont :{res_str}"
                    print(message)
                    await ctx.send(message)

    else:
        print("Erreur input")
        await ctx.send(f"Tu as fait {erreur} erreurs. \n Un dé doit être décrit comme tel: \n \"xdy\" où x est le "
                       f"nombre de dés et y le nombre de faces")


@bot.command()
async def spam(ctx, nombre, temps, *texte):
    print("spam")
    message = " ".join(texte)
    for i in range(int(nombre) + 1):
        await ctx.send(message)
        sleep(int(temps))


@bot.command()
async def compte(ctx, nombre, temps):
    print("compte")
    for i in range(int(nombre) + 1):
        message = ""
        message += str(i)
        await ctx.send(message)
        sleep(int(temps))


@bot.command()
async def kick(ctx, user: discord.User, *reason):
    print(reason)
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(
        f"{user} à été détruit par le dés de dieux, si il revient cela donnera une preuve de plus qu'il est l'antéchriste ")



@bot.command()
async def ban(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")




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
    await ctx.send(message)
"""

bot.run("NzYxMTU1ODYyODM5NTU4MTY0.X3Wfow.eAsaacpeNbK2y_ajGU_OxcDK6_Y")
