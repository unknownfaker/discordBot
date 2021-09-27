import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트")
    await client.change_presence(status=discord.Status.online, activity=game)


@client .event
async def on_message(message):
    if message.content.startswith("안녕"):
        await  message.channel.send("반가워요!")
    if message.content.startswith("심심"):
        await  message.channel.send("공부해요!")
    if message.content.startswith("바보"):
        await  message.channel.send("그건 너고!")
    if message.content.startswith("사랑해"):
        await  message.channel.send("저두요!")
    if message.content.startswith("넌 뭐야"):
        await  message.channel.send("대화봇인데요?")
    if message.content.startswith("방장"):
        await  message.channel.send("멋쟁이 멍님!")
    if message.content.startswith("비니"):
        await  message.channel.send("존잘 꿀보이스 비니님!")
    if message.content.startswith("뭐해"):
        await  message.channel.send("새로운 기능들을 개발중이에요!")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

