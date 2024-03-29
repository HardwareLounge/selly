# selly

Manages the sales ads of the [HardwareLounge Discord server](https://discord.gg/WYXvsZGEHj "Join the Discord server"). The bot will remove old messages and check for allowed domains in messages. If a message does not contain at least one of the allowed domains, it will be deleted.

## Invite

Invite the bot with the following link:

`https://discord.com/api/oauth2/authorize?client_id=` CLIENT ID `&permissions=93184&scope=bot`

You can find the client ID in the [Discord Developer Portal](https://discord.com/developers/applications "Discord Developer Portal").

## Setup

### Local

1. `apt install python3 python3-pip`

2. `pip3 install -r requirements.txt`

3. [Configure the bot](#configuration)

4. `python3 main.py`

### Docker

1. `docker build -t selly .`

2. `docker run -d --name selly -e TOKEN=YOUR_TOKEN -e CHANNELS=YOUR_CHANNELS [...] selly` (Add the [environment variables](#configuration) with `-e`)

## Configuration

Only [General](#general) and [Delete conditions](#delete-conditions) are required. The other sections have default values.

### General

TOKEN: The bot token. You can find it in the [Discord Developer Portal](https://discord.com/developers/applications "Discord Developer Portal").

CHANNELS: A list of channel IDs where the bot is allowed to run.

### Delete conditions

ALLOWED_DOMAINS: A list of domains that are allowed in a message. If a message does not contain at least one of these domains, it will be deleted.

ALLOW_WWW_SUBDOMAINS: If this is set to `true`, the bot will also allow the `www` subdomain of the allowed domains. If a configured allowed domain contains a `www` subdomain, this will be ignored. Set this to `false` if you want to allow only the exact domain.

ALLOWED_ROLES: A list of role IDs that are allowed to post messages without a valid link. If a message does not contain at least one of the allowed domains, but the author has at least one of the allowed roles, the message will not be deleted.

### Message when deleting a message without valid link

MESSAGE_TITLE: The title of the message that will be sent when a message is deleted. Default: `Your ad must contain a sales ad link`

MESSAGE_DESCRIPTION: The description of the message that will be sent when a message is deleted. You can use `\n` for a line break and `{allowed_domains}` for a list of the allowed domains. Default: `Please attach a link with at least one of the following domains:\n\n{allowed_domains}\n\nIf your ad not contain at least one of these domains, your message will be deleted.`

MESSAGE_COLOR: The color of the message that will be sent when a message is deleted. Use a hexadecimal color code. Default: `FF0000`

DELETE_MESSAGE_AFTER: The [time](#timespan-examples) after which the message that will be sent when a message is deleted will be deleted. Default: `30 seconds`

### Delete old messages

CHECK_FOR_OLD_MESSAGES_EVERY: The [time](#timespan-examples) after which the bot will check for old messages. Default: `30 minutes`

DELETE_MESSAGES_OLDER_THAN: The [time](#timespan-examples) after which a message will be deleted. Pinned messaged and messages from bots will be ignored. Default: `2 weeks`

### Config file (for [local](#local))

Create a `config.yml` file in the root directory of the project. Use the YAML format and use lowercase for the keys.

Example of a full config:

```yaml
# General
token: xxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
channels:
  - 1059677880470216744
  - 1051200829736103998

# Delete conditions
allowed_domains:
  - ebay.com
allow_www_subdomains: true
allowed_roles:
  - 700795226817691668
  - 505097770252632081

# Message when deleting a message without valid link
message_title: Please attach a link to your ad
message_description: If you dont attach a link to your ad, your message will be deleted.
message_color: C62B2B
delete_message_after: 1 minute

# Delete old messages
check_for_old_messages_every: 5 minutes
delete_messages_older_than: 1 day
```

### Environment variables (for [Docker](#docker))

Use uppercase for the keys. Lists are separated by a comma. The environment variables will override the config file.

Example of a full config:

```bash
# General
TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CHANNELS=1059677880470216744,1051200829736103998

# Delete conditions
ALLOWED_DOMAINS=ebay.com
ALLOW_WWW_SUBDOMAINS=true
ALLOWED_ROLES=700795226817691668,505097770252632081

# Message when deleting a message without valid link
MESSAGE_TITLE=Please attach a link to your ad
MESSAGE_DESCRIPTION=If you dont attach a link to your ad, your message will be deleted.
MESSAGE_COLOR=C62B2B
DELETE_MESSAGE_AFTER=1 minute

# Delete old messages
CHECK_FOR_OLD_MESSAGES_EVERY=5 minutes
DELETE_MESSAGES_OLDER_THAN=1 day
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
