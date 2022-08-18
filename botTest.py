import discord
import time
import asyncio
import random
import json

#serverId = 877618533427707944
messages = joined = helloCount = 0
userMessages = {"Tintin#0921":0}

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"

token = read_token()
client = discord.Client()

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                for key, value in userMessages.items():
                    f.write(f"{key} : {value} \n")

                messages = 0
                joined = 0

                await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)

#Accessing pictures in the json file
with open('pictures.json') as f:
    pictures = json.load(f)

#For when someone new joins the server
@client.event
async def on_member_joined(member):
    global joined
    joined += 1
    #Gets all of the channels that are in the server that the member joined
    for channel in member.server.channels:
        if str(channel) == "general":
            client.send_message(f"""Welcome to the server {member.mention}!""")

@client.event
async def on_message(message):
    global messages
    messages += 1

    id = client.get_guild(877618533427707944)

    #List of channels that can process the bot commands
    channels = ["general"]

    #Checks if the message is from the bot
    if message.author != client.user:
        #Checks if the message was sent in the right channel
        if str(message.channel) in channels:
            #Different situations for the bot to respond to 
            if message.content.find("!hello") != -1:
                await message.channel.send("Hi")
            if message.content.find("!users") != -1:
                await message.channel.send(f"""Number of Members: {id.member_count}""")
            if message.content.lower().find("hello"):
                global helloCount
                helloCount += 1
            if message.content.lower().find("draven") != -1:
                picture = pictures["pic"][random.randint(0, 3)]
                await message.channel.send(picture)
            if message.content.lower().find("league") != -1:
                await message.channel.send("of Draven?")
            if str(message.author) in userMessages.keys():
                userMessages[str(message.author)] = userMessages[str(message.author)] + 1
            elif str(message.author) not in userMessages.keys():
                userMessages[str(message.author)] = 1
        else:
            print(f"""User:{message.author} tried to do command \"{message.content}\" in the channel \"{message.channel}\"""")

client.loop.create_task(update_stats())
client.run(token)
