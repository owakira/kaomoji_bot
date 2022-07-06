from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

router = Router()


def insert_emoji_into_text(text: str, emoji: str) -> str:
    """
    Inserts emoji into text
    Insert start if text starts with ',' symbol
    else insert end
    :param text: Text to which want to insert
    :type text: str
    :param emoji: Emoji to insert
    :type emoji: str
    :return: Text with inserted emoji
    :rtype: str
    """
    if text.startswith(","):
        return f"{emoji} {text[1:]}"
    return f"{text} {emoji}"


@router.inline_query()
async def check(query: InlineQuery, emojis: list[str]) -> None:
    text = query.query
    result = []
    for i, emoji in enumerate(emojis):
        text_with_emoji = insert_emoji_into_text(text, emoji)
        result.append(
            InlineQueryResultArticle(
                id=str(i),
                title=text_with_emoji,
                input_message_content=InputTextMessageContent(
                    message_text=text_with_emoji,
                    parse_mode="",
                ),
            )
        )
    await query.answer(result, cache_time=0)
