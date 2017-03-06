import asyncio
import discord
import wolframalpha
import json
from urllib.request import urlopen
from urllib.parse import urlencode

from discord.ext import commands

class Clever(discord.Client):

	api_key = None
	wolfram = None

	def __init__(self, bot):
		self.bot = bot

		self.response_whitelist = self.bot.config['clever']['channels'].split(' ')

		response_blacklist = self.bot.config['clever']['user_blacklist'].split(' ')
		self.response_blacklist = list(map(int, response_blacklist))

		if self.bot.config['clever']['api_key']:
			self.api_key = self.bot.config['clever']['api_key']

		if self.bot.config['clever']['wolfram_key']:
			self.wolfram = wolframalpha.Client(self.bot.config['clever']['wolfram_key'])

	"""
	This is still being worked on.
	"""
	@commands.command(pass_context=True, no_pm=True)
	async def compute(self, ctx, *, query : str):
		"""Query something via Wolfram Aplha."""
		"""
		res = self.wolfram.query(query)

		for pod in res.pods:
			await self.bot.say(pod.text)
			await self.bot.say(pod.img)

		# await self.bot.say(next(res.results).text)
		"""

	@asyncio.coroutine
	async def on_message(self, message):
		if not self.api_key:
			return False

		appropriate_medium = message.channel.name in self.response_whitelist or message.channel.is_private

		if not message.content.startswith('$') and not int(message.author.id) in self.response_blacklist \
				and self.bot.user.mentioned_in(message) and appropriate_medium:
			stripped_message = message.clean_content.strip('@{0}'.format(self.bot.user.display_name))

			params = urlencode(
				{'key': self.api_key,
				 'input': stripped_message}
			)

			response = urlopen('https://www.cleverbot.com/getreply?{0}'.format(params)).read().decode('utf8')

			obj = json.loads(response)
			clever_response = obj['output']

			response = "{0} {1}".format(message.author.mention, clever_response)

			print('Sent response to {0}'.format(message.author.id))

			await self.bot.send_message(message.channel, response)