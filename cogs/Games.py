import random
from discord.ext import commands

class Games:

	eightball_answers = [
		'It is certain',
		'It is decidedly so',
		'Without a doubt',
		'Yes, definitely',
		'You may rely on it',
		'As I see it, yes',
		'Most likely',
		'Outlook good',
		'Yes',
		'Signs point to yes',
		'Reply hazy try again',
		'Ask again later',
		'Better not tell you now',
		'Cannot predict now',
		'Concentrate and ask again',
		'Don\'t count on it',
		'My reply is no',
		'My sources say no',
		'Outlook not so good',
		'Very doubtful'
	]

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True, no_pm=True)
	async def eightball(self, ctx, *, question : str):
		"""Ask me a question, fam."""
		# answer = self.bot.clever.ask(question)
		answer = random.choice(self.eightball_answers) + '.'
		await self.bot.say(answer)