from dataclasses import dataclass
from yaml import safe_load

@dataclass
class ConfigData:

    info_channel: int
    news_channel: int
    nm_channel: int

    chat_channel: int
    picture_channel: int
    commands_channel: int
    
    logs_channel: int
    qts_channel: int

    member_role: int
    quest_role: int
    moder_role: int
    adm_role: int
    
def load_config() -> ConfigData:
    with open("source/utils/config.yml", encoding="utf-8") as file:
        return ConfigData(**safe_load(file.read()))
