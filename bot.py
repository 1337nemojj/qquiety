import random
import discord
from discord.ext import commands
import openai
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
openai.api_key = config.get('API', 'ai_bot')


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def social(ctx):
    info = '```tw - https://www.twitch.tv/qquiety\ntg - https://t.me/qquietykids\ntgchat - https://t.me/qquietychat (dead)\n soon...```'
    await ctx.send(info)

@bot.command()
async def h(ctx):
    info = '```?roll - кто пойдет на мид 1-100\n?social - media links\n что-то еще но потом я у стал, кодер хочет в доту```'
    await ctx.send(info)

# @bot.command()
# async def get_username(ctx):
#     username = ctx.author.name
#     await ctx.send(f"Your username is: {username}")


@bot.command()
async def roll(ctx, num1: int, num2: int):
    if num1 > num2:
        num1, num2 = num2, num1  # Swap the values if num1 is greater than num2
    
    roll = random.randint(num1, num2)
    print(f'Roll - {roll}')
    await ctx.send(str(roll))


@bot.command()
async def ask(ctx, *, question):

    model = "gpt-3.5-turbo"
    prompt = f"Q: {question}\nA:"
    username = ctx.author.name
    print(username)

    #   imagine you are a psychologist who helps lonely people
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": f"try emitate human speech, answer in monolithic format, dont answer with list of advice instead answer have to be small 3-5 sentences and cancel it with emojj"},
            {"role": "user", "content": f"my name nemojj, {question}"}
        ]
    )

    answer = response.choices[0].message.content

    await ctx.send(answer)
    print (question, "\n", answer)
bot.run(config.get('API', 'ds_bot'))

"""
создать базу данных по привязке к каждому пользвателю 

sqllite3 

[table]
    |users|
        |name1|
            |ask|answer|date|
        |name2|
            |ask|answer|date|

автоудаление старых записей или\и контроль кол-ва завпросов и ответов


"""