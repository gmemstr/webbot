import discord
from feedgen.feed import FeedGenerator
import config

token = open(".token", "r").read()

client = discord.Client()
feed = FeedGenerator()
feed.title(config.feedtitle)
feed.link(href=config.feedlink)
feed.description(config.feeddescription)

@client.event
async def on_ready():
    print("Logged in as", client.user.name, client.user.id)

@client.event
async def on_message(message):
    updateFeed(message)

def updateFeed(message):
    if str(message.channel) == config.channel:
        feed_entry = feed.add_entry()
        feed_entry.id(message.id)
        feed_entry.title('Message from ' + message.author.name)
        feed_entry.description(message.content)
        # Find out why index is sometimes 0 and sometimes 1
        feed_entry.link(href=message.embeds[0]["url"])
        feed.rss_file("discord.xml", pretty=True)
        print("RSS Updated")

client.run(token)
