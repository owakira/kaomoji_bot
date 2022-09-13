import pathlib


def load_emojis(path_to_emojis_file: str | pathlib.Path) -> list[str]:
    with open(path_to_emojis_file, "r", encoding="UTF-8") as file:
        data = file.readlines()
    return [kaomoji.strip() for kaomoji in data]
