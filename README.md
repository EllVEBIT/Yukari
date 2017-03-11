# Yukari
A Discord bot written in Python originally for Solero.me's Discord. It sends phrases based on what's discussed on the server and more.

## Configuration
A configuration sample is located in [config.ini](config.ini).

You will need to adjust the `token` value under the **bot** section. You may create a bot application and subsequently retrieve a bot token [here](https://discordapp.com/developers/applications/me).

In order to get image searches to work (`$image`) you'll need to adjust the `developer_key` and `context` values. You may obtain a developer key by creating a project through Google's [developer console](https://console.developers.google.com/) and then creating server credentials. You will need to enable the Custom Search API and then retrieve the context string through that. You get 100 requests a day for free, any more than that costs money. Fortunately, Google has a $300 credit trial.

## Prerequisites
You will need to following modules for this library to work:
* Python 3.5+
* [Redis](https://redis.io/)
* [discord.py](https://github.com/Rapptz/discord.py)
* [youtube_dl](https://github.com/rg3/youtube-dl)
* [markovify](https://github.com/jsvine/markovify)
* [google-api-python-client](https://github.com/google/google-api-python-client)
* [urbandict](https://github.com/novel/py-urbandict)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

## Commands
In addition to the following commands, there are also the standard play, stop, summon and skip commands for playing music.
### Lewd
* $lewd **@user** - give **@user** permission to use lewd commands
* $unlewd **@user** - revoke **@user's** permission to use lewd commands
* $hentai **tags** - send an image from [Gelbooru](http://gelbooru.com/)
* $furry **tags** - send an image from [e621](https://e621.net/)
* $rule34 **tags** - send an image from [rule34.xxx](http://rule34.xxx/)
* $butts - send an image from obutts.ru
* $boobs - send an image from oboobs.ru

### Fun
* $urban **term** - return a definition of a term from Urban Dictionary.

### Games
* $eightball **question** - ask the bot something.
