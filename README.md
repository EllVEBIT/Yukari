# Yukari
This is [Solero](https://solero.me/)'s Discord bot. It sends random phrases to the main channel by logging messages and through a markov chain module.

[Join our Discord](https://discord.gg/aerith-swordoath-cody) for help with configuring and extending the bot!

## Configuration
You currently need to make adjustments to a number of files to take full advantage of Yukari's features. You will need to create a channel named #lewd for the bot's lewd commands (such as $hentai and $butts) to work. I will add a way to configure this without having to manually edit the cog soon.

* _Yukari.py_ - you need to replace ``bot_token`` with your bot's token, which you can get from [here](https://discordapp.com/developers/applications/me).
* _cogs/Lewd.py_ - you need to change ``your_key`` and ``context_string``. You get your key by creating a project through Google's [developer console](https://console.developers.google.com/), and then creating server credentials. You will need to enable the Custom Search API and then retrieve the context string through that. You get 100 requests a day for free, any more than that costs money, but Google has a $300 credit trial.
* _cogs/Markov.py_ - you may rename the "magic file" by change the value of the *magic_file* field in the Markov class.
* _cogs/\_\_init\_\_.py_ - you can change ``yukari.db`` to anything you'd like.
* _yukari.db_ - you will need to make adjustments to the permissions table so that Yukari accepts commands from you and your friends. To give someone permission, add that person's Discord id# to the _permitted_ column of the command. You don't **have** to separate the ids by comma; you can separate them by vertical lines if you want.

## Prerequisites
You will need to following modules for this library to work:
* Python 3.5
* [discord.py](https://github.com/Rapptz/discord.py)
* [youtube_dl](https://github.com/rg3/youtube-dl)
* [markovify](https://github.com/jsvine/markovify)
* [urbandict](https://github.com/novel/py-urbandict)

## Commands
In addition to the following commands, there are also the standard play, stop, summon and skip commands for playing music.
### Lewd
* $hentai - send an image from [Gelbooru](http://gelbooru.com/)
* $furry - send an image from [e621](https://e621.net/)
* $rule34 - send an image from [rule34.xxx](http://rule34.xxx/)
* $butts - send an image from obutts.ru
* $boobs - send an image from oboobs.ru

### Fun
* $urban - return a definition of a term from Urban Dictionary.

### Games
* $eightball - ask the bot something.
