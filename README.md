WebBot
------

Transforms Discord channel messages into RSS feed.

Requires python3 and a .token file with your Discord bot's token from [here](https://discordapp.com/developers/applications/).

Frontend can be found at localhost:5000

## Running

```sh
virtualenv -p python3 .python
```

```sh
source .python/bin/activate
```

```sh
pip3 install -r requirements.txt 
```

```sh
python3 main.py
```

Note: Rename discord.xml.example to discord.xml for development purposes


## After install new libraries

```sh
pip freeze > requirements.txt
```