from telegram import Bot
import asyncio

async def send_message(message):
    bot = Bot(token='7358380418:AAG6-W6M3QFTnCTil7gSa5jyN2AOSXXzJis')
    message = message
    await bot.send_message(chat_id=-1002191715820, text=message)


