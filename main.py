import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

lists_dict = {}


@bot.command(name="new", help="Creates a new todo list")
async def create_list(ctx, list_name):
    embed = discord.Embed()
    list_name = list_name.lower()
    if list_name in lists_dict:
        embed.color = 0xff0000
        embed.title = f"**List already exists!**"
        embed.description = f"{list_name.capitalize()} already exists"
    else:
        embed.color = 0x00ff00
        embed.title = f"**List has been created!**"
        embed.description = f"New list {list_name.capitalize()} has been created!"
        lists_dict[list_name] = {}
    await ctx.send(embed=embed)


@bot.command(name="delete", help="Removes todo list")
async def delete_list(ctx, list_name):
    embed = discord.Embed()
    list_name = list_name.lower()
    if lists_dict.pop(list_name, None) is None:
        embed.color = 0xff0000
        embed.title = f"**List not found!**"
        embed.description = f"{list_name.capitalize()} was not found"
    else:
        embed.color = 0x00ff00
        embed.title = f"**List has been removed!**"
        embed.description = f"{list_name.capitalize()} has been removed!"
    await ctx.send(embed=embed)


@bot.command(name="add", help="Adds item to list")
async def add_item(ctx, item, list_name):
    embed = discord.Embed()
    item = item.lower()
    list_name = list_name.lower()
    if list_name not in lists_dict:
        embed.color = 0xff0000
        embed.title = f"**List not found!**"
        embed.description = f"{list_name.capitalize()} was not found"
    else:
        lists_dict[list_name][item] = False
        embed.color = 0x00ff00
        embed.title = list_name.capitalize()
        items = ""
        for item in lists_dict[list_name]:
            if lists_dict[list_name][item]:
                items += f"~~[X] {item.capitalize()}~~\n"
            else:
                items += f"[ \u200B \u200B ] {item.capitalize()}\n"
        embed.description = items
    await ctx.send(embed=embed)


@bot.command(name="remove", help="Removes item from list")
async def remove_item(ctx, item, list_name):
    embed = discord.Embed()
    item = item.lower()
    list_name = list_name.lower()
    if list_name not in lists_dict:
        embed.color = 0xff0000
        embed.title = f"**List not found!**"
        embed.description = f"{list_name.capitalize()} was not found"
    elif item not in lists_dict[list_name]:
        embed.color = 0xff0000
        embed.title = f"**Item was not found on list!**"
        embed.description = f"{item.capitalize()} was not found in {list_name.capitalize()}"
    else:
        lists_dict[list_name].pop(item, None)
        embed.color = 0x00ff00
        embed.title = list_name.capitalize()
        items = ""
        for item in lists_dict[list_name]:
            if lists_dict[list_name][item]:
                items += f"~~[X] {item.capitalize()}~~\n"
            else:
                items += f"[ \u200B \u200B ] {item.capitalize()}\n"
        embed.description = items
    await ctx.send(embed=embed)


@bot.command(name="done", help="Sets item as done")
async def set_done(ctx, item, list_name):
    embed = discord.Embed()
    item = item.lower()
    list_name = list_name.lower()
    if list_name not in lists_dict:
        embed.color = 0xff0000
        embed.title = f"**List not found!**"
        embed.description = f"{list_name.capitalize()} was not found"
    elif item not in lists_dict[list_name]:
        embed.color = 0xff0000
        embed.title = f"**Item was not found on list!**"
        embed.description = f"{item.capitalize()} was not found in {list_name.capitalize()}"
    else:
        lists_dict[list_name][item] = True
        embed.color = 0x00ff00
        embed.title = list_name.capitalize()
        items = ""
        for item in lists_dict[list_name]:
            if lists_dict[list_name][item]:
                items += f"~~[X] {item.capitalize()}~~\n"
            else:
                items += f"[ \u200B \u200B ] {item.capitalize()}\n"
        embed.description = items
    await ctx.send(embed=embed)


@bot.command(name="show", help="Shows list contents")
async def show_list(ctx, list_name):
    embed = discord.Embed()
    list_name = list_name.lower()
    if list_name not in lists_dict:
        embed.color = 0xff0000
        embed.title = f"**List not found!**"
        embed.description = f"{list_name.capitalize()} was not found"
    else:
        embed.title = list_name.capitalize()
        items = ""
        for item in lists_dict[list_name]:
            if lists_dict[list_name][item]:
                items += f"~~[X] {item.capitalize()}~~\n"
            else:
                items += f"[ \u200B \u200B ] {item.capitalize()}\n"
        embed.description = items
    await ctx.send(embed=embed)

bot.run(token)
