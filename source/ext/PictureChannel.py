from disnake.ext import commands
from utils.config import load_config
from disnake import Message

class Gallery(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
    
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot: return
        elif message.channel.id == self.config.picture_channel:
            if len(message.attachments) > 0:
                await message.add_reaction("❤️‍🔥")
                await message.add_reaction("💪")
                await message.add_reaction("🗿")
                
                if message.content == "":
                    name = f"ветка {message.author.display_name}"
                else:
                    name = message.content
                await message.create_thread(name=name, auto_archive_duration=60)
            else:
                await message.delete()

def setup(bot):
    bot.add_cog(Gallery(bot))