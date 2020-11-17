import discord
import requests
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if "!" in message.context:
        if message.content.startswith('!Help'):
            await message.channel.send('명령어를 보시겠습니까?')
        if message.content.startswith('!?'):
            await message.channel.send('https://tenor.com/view/lol-mia-league-of-legends-missing-ping-gaming-gif-17055482')
        if message.content.startswith('!노래'):
            await message.channel.send('노래는 못불러요')
        if message.content.startswith('!$'):
            if "$" in message.content:
                userName = message.content.split("$")[1]
                userData = getUserData(userName)
                e = discord.embed(title = "Foo")
                e.set_author("유저 조회 결과")
                e.set_thumbnail(url = userData["userImage"])
                for item in userData["result"]:
                    Game = item["ChampName"]+ " - " + item["GameResult"]
                    KDA = item["Kill"] + item["Death"] + item["Assist"]
                    print( Game, KDA )
                await message.channel.send(embed=e)
                # getUserData(userName)
            else:
                await  message.channel.send("값이 잘못 요청되었습니다")
                await  message.channel.send("!&닉네임")
        if message.content.startswith('!내전'):
            await message.channel.send('구현중인 명령어입니다')
        else: message.channel.send('올바른 명령어가 아닙니다.')


def getUserData(userName):
    response = requests.get("http://3964bf147c56.ngrok.io/?name="+ userName)
    json_val = response.json()
    print(json_val['userName'])


client.run('token')
