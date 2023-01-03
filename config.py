import os
from typing import List, Optional, Union

import yaml


class Config:
    def __init__(self) -> None:
        # Read config.yml
        if os.path.exists("config.yml"):
            with open("config.yml", "r") as f:
                self._yml = yaml.safe_load(f)
        else:
            self._yml = {}
        # Get values
        self.token = self._get("token")
        self.guilds = self._get("guilds", is_list=True)
        self.channels = self._get("channels", is_list=True)
        self.message_title = self._get("message_title")
        self.message_description = self._get("message_description")
        message_color = self._get("message_color", "FF0000")
        if message_color.startswith("#"):
            message_color = message_color[1:]
        if message_color.startswith("0x"):
            message_color = message_color[2:]
        self.message_color = int(message_color, 16)
        self.delete_message_after_seconds = int(self._get("delete_message_after_seconds", "60"))

    def _get(self, key: str, default: Optional[str] = None, is_list: bool = False) -> Union[str, List[int]]:
        """Get a value from the config"""
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
        if is_list:
            if not isinstance(value, list):
                value = str(value).split(",")
            new_value = []
            for item in value:
                new_value.append(int(item))
            return new_value
        return str(value)
