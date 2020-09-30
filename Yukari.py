import configparser
import importlib
import cogs # For dynamically importing cogs

from discord.ext import commands

config = configparser.ConfigParser()
config.read('config.ini')

bot = commands.Bot(command_prefix=config['bot']['cmd_prefix'], description=config['bot']['desc'])
bot.config = config
cogs = config['bot']['cogs'].split(' ')

for cog_name in cogs:
	cog_module = importlib.import_module('cogs.{0}'.format(cog_name), package='cogs')
	cog_class = getattr(cog_module, cog_name)
	bot.add_cog(cog_class(bot))

@bot.event
async def on_ready():
	print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

token = os.environ.get('BOT_TOKEN') 

# Твой токен
bot.run(str(token))
