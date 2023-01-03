# selly

Manages the sales ads of the [HardwareLounge Discord server](https://discord.gg/WYXvsZGEHj "Join the Discord server").

## Invite

Invite the bot with the following link:

`https://discord.com/api/oauth2/authorize?client_id=` CLIENT ID `&permissions=11264&scope=bot`

You can find the client ID in the [Discord Developer Portal](https://discord.com/developers/applications "Discord Developer Portal").

## Configuration

**TOKEN**: The bot token. You can find it in the [Discord Developer Portal](https://discord.com/developers/applications "Discord Developer Portal").

**GUILDS**: A list of guild IDs where the bot is allowed to run.

**CHANNELS**: A list of channel IDs where the bot is allowed to run.

**MESSAGE_TITLE**: The title of the message that will be sent when a message is deleted.

**MESSAGE_DESCRIPTION**: The description of the message that will be sent when a message is deleted.

**MESSAGE_COLOR**: The color of the message that will be sent when a message is deleted. Use a hexadecimal color code. Default: `FF0000`

**DELETE_MESSAGE_AFTER**: The time in seconds after which the message will be deleted. Default: `60`

### Config file (for local)

Create a `config.yml` file in the root directory of the project. Use the YAML format and use lowercase for the keys.

Example:

```yaml
token: xxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

guilds:
  - 505059915044225046
channels:
  - 1059677880470216744
  - 1051200829736103998

message_title: Please attach a link to your ad
message_description: If you dont attach a link to your ad, your message will be deleted.
delete_message_after_seconds: 30
```

### Environment variables (for Docker)

Use uppercase for the keys. Lists are separated by a comma. The environment variables will override the config file.

Example:

```
TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GUILDS=505059915044225046
CHANNELS=1059677880470216744,1051200829736103998
MESSAGE_TITLE=Please attach a link to your ad
MESSAGE_DESCRIPTION=If you dont attach a link to your ad, your message will be deleted.
DELETE_MESSAGE_AFTER_SECONDS=30
```
