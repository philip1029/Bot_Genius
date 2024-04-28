import discord
import os
# os.system("pip3 install discord")


# 봇 토큰
TOKEN = 'MTIxMzExOTg4ODI0NDM0Mjc5NA.Gh-el2.jTHxElYYCil8eM0CkyvXiosUwev5kKqnNpLsZY'

# Intents 설정
intents = discord.Intents.default()
intents.messages = True

# 클라이언트 생성
client = discord.Client(intents=intents)

# 파일 저장 경로 지정
if os.getcwd() == "/Users/philip091029":
    os.chdir("/Users/philip091029/Desktop/python/Bot_Genius")

SCORE_FILE = './score.txt'
print(os.getcwd())

# 파일에서 점수를 불러오는 함수
def load_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'r') as file:
            return int(file.read())
    else:
        return 0

# 점수를 파일에 저장하는 함수
def save_score(score):
    with open(SCORE_FILE, 'w') as file:
        file.write(str(score))

# 봇이 준비되었을 때 실행되는 이벤트 핸들러
@client.event
async def on_ready():
    print(f'{client.user}로 로그인 성공!')
    # 봇이 준비되면 파일에서 점수를 불러옴
    global score
    score = load_score()

# 메시지가 수신되었을 때 실행되는 이벤트 핸들러
@client.event
async def on_message(message):
    global score

    # 메시지를 보낸 사용자가 봇일 경우 무시
    if message.author == client.user:
        return

    # '+1'을 입력하면 점수가 올라감
    if message.content == '+1':
        score += 1
        save_score(score)
        await message.channel.send(f'점수가 1 올랐습니다! 현재 점수: {score}')

    # '-1'을 입력하면 점수가 올라감
    if message.content == '-1':
        score -= 1
        save_score(score)
        await message.channel.send(f'점수가 1 내려갔습니다! 현재 점수: {score}')

# 봇 실행
client.run(TOKEN)
