import disnake

from config import Config


config = Config()

intents = disnake.Intents.default()
intents.message_content = True
client = disnake.Client(intents=intents)


@client.event
async def on_ready():
    print("Ready!")


@client.event
async def on_message(message: disnake.Message):
    # Ignore bots
    if message.author.bot:
        return
    # Ignore other guilds
    if message.guild.id not in config.guilds:
        return
    # Ignore other channels
    if message.channel.id not in config.channels:
        return
    # Check if there is a link in the message
    link_in_message = False
    for word in message.content.split("\n"):
        if word.startswith("http://") or word.startswith("https://"):
            link_in_message = True
            break
    if not link_in_message:
        # Delete the message
        await message.delete()
        # Send a message
        await message.channel.send(
            embed=disnake.Embed(
                title=config.message_title,
                description=config.message_description,
                color=config.message_color
            ),
            delete_after=config.delete_message_after_seconds
        )


client.run(config.token)
