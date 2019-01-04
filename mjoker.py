
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime

client = commands.Bot(description="Here is some command for you", command_prefix=commands.when_mentioned_or("mw!"), pm_help = False)



@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started Soyal') #add_your_bot_name_here
	return await client.change_presence(game=discord.Game(name='Master play bot | 26790 users')) #add_your_bot_status_here
	

def is_owner(ctx):
    return ctx.message.author.id == "<@498378677512437762>" #replace_it_with_your_discord_id

def is_marcos(ctx):
    return ctx.message.author.id == "<@498378677512437762>" 		
 





		
	
@client.command(pass_context = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it!")
    except discord.ext.commands.MissingPermissions:
        await client.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: ^dm [tag person] [msg]")
	
		
		

	
	

@client.command(pass_context = True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    await client.say("Ping: {}ms".format(round((t2-t1)*1000)))





@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
    await client.send_message(channel, embed=embed)
    await client.delete_message(ctx.message)

	
	
@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)	
	
	
	


client.run(os.getenv('Token'))
