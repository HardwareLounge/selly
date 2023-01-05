import datetime

import disnake
from disnake.ext import tasks

from config import Config


config = Config()


class Client(disnake.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await self.wait_until_ready()
        print("Ready!")
        self.delete_old_messages.start()

    async def on_message(self, message: disnake.Message):
        # Ignore bots
        if message.author.bot:
            return
        # Ignore other guilds
        if message.guild.id not in config.guilds:
            return
        # Ignore other channels
        if message.channel.id not in config.channels:
            return
        # Check if there is a valid link in the message
        valid_link_in_message = False
        for word in message.content.split(" "):
            valid_start = False
            if word.startswith("http://"):
                word = word[7:]
                valid_start = True
            elif word.startswith("https://"):
                word = word[8:]
                valid_start = True
            if valid_start:
                for domain in config.allowed_domains:
                    if valid_link_in_message:
                        break
                    valid_link_in_message = word.startswith(domain)
        if not valid_link_in_message:
            # Delete the message
            await message.delete()
            # Send a message
            await message.channel.send(
                embed=disnake.Embed(
                    title=config.message_title,
                    description=config.message_description,
                    color=config.message_color
                ),
                delete_after=config.delete_message_after
            )

    @tasks.loop(seconds=config.check_for_old_messages_every)
    async def delete_old_messages(self):
        print("Deleting old messages...")
        for guild_id in config.guilds:
            guild = self.get_guild(guild_id)
            # Skip non-existent guilds
            if guild is None:
                continue
            for channel_id in config.channels:
                channel = guild.get_channel(channel_id)
                # Skip non-existent channels
                if channel is None:
                    continue
                async for message in channel.history(limit=None):
                    # Ignore bots
                    if message.author.bot:
                        continue
                    # Delete old messages
                    if (datetime.datetime.now(datetime.timezone.utc) - message.created_at).total_seconds() > config.delete_messages_older_than:
                        print(f"Deleting message {message.id} from {message.author.id} in {repr(message.channel.id)} (created at: {message.created_at})")
                        await message.delete()
        print("Done!")


intents = disnake.Intents.default()
intents.message_content = True
client = Client(intents=intents)
client.run(config.token)
