from discord.client import Client
from discord.ext.commands.core import command
from discord import webhook
import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
from discord.ext import commands
import aiohttp,requests,os
from colorama import Fore

# PS.
# Selfbots are against ToS, if someone see you are using it, you might get reported and 
# permanently banned from acess to your account
# I'm not responsible of nothing that happens to your account! 
# Be carefully!

# ERROR and INFO
# For module not found - Open cmd and type pip install + {module}
# I coded using Python 3.8.0 make sure to add to path in setup

# Explanation
# Selfbots use tokens to login the bot to the account
# Token | Don't give your token to others. It gives full acess to your account. 
# Keep it private, when you change password your token changes

# If you don't know how to get your token 
# < https://www.youtube.com/watch?v=YEgFvgg7ZPI >

os.system('cls')
prefix = input(f"{Fore.YELLOW}Input your desidered prefix:\n")
token = input(f"{Fore.YELLOW}Input your token here:\n{Fore.RESET}")
Client = commands.Bot(description="DWTS",command_prefix=prefix,self_bot=True)
# In client you can choose to change your desc,prefix if you want.   

# First Command  | Delete Webhook
# Usage : prefix($)delhook + webhook link
# It deletes a webhook without being in the server or having perms to do it.
# Casually used to delete webhooks from token grabbers (my intention for yall use it)
# args goes for webhook link

@Client.event
async def on_connect():
    os.system('cls')
    print(f"{Fore.RED}Selfbot Started!")
    print(f"{Fore.RED}Username:")
    print(f"{Fore.BLUE}{Client.user.name}#{Client.user.discriminator}")
    print(f"{Fore.RED}ID:\n{Fore.BLUE}{Client.user.id}")
    print(f"{Fore.RED}Token:\n{Fore.BLUE}{token}")
    print(f"{Fore.RED}Current Prefix:\n{Fore.BLUE}{prefix}")
@Client.command()                    
async def delhook(ctx,*,args):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as session:
        async with session.get(args) as r:
            if r.status == 400:
                await ctx.send("Invalid webhook") 
# Prop it might send a message or not, i'm working on a better code just check if webhook link is working.
            if r.status == 200:
                await ctx.send("Valid webhook,deleting.")
                requests.delete(args)
                await ctx.send("Deleted!")

# Second Command | Send Webhook
# Usage : prefix($)sendhook + (message) + webhook link to send message.
# Simple code to send messages to webhooks (without spamming).
# hook_url goes for webhook link
# args goes for message/content

@Client.command()
async def sendhook(ctx,args,*,hook_url):
    hook = DiscordWebhook(url=hook_url,content=args)
    response = hook.execute()
    await ctx.message.delete()

# Third Command | Spam Webhook (unsafe!)
# Usage : prefix($)spamhook + message + webhooklink
# Spamming webhook with a message nonstop
# You might get rate limited from Discord so, I highly recommend using a VPN to avoid it.
# Basically they block your IP from discord for some mins 
# Why? You are abusing the API 
# When you get rate limited you won't be able to send messages,login or any other thing
# It usually takes 30 min and then you will be able to have acess to discord

@Client.command()
async def spamhook(ctx,args,*,hook_url):
    hook = DiscordWebhook(url=hook_url,content=args)
    while 3 > 2:
           response = hook.execute()

# Login the selfbot
Client.run(token, bot=False)
