import discord
from feedgen.feed import FeedGenerator

token = open(".token", "r").read()

client = discord.Client()
feed = FeedGenerator()
feed.title("Discord Channel RSS")
feed.link(href="reddit.com/r/webdev")
feed.description("Discord Channel RSS")

@client.event
async def on_ready():
    print("Logged in as", client.user.name, client.user.id)

@client.event
async def on_message(message):
    updateFeed(message)

def updateFeed(message):
    feed_entry = feed.add_entry()
    feed_entry.id(message.id)
    feed_entry.title('Message from ' + message.author.name)
    feed_entry.description(message.content)
    # Find out why index is sometimes 0 and sometimes 1
    if len(message.embeds) > 0:
        feed_entry.link(href=message.embeds[0]["url"])
    feed.rss_file("discord.xml", pretty=True)

client.run(token)
