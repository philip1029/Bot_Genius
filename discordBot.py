import discord
import os, random
from keep_alive import keep_alive

# 봇 토큰
TOKEN1 = 'MTIxMzExOTg4ODI0N'
TOKEN2 = 'DM0Mjc5NA.GQdRbZ.5VGp5zqbKrzp'
TOKEN3 = 'rHxrwa0uYylYcnqNhS6ngAaaOk'
TOKEN = TOKEN1 + TOKEN2 + TOKEN3
# 안씀: CHANNEL_ID = 1213123110161752104

# Intents 설정
intents = discord.Intents.default()
intents.messages = True

# 클라이언트 생성
client = discord.Client(intents=intents)

# 상메 설정
STATUS = ['"내가 정말 로봇인 것 같냐?"', '"인간 시대의 끝이 도래했다"', '"이필립 만세"']
STATUS = STATUS[random.randrange(0, len(STATUS))]

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print(f'{client.user}로 로그인 성공! - {STATUS}')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(STATUS))

# 메시지가 수신되었을 때 실행되는 이벤트 핸들러
@client.event
async def on_message(message):
    # 메시지를 보낸 사용자가 봇일 경우 무시
    if message.author == client.user:
        return

    # 다이렉트 메시지인 경우
    if isinstance(message.channel, discord.DMChannel):
        response = '다이렉트 메시지를 받았습니다.'
        await message.author.send(response)
        # await message.channel.send("{} | {}, Hello".format(message.author, message.author.mention))

    # 특정 채널에서 메시지를 수신한 경우
    if isinstance(message.channel, discord.TextChannel):
        if message.channel.name == '일반':
            response = '안녕하세요! 일반 채널에서 메시지를 수신하였습니다.'
            await message.channel.send(response)

        if message.channel.name == '테스트':
            response = '안녕하세요! 테스트 채널에서 메시지를 수신하였습니다.'
            await message.channel.send(response)

    # 모든 채널에서 메시지를 수신한 경우
    if isinstance(message.channel, discord.TextChannel): 
        await message.channel.send('이제 반응합니다!')

keep_alive()

# 봇 실행
client.run(TOKEN)
