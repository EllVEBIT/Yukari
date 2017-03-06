import random
import requests
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from discord.ext import commands
from googleapiclient.discovery import build

from . import Permissible

class Lewd(Permissible):

	def __init__(self, bot):
		super().__init__()
		self.bot = bot

		self.admins = self.bot.config['bot']['admins'].split(' ')

		self.developer_key = self.bot.config['lewd']['developer_key']
		self.context = self.bot.config['lewd']['context']

		filtered_terms = self.bot.config['lewd']['filtered'].split(' ')
		self.filtered = [term.replace('+', ' ') for term in filtered_terms]

	@commands.command(pass_context=True, no_pm=True)
	async def lewd(self, ctx, *, query: str):
		"""Gives the specified user(s) access to lewd commands."""
		if ctx.message.author.id in self.admins:
			ids = [user.id for user in ctx.message.mentions]
			names = [user.display_name for user in ctx.message.mentions]

			self.give_permission(ids)

			await self.bot.say('{0} has been added to the {1} permission list.'.format(', '.join(names), self.name))

	@commands.command(pass_context=True, no_pm=True)
	async def unlewd(self, ctx, *, query: str):
		"""Revokes access to lewd commands from the specified user(s)."""
		if ctx.message.author.id in self.admins:
			ids = [user.id for user in ctx.message.mentions]
			names = [user.display_name for user in ctx.message.mentions]

			self.remove_permission(ids)

			await self.bot.say('{0} has been removed from the {1} permission list.'.format(', '.join(names), self.name))

	@commands.command(pass_context=True, no_pm=True)
	async def butts(self, ctx):
		"""Sends a random image of a butt."""
		if ctx.message.author.id in self.get_list('permission'):
			lewd_image = self._get_lewd_image('butts')
			await self.bot.say(lewd_image)

	@commands.command(pass_context=True, no_pm=True)
	async def boobs(self, ctx):
		"""Sends a random image of a pair of breasts."""
		if ctx.message.author.id in self.get_list('permission'):
			lewd_image = self._get_lewd_image('boobs')

			await self.bot.say(lewd_image)

	@commands.command(pass_context=True, no_pm=True)
	async def hentai(self, ctx, *, query: str):
		"""Sends an image from Gelbooru. You must specify the image's tags."""
		if ctx.message.author.id in self.get_list('permission'):
			image = self._booru_search('gelbooru.com', query)

			await self.bot.say('http:{0}'.format(image))

	@commands.command(pass_context=True, no_pm=True)
	async def rule34(self, ctx, *, query: str):
		"""Sends an image from Rule34. You must specify the image's tags."""
		if ctx.message.author.id in self.get_list('permission'):
			url = self._booru_search('rule34.xxx', query)
			image = 'http:{0}'.format(url)

			await self.bot.say(image)

	@commands.command(pass_context=True, no_pm=True)
	async def furry(self, ctx, *, query: str):
		"""Sends an image of.. something."""
		if ctx.message.author.id in self.get_list('permission'):
			url = 'https://e621.net/post/index.json?tags={0}'.format(query)

			response = requests.get(url).json()
			random_index = random.randint(0, 99)
			image = response[random_index]['file_url']

			await self.bot.say(image)

	@commands.command(pass_context=True, no_pm=True)
	async def image(self, ctx, *, query: str):
		"""Search for an image."""
		if ctx.message.author.id in self.get_list('permission') and not self._filtered(query):
			service = build('customsearch', 'v1', developerKey=self.developer_key)

			result = service.cse().list(
				q=query,
				cx=self.context,
				searchType='image'
			).execute()

			resultItems = result['items']
			randomItem = random.choice(resultItems)
			randomImage = randomItem['link']

			await self.bot.say(randomImage)

	def _get_lewd_image(self, what):
		api_url = 'http://api.o{0}.ru/noise/'.format(what)

		r = requests.get(api_url)
		response = r.json()
		preview = response[0]['preview']
		r.close()

		image_url = 'http://media.o{0}.ru/{1}'.format(what, preview)
		return image_url

	def _booru_search(self, site, query):
		if query == 'random':
			url = 'http://{0}/index.php?page=post&s={1}'.format(site, query)

			r = requests.get(url)
			image = BeautifulSoup(r.text).findAll('img', id='image')[0]['src']
			r.close()

		else:
			url = 'http://{0}/index.php?page=dapi&s=post&q=index&tags={1}'.format(site, query)
			response = requests.get(url)
			root = ET.fromstring(response.text)

			random_index = random.randint(0, 99)
			image = root[random_index].get('file_url')

			response.close()

		return image

	# Could probably use regex TBH but I ain't about that life.
	def _filtered(self, query):
		try:
			query.encode('ascii')
		except UnicodeDecodeError:
			return True

		for filtered in self.filtered:
			if filtered in query.lower():
				return True

		"""
		tokens = query.split(' ')
		filtered = ' '.join(self.filtered)

		for token in tokens:
			if token.lower() in filtered:
				return True
		"""

		return False