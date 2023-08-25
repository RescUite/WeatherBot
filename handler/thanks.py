from aiogram import F, Router, types

router = Router()


@router.message(F.text.lower() == "спасибо")
async def answer_to_thanks(message: types.Message):
    await message.answer(f"Всегда пожалуйста, {message.from_user.first_name}!")
