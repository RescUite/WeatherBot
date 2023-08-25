from aiogram import Bot, types


async def set_up_default_commands(bot: Bot):
    await bot.set_my_commands(
        [
            types.BotCommand(
                command="/start",
                description="Запустить бота",
            ),
            types.BotCommand(
                command="/weather",
                description="Узнать погоду",
            )
        ]
    )
