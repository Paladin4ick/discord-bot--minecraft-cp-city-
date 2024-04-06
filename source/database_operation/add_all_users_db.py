"""Add all users to the database."""
import sqlite3

from disnake.ext import commands
from loguru import logger


class AddUsersDB(commands.Cog):
    """
    Constructor for CreateDB class.

    :param bot: The object of the Disnake bot or client.
    """

    def __init__(self, bot):
        """
        Create a constructor for the AddUsersDB class.

        Args:
            bot: The object of the Disnake bot or client.
        """
        self.bot = bot

    async def add_user_database(self, member, cursor, db):
        """
        Add a user to the database if they don't exist.

        This function checks for the user in the database and adds them
        with their username and initial data (e.g., 0 experience points)
        if they are not found.

        Args:
            member: Discord Member object representing the user to process.
            cursor: Database cursor object for interacting with the database.
            db: Database object.

        Exception:
            Any exception raised during database interaction.
        """
        select_user_id = 'SELECT user_id FROM users WHERE user_id=?'
        cursor.execute(select_user_id, (member.id,))
        if not cursor.fetchone():
            sql = 'INSERT INTO users VALUES (?, ?, ?)'
            sql_value = (member.id, member.name, 0)
            cursor.execute(sql, sql_value)
            db.commit()

    async def process_member(self, member, cursor, db):
        """
        Add a user to the database if the user is not there.

        Args:
            member: Discord Member object representing the user to process.
            cursor: Database cursor object for interacting with the database.
            db: Databse object.

        Raises:
            sqlite3.Error: If an error occurs during database interaction.
                Add other specific exceptions if applicable.
        """
        try:
            await self.add_user_database(member, cursor, db)

        except sqlite3.Error as error:
            logger.error(error)
            raise

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Bot ready event handler.

        Goes through all bot servers and processes each member,
        by calling `process_member`. Logs errors.
        """
        for guild in self.bot.guilds:
            members = guild.members

        try:
            with sqlite3.connect('source/database/users.db') as db:
                cur = db.cursor()

                for member in members:
                    await self.process_member(member, cur, db)
                    db.commit()
                    logger.success('Данные успешно внесены в базу данных')

        except sqlite3.Error as error:
            logger.error(error)


def setup(bot):
    """
    Add the AddUsersDB extension to the Discord bot.

    This function registers the AddUsersDB class as a cog with the Discord bot,
    enabling its functionality for managing user database interactions.

    Args:
        bot (discord.ext.commands.Bot): The Discord bot instance.
    """
    bot.add_cog(AddUsersDB(bot))
