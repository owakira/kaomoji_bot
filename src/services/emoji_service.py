import pathlib


def load_emojis(path_to_emojis_file: str | pathlib.Path) -> list[str]:
    """
    Loads emojis from txt file
    :param path_to_emojis_file: Path to emojis file
    :type path_to_emojis_file: str | pathlib.Path
    :return: List emojis
    :rtype: list[str]
    """
    with open(path_to_emojis_file, "r", encoding="UTF-8") as file:
        data = file.readlines()
    return [kaomoji.strip() for kaomoji in data]
