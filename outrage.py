import discord
from discord.ext import commands, tasks
from discord.ext import commands
import os
import glob

token = ""
bot = commands.Bot(command_prefix=['-'], description="Hi im a Robot!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("yo im here")



@bot.listen("on_message")
async def greeter(ctx):
    if ctx.author == bot.user:
        return
    
    
@bot.command()
async def files(ctx):
    """
    Alle Dateien im Ordner um die funktion abzuspielen
    """
    s = ""
    liste = [x for x in glob.glob("files/*.wav")]
    for i in liste:
        s+=i+"\n"

    a = s.replace("files\\","")
    ausgabe = a.replace(".wav","")
    print(ausgabe)
    embed = discord.Embed(title="Alle Files", description=ausgabe, color=0x00dbc2)
    await ctx.channel.send(embed=embed)
    

@bot.command()
async def p(ctx,audio):
    """
    -p eingeben und filename aus dem -file command wählen, bsp: -p mommy
    """

    path = os.getcwd()
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client:
        channel = ctx.author.voice.channel
        voice_client.play(discord.FFmpegPCMAudio(f"files/{audio}"+".wav"), after=lambda e: print('done', e))
    
    else:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(f"files/{audio}"+".wav"), after=lambda e: print('done', e))


if __name__ == '__main__':
    bot.run(token)

