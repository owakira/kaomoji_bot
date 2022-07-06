from src.config import BASE_DIR
from src.services.emoji_service import load_emojis


def test_load_emojis() -> None:
    emojis = ["^_^", "[¬º-°]¬", "-_-;"]
    assert emojis == load_emojis(BASE_DIR / "tests" / "emojis_example.txt")
