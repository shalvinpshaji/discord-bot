import os
from discord.ext import commands
import req


url = 'https://www.geeksforgeeks.org/fundamentals-of-algorithms/'
TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')
r = req.GetContent()
bot = commands.Bot(command_prefix='!')


@bot.command(name='topics', help='Responds with all the main topics.')
async def topics(ctx):
    await ctx.send(r.list_string)


@bot.command(name='subtopics', help='Respond with all the algorithms in given subtopic number.')
async def sub(ctx, n: int):
    message = r.get_individual_links(r.lists[n-1])
    await ctx.send(message)


@bot.command(name='get', help='Respond with the specified subtopic from specified topic')
async def get(ctx, n1: int, n2: int):
    if n1 not in range(1, len(r.links)):
        return
    ol = r.lists[n1 - 1]
    a_tags = ol.find_all('a')
    if n2 not in range(1, len(a_tags)):
        return
    tag = a_tags[n2-1]
    message, code = r.get_final_message(tag.get('href'))
    code = '**CODE**\n' + code
    if len(message) > 1999:
        parts = [message[i:i + 2000] for i in range(0, len(message), 2000)]
    else:
        parts = [message]
    if len(code) > 1999:
        code_part = [code[i:i+2000] for i in range(0, len(message), 2000)]
    else:
        code_part = [code]
    for part in parts:
        await ctx.send(part)
    for part in code_part:
        await ctx.send(part)
bot.run(TOKEN)
