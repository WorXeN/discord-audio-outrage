import discord
from discord.ext import commands, tasks
from discord.ext import commands
import os


token = "ODA5NjE2NjgyNjk5OTgwODIx.YCXsSw.pwRyEK9Dm4anYWVxMoR22mg5bys"
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
    for i in os.listdir("."):
        s+=i+"\n"
        
    embed = discord.Embed(title="Alle Files", description=s, color=0x00dbc2)
    await ctx.channel.send(embed=embed)
    

@bot.command()
async def p(ctx,audio):
    audioliste = [x for x in os.listdir('.')]
    a = ""
    print(a)
    for i in audioliste:
        print(i+"in der loop")
        if(i.endswith(('.mp3'))):
            a = ".mp3"
            break
        if(i.endswith(('.avi'))):
            a = ".avi"
            break
        if(i.endswith(('.wav'))):
            a = ".wav"
            break
        if(i.endswith(('.m4a'))):
            a = ".m4a"
            break
        
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client:
        channel = ctx.author.voice.channel   
        voice_client.play(discord.FFmpegPCMAudio(f"{audio}"+str(a)), after=lambda e: print('done', e))
    
    else:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(f"{audio}"+str(a)), after=lambda e: print('done', e))


if __name__ == '__main__':
    bot.run(token)

