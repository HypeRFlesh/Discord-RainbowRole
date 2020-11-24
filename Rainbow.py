import discord
import asyncio
import random
from colorama import init, Fore, Back, Style
import datetime
init(convert=True)
print(Fore.RED)
print("""
      :::::::::: :::            :::      ::::::::  :::    :::
     :+:        :+:          :+: :+:   :+:    :+: :+:    :+:
    +:+        +:+         +:+   +:+  +:+        +:+    +:+
   :#::+::#   +#+        +#++:++#++: +#++:++#++ +#++:++#++
  +#+        +#+        +#+     +#+        +#+ +#+    +#+
 #+#        #+#        #+#     #+# #+#    #+# #+#    #+#
###        ########## ###     ###  ########  ###    ###



""")
#https://discord.com/developers/applications ,make an app,make a bot,go in OAuth2,select bot,scroll and select admin , then copy the link displayed, paste that into your browser and add it to the desired server for rainbow roles
token = '' #Your token here
serverid =  #Your server id here
#turn on developer mode in settings and right click the server icon on pc and click copy ID
rainbowrolename = "RainbowRole" #Role
delay = 1 #Delay


client = discord.Client()
rainbowcolours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

async def rainbowrole(role):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("Found role.")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(rainbowcolours))
                    currentDT = datetime.datetime.now()
                    hour = str(currentDT.hour)
                    minute = str(currentDT.minute)
                    second = str(currentDT.second)
                    print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Changed {rainbowrolename} to {color}")#text 1 goes here

                except Exception:
                    await role.edit(color=random.choice(rainbowcolours))
                    currentDT = datetime.datetime.now()
                    hour = str(currentDT.hour)
                    minute = str(currentDT.minute)
                    second = str(currentDT.second)
                    print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Attempted to change role {rainbowrolename}'s color")#text 1 goes here
                    pass
                await asyncio.sleep(delay)
    print('Cannot find anything called ' + rainbowrolename)
    try:
        await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("Created "+rainbowrolename)
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("Haven't got permissions to make the role")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))

@client.event
async def on_ready():
    client.loop.create_task(rainbowrole(rainbowrolename))


client.run(token)
