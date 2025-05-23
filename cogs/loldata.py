import requests

from discord import File
from discord.ext import commands, tasks
from discord.ext.commands import Context

puuid1 = "_A1_uhiHDYfIbPJ5-FjvsARFYW9xGHFI5Mp58wejelrjZjdYLkt2iNnzEm-be1gV6cpGIXfb3eCnOA"
puuid2 = "HSmdypw1pIsD0KS74aw6MNzElq6jAuK_QuKADPqCumlHlfybGBL_FJ5BVA2fo5_rRsUj7oZUYVJiwQ"

indexes = [(3, 4, 1), (8, 9, 6)]

class LolData(commands.Cog, name="loldata"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.hybrid_command(
        name="get",
        description="Get n games from Riot API",
    )
    async def get(self, ctx: Context, n: int) -> None:
        # self.bot.logger.info(f"The user {ctx.author} ran !{ctx.command.name}")
        games_id = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid1}/ids?type=ranked&start=0&count={n}&api_key={self.bot.config["RIOT_API_KEY"]}").json()
        for id in games_id:

            game_data = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{id}?api_key={self.bot.config["RIOT_API_KEY"]}").json()
            index = game_data['metadata']['participants'].index(puuid1)

            try:
                game_data["metadata"]['participants'].index(puuid2)
            except ValueError:
                continue
            
            if index not in [3, 8]: continue
            order = 1 if index == 8 else 0

            player1 = game_data['info']["participants"][indexes[order][0]]["championName"]
            player2 = game_data['info']["participants"][indexes[order][1]]["championName"]
            ennemy1 = game_data['info']["participants"][indexes[not order][0]]["championName"]
            ennemy2 = game_data['info']["participants"][indexes[not order][1]]["championName"]
            ennemy3 = game_data['info']["participants"][indexes[not order][2]]["championName"]
            
            result = "Win" if game_data['info']["participants"][indexes[order][0]]["win"] else "Lose"

            await ctx.send(" ".join([player1, player2, ennemy1, ennemy2, ennemy3, result]))

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LolData(bot))
