import asyncio
from telethon import TelegramClient, events
import requests

api_id = 16699338
api_hash = 'dda94abe73ffe1d1570f4db17fa74ab5'
session_name = 'my_session'
trip_bot_username = 'TripClaimerBot'

bot_token = '8021547206:AAFLTVFmgGb5qOxAMh-CCGha_Kn-udSQ08k'
target_chat_ids = [422292454, 8143052475]

def forward_message_to_chats(text):
    for chat_id in target_chat_ids:
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        data = {'chat_id': chat_id, 'text': text}
        try:
            r = requests.post(url, data=data, timeout=5)
            if r.status_code != 200:
                print(f'Failed to send to {chat_id}: {r.text}')
        except requests.exceptions.Timeout:
            print(f'Timeout when sending to {chat_id}')
        except Exception as e:
            print(f'Exception sending to {chat_id}: {e}')

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    print('Listening for TripClaimerBot messages...')

    @client.on(events.NewMessage(from_users=trip_bot_username))
    async def handler(event):
        msg = event.message.message
        forward_message_to_chats(msg)

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
