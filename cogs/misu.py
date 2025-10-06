import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context


class Misu(commands.Cog, name="misu"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        # Envoyer un message de bienvenue
        channel = self.bot.get_channel(self.bot.config["channel_id_logs"])
        if channel:
            await channel.send(f"Bienvenue {member.mention} 🎉 !")

        # Donner un rôle
        try:
            role = member.guild.get_role(self.bot.config["role_id_nobody"])
            await member.add_roles(role)
            await channel.send(f"🎭 {member.name} est devenu {role.name}")
        except: pass
        

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.bot.get_channel(self.bot.config["channel_id_logs"])
        if channel:
            await channel.send(f"😢 {member.mention} a quitté le serveur…")


    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     if message.author == self.bot.user:
    #         return

    #     target_channel = self.bot.get_channel(self.bot.config["channel_id_logs"])
    #     await target_channel.send(
    #         f"📢 Message de {message.author.mention} sur {message.channel.name}"
    #     )

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Misu(bot))
