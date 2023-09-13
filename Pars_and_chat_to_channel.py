import requests
from bs4 import BeautifulSoup
from telethon import TelegramClient
import time


sort_anec = []


def get_first_news():
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.52'
    }

    url = 'https://www.anekdot.ru/random/anekdot/'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    anecdot = soup.find_all('div', class_="text")


    for article in anecdot:
        article_title = article.text.strip()
        sort_anec.append(article_title)

    return sort_anec


i = 0

while i < 10:
    i = i + 1
    get_first_news()
    time.sleep(1)



# Use your own values from my.telegram.org and channel tag from t.me/@your_channel_tag. Channel id can be find when yoi forward channel message to bot @JsonDumpBot
api_id = your_id
api_hash = your_hash
channel_tag = your_channel tag
channel_id = your_channel_id
client = TelegramClient(session_storage_name, api_id, api_hash)
client.connect()
# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(channel_tag, sort_anec[0]))

print(sort_anec)

async def main():
    while True:
        for x in sort_anec:

            time.sleep(15) #delay in second per every message
            await client.send_message(channel_id, x)


with client:
    client.loop.run_until_complete(main())
