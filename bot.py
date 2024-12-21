import os
import sys
import json
import discord
from discord.ext import commands

PATH = os.path.realpath(os.path.dirname(__file__))

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

if not os.path.isfile(f"{PATH}/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{PATH}/config.json") as f:
        config = json.load(f)


class DiscordBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or(config["prefix"]),
            intents=intents,
            help_command=None,
        )
        self.config = config
        self.path = PATH
        
    async def load_cogs(self) -> None:
        """
        The code in this function is executed whenever the bot will start.
        """
        for file in os.listdir(f"{PATH}/cogs"):
            if file.endswith(".py"):
                extension = file[:-3]
                try:
                    await self.load_extension(f"cogs.{extension}")
                    # self.logger.info(f"Loaded extension '{extension}'")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    # self.logger.error(
                    #     f"Failed to load extension {extension}\n{exception}"
                    # )

    async def setup_hook(self) -> None:
        """
        This will just be executed when the bot starts the first time.
        """
        # self.logger.info(f"Logged in as {self.user.name}")
        # self.logger.info(f"discord.py API version: {discord.__version__}")
        # self.logger.info(f"Python version: {platform.python_version()}")
        # self.logger.info(
        #     f"Running on: {platform.system()} {platform.release()} ({os.name})"
        # )
        
        await self.load_cogs()

bot = DiscordBot()
bot.run(config["token"])
