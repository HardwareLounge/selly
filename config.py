import os
from typing import List, Optional, Union

import yaml
from humanfriendly import parse_timespan


class Config:
    def __init__(self) -> None:
        # Read config.yml
        if os.path.exists("config.yml"):
            with open("config.yml", "r") as f:
                self._yml = yaml.safe_load(f)
        else:
            self._yml = {}
        # General
        self.token = self._get("token")
        self.guilds = self._get("guilds", is_int_list=True)
        self.channels = self._get("channels", is_int_list=True)
        # Delete messages that not contain a link with the following domains
        self.allowed_domains = self._get("allowed_domains", is_str_list=True)
        # Message when deleting a message without valid link
        self.message_title = self._get("message_title", "Your ad must contain a sales ad link")
        formated_allowed_domains = []
        for domain in self.allowed_domains:
            formated_allowed_domains.append(f"- {domain}")
        self.message_description = self._get(
            "message_description",
            "Please attach a link with at least one of the following domains:\\n\\n{allowed_domains}\\n\\nIf your ad not contain at least one of these domains, your message will be deleted."
        ).replace("\\n", "\n").format(allowed_domains="\n".join(formated_allowed_domains))
        message_color = self._get("message_color", "FF0000")
        if message_color.startswith("#"):
            message_color = message_color[1:]
        elif message_color.startswith("0x"):
            message_color = message_color[2:]
        self.message_color = int(message_color, 16)
        self.delete_message_after = parse_timespan(self._get("delete_message_after_seconds", "30 seconds"))
        # Delete old messages
        self.check_for_old_messages_every = parse_timespan(self._get("check_for_old_messages_every", "30 minutes"))
        self.delete_messages_older_than = parse_timespan(self._get("delete_messages_older_than", "2 weeks"))

    def _get(self, key: str, default: Optional[str] = None, is_int_list: bool = False, is_str_list: bool = False) -> Union[str, List[int], List[str]]:
        """Get a value from the config"""
        assert not (is_int_list and is_str_list), "`is_int_list` and `is_str_list` can't be True at the same time"
        # Get value
        value = os.getenv(
            key.upper(),
            self._yml.get(
                key.lower(),
                default
            )
        )
        # Check if value exists
        if value is None:
            raise ValueError(f"{repr(key)} is not configured")
        # Format value
        if is_int_list or is_str_list:
            if not isinstance(value, list):
                value = str(value).split(",")
            new_value = []
            for item in value:
                if is_int_list:
                    item = int(item)
                elif is_str_list:
                    item = str(item).strip()
                new_value.append(item)
            return new_value
        return str(value).strip()
