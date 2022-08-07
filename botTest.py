import discord

#serverId = 877618533427707944

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()

#For when someone new joins the server
@client.event
async def on_member_joined(member):
    #Gets all of the channels that are in the server that the member joined
    for channel in member.server.channels:
        if str(channel) == "general":
            client.send_message(f"""Welcome to the server {member.mention}!""")


@client.event
async def on_message(message):
    id = client.get_guild(877618533427707944)

    #List of channels that can process the bot commands
    channels = ["general"]

    #Checks if the message was sent in the right channel
    if str(message.channel) in channels:
        #Different situations for the bot to respond to 
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content ==  "!users":
            await message.channel.send(f"""Number of Members: {id.member_count}""")
    else:
        print(f"""User:{message.author} tried to do command \"{message.content}\" in the channel \"{message.channel}\"""")


client.run(token)