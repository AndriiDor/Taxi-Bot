README.txt
==========

Telegram Forwarding Bot
------------------------

This bot acts as a Telegram user client that listens to messages from a specific source bot (e.g., TripClaimerBot) and forwards them to a list of end users via your own Telegram bot (created with BotFather). It is intended for real-time forwarding of updates to multiple clients.

1. Functionality
----------------
- Listens for incoming messages from a specified bot (e.g., TripClaimerBot).
- Forwards all message content (text, photos, documents) to one or more Telegram users.
- Uses Telethon to simulate a real Telegram user session.
- Uses python-telegram-bot to send messages from your bot.
- Works in real time, with minimal delay.

2. Requirements
---------------
- Python 3.9 or higher
- Telegram API credentials (API_ID and API_HASH)
- Telegram bot token (from BotFather)
- A Telegram account (for the user session)
- pip for package installation

3. Python Packages
------------------
Install all dependencies with:

    pip install -r requirements.txt

Dependencies:
- telethon
- python-telegram-bot
- python-dotenv

requirements.txt should contain:

    telethon
    python-telegram-bot
    python-dotenv

4. Project Structure
--------------------

Taxi_bot/
├── Taxi_bot.py             # Main logic (listening and forwarding)
├── get_id.py               # Script to retrieve a user's Telegram ID
├── .env                    # Environment variables and secrets
├── requirements.txt        # Package list for pip
└── README.txt              # This documentation

5. .env File Format
-------------------

Create a `.env` file in the root directory:

    API_ID=your_api_id_from_my.telegram.org
    API_HASH=your_api_hash
    BOT_TOKEN=your_bot_token_from_BotFather
    TARGET_USER_IDS=123456789,987654321     # Comma-separated Telegram user IDs
    SOURCE_BOT_USERNAME=TripClaimerBot      # Without the @

To get your API credentials, visit: https://my.telegram.org

6. Getting Telegram User IDs
-----------------------------

To obtain a user's Telegram ID (so your bot can forward messages to them):

1. Run get_id.py.
2. Ask the user to send a message to your bot.
3. The script will print their user ID.
4. Add that ID to the TARGET_USER_IDS in .env.

Note: A user must start a conversation with your bot before your bot can send them messages.

7. Running the Bot
------------------

Start the bot with:

    python Taxi_bot.py

On first run:
- Enter your phone number (used by the user client).
- Enter the Telegram code received by SMS.
- If 2FA is enabled, enter the password.

A .session file will be created to store your login. You won’t need to log in again unless the session is deleted.

8. Deploying to a Server (VPS)
------------------------------

Recommended setup:
- Linux VPS (e.g., Hetzner, Contabo)
- Install Python, pip, Git
- Upload or clone the project
- Create the .env file with correct credentials
- Install dependencies
- Run with screen, tmux, or systemd to keep it alive in the background

9. Limitations and Warnings
---------------------------

- This project uses Telethon (user account). Do not violate Telegram's Terms of Service. Excessive automation from user accounts can result in bans.
- Each Telethon session is tied to one phone number. To support multiple numbers/accounts, you need separate .session files and parallel scripts.
- TARGET_USER_IDS must contain only users who have sent at least one message to your bot.
- Messages are forwarded only from the specific source bot defined in .env.

10. Optional Improvements
-------------------------

- Add logging or error handling
- Support forwarding stickers, videos, etc.
- Use a database to manage user IDs dynamically
- Add an admin interface via Flask or FastAPI

Author: Andrii Dorofeiev
Year: 2025
