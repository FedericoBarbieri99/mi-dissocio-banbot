import os
import discord
from dotenv import load_dotenv

#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'mi dissocio' in message.content.lower():
       
        try: 
            await message.author.ban(reason='Meme morto')
            await message.channel.send('oh no, anyways')
        
        except:
            await message.channel.send('Sei fortunato che non posso bannarti')
        
        
client.run(TOKEN)

#Don pynguino