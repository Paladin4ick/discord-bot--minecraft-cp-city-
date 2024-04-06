"""Import the function to get .env from os.

The getenv function retrieves the .env file from the private folder
"""
import sqlite3
from os import getenv

import disnake
from disnake.ext import commands
from dotenv import load_dotenv
from loguru import logger
from utils import Extensions
from utils.config import load_config

load_dotenv('.venv/.env')

config = load_config()

logger.add('source/logs/log_main.log', rotation='12:00')

activity_type = (disnake.ActivityType.watching)
activity = disnake.Activity(type=activity_type, name='/yuimiko')

intents = disnake.Intents.all()
bot = commands.Bot(
    command_prefix='>',
    help_command=None,
    activity=activity,
    intents=intents,
    test_guilds=[1202846041645383730],
)


@bot.event
async def on_ready():
    """Event: bot connected.

    Connecting the bot to the database.
    Adding all users to the database
    """
    try:
        with sqlite3.connect('source/database/users.db') as db:
            cur = db.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER,
                user_name VARCHAR,
                raiting INTEGER)
                """)
            db.commit()
        logger.success('Бот успешно запущен')
    except Exception as exc:
        logger.error('Ошибка запуска бота, {0}'.format(exc))


for e in Extensions.all():
    bot.load_extension(name=f"{e['package']}.{e['name']}")

bot.run(getenv('BOT_TOKEN'))
