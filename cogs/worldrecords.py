import io
import datetime
from zoneinfo import ZoneInfo
from itertools import chain

from discord import File
from discord.ext import commands, tasks
from discord.ext.commands import Context

from classes.Manager import Manager


class WorldRecords(commands.Cog, name="worldrecords"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.manager = Manager(f"{self.bot.path}/database", bot.config)

        self.categories = [
            "athletics",
            "rubiks",
            "swimming",
            "speedrun"
        ]

        # Create commands for each categories
        # Get WR, get URL
        for category in self.categories:

            description = ""
            name = category

            # WR
            command_name = "wr_" + name
            async def get_wr_command(ctx: Context, name=category):
                data = self.manager.get_one(name)
                await self.send_response(ctx, data, name, file=True)

            get_wr_command.__name__ = command_name # Mandatory
            get_wr_command.__doc__ = description

            self.bot.hybrid_command(command_name, description=description)(get_wr_command)

            # URL
            command_name = "url_" + category
            async def get_url_command(ctx: Context, name=category):
                data = self.manager.get_url(name)
                await self.send_response(ctx, data, name)

            get_url_command.__name__ = command_name # Mandatory
            get_url_command.__doc__ = description

            self.bot.hybrid_command(command_name, description=description)(get_url_command)

        self.checking.start()

    def check_wr(self) -> str:
        new_wr = {
            category: self.manager.execute_one(category)
            for category in self.categories
        }

        if not any(new_wr.values()):
            return 'No new world record'
        
        new_wr = {k: v for k, v in new_wr.items() if v is not None}

        for wr in chain(*new_wr.values()):
            return self.manager.format_new_wr(wr)


    def check_options(command_name, *option):
        match command_name:
            case 'show':
                if option[0] not in ['byName', 'byDate'] and option[1] not in ['asc', 'desc']:
                    return 
    

    async def send_response(self, ctx: Context, response, category, file=False):
        if len(response) < 2000 and not file:
            return await ctx.send(response)
        
        return await ctx.send(file=File(io.StringIO(response), f"{category}_wr.txt"))


    @commands.hybrid_command(
        name="show",
        description="Show database",
    )
    async def show(self, ctx) -> None:
        # options = self.check_options()
        # print(options)
        data = self.manager.get_all(self.categories)
        await ctx.send(file=File(io.StringIO(data), self.bot.config["show_database_filename"]))


    @commands.hybrid_command(
        name="check",
        description="Checking if there are world records",
    )
    async def check(self, ctx: Context) -> None:
        response = self.check_wr()
        await ctx.send(response)


    @commands.hybrid_command(
        name="time_left",
        description="Get time remaining before the check",
    )
    async def time_left(self, ctx: Context) -> None:
        response = self.check_wr()
        await ctx.send(response)

    
    # @tasks.loop(minutes=1)
    @tasks.loop(time=datetime.time(hour=12, tzinfo=ZoneInfo("Europe/Paris")))
    async def checking(self) -> None:
        response = self.check_wr()
        channel = self.bot.get_channel(self.bot.config['channel_id_world_records'])
        await channel.send(response)
        
    @checking.before_loop
    async def before_check(self):
        """Attend que le bot soit prêt avant de démarrer."""
        await self.bot.wait_until_ready()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WorldRecords(bot))
