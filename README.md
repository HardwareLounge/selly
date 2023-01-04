# selly

Manages the sales ads of the [HardwareLounge Discord server](https://discord.gg/WYXvsZGEHj "Join the Discord server").

## Invite

Invite the bot with the following link:

`https://discord.com/api/oauth2/authorize?client_id=` CLIENT ID `&permissions=11264&scope=bot`

You can find the client ID in the [Discord Developer Portal](https://discord.com/developers/applications "Discord Developer Portal").

## Setup

### Local

1. `apt install python3 python3-pip`

2. `pip3 install -r requirements.txt`

3. [Configure the bot](#configuration)

4. `python3 main.py`

### Docker

1. `docker build -t selly .`

2. `docker run -d --name selly -e TOKEN=YOUR_TOKEN -e GUILDS=YOUR_GUILDS [...] selly` (Add the [environment variables](#configuration) with `-e`)

## Configuration

### General

TOKEN: The bot token. You can find it in the [Discord Developer Portal](https://discord.com/developers/applications "Discord Developer Portal").

GUILDS: A list of guild IDs where the bot is allowed to run.

CHANNELS: A list of channel IDs where the bot is allowed to run.

### Delete message without link

MESSAGE_TITLE: The title of the message that will be sent when a message is deleted. Default: `Your ad must contain a link`

MESSAGE_DESCRIPTION: The description of the message that will be sent when a message is deleted. Default: `Please attach a link to your ad. If your ad not contain a link, it will be deleted.`

MESSAGE_COLOR: The color of the message that will be sent when a message is deleted. Use a hexadecimal color code. Default: `FF0000`

DELETE_MESSAGE_AFTER: The [time](#timespan-examples) after which the message will be deleted. Default: `30 seconds`

### Delete old messages

DELETE_OLD_MESSAGES_EVERY: The [time](#timespan-examples) after which the bot will check for old messages. Default: `30 minutes`

DELETE_OLD_MESSAGES_OLDER_THAN: The [time](#timespan-examples) after which a message will be deleted. Default: `2 weeks`

### Config file (for local)

Create a `config.yml` file in the root directory of the project. Use the YAML format and use lowercase for the keys.

Example of a full config (only general is required):

```yaml
# General
token: xxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
guilds:
  - 505059915044225046
channels:
  - 1059677880470216744
  - 1051200829736103998

# Delete message without link
message_title: Please attach a link to your ad
message_description: If you dont attach a link to your ad, your message will be deleted.
message_color: C62B2B
delete_message_after: 1 minute

# Delete old messages
delete_old_messages_every: 5 minutes
delete_old_messages_older_than: 1 day
```

### Environment variables (for Docker)

Use uppercase for the keys. Lists are separated by a comma. The environment variables will override the config file.

Example of a full config (only general is required):

```
TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GUILDS=505059915044225046
CHANNELS=1059677880470216744,1051200829736103998

MESSAGE_TITLE=Please attach a link to your ad
MESSAGE_DESCRIPTION=If you dont attach a link to your ad, your message will be deleted.
MESSAGE_COLOR=C62B2B
DELETE_MESSAGE_AFTER=1 minute

DELETE_OLD_MESSAGES_EVERY=5 minutes
DELETE_OLD_MESSAGES_OLDER_THAN=1 day
```

## Timespan Examples

| Timespan | Long | Short |
| --- | --- | --- |
| 1 second | `1 second` | `1s` |
| 2 seconds | `2 seconds` | `2s` |
| 1 minute | `1 minute` | `1m` |
| 2 minutes | `2 minutes` | `2m` |
| 1 hour | `1 hour` | `1h` |
| 2 hours | `2 hours` | `2h` |
| 1 day | `1 day` | `1d` |
| 2 days | `2 days` | `2d` |
| 1 week | `1 week` | `1w` |
| 2 weeks | `2 weeks` | `2w` |
| 1 year | `1 year` | `1y` |
| 2 years | `2 years` | `2y` |
