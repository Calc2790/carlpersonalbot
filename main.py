import discord
import os
import requests
import json
from discord import Intents
from dotenv import load_dotenv

load_dotenv()

# Set up intents 
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


intents = Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!quotes'):
        quote = get_quote()
        await message.channel.send(quote)
      

client.run(os.getenv('TOKEN'))
