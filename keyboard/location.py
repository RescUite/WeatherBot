from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="Отправить боту свою геолокацию",
                request_location=True,
            )
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Кнопка снизу"
)
