import urbandict
from discord.ext import commands

class Fun:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True, no_pm=True)
	async def urban(self, ctx, *, term : str):
		"""Return an Urban Dictionary definition of a term."""
		result = urbandict.define(term)
		definition = result[0]['def'].strip()

		await self.bot.say(definition)
