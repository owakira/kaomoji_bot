from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

greeting_keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Эмодзи в начале", switch_inline_query_current_chat=",")],
        [InlineKeyboardButton(text="Эмодзи в конце", switch_inline_query_current_chat="")],
    ],
)
