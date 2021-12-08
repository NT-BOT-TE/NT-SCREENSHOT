from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hello he/she {m.from_user.mention}.\n\nI'm Screenshot Bot. I can provide screenshots from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😎 Group", url="https://t.me/Ntbotgroup"
                    ),
                    InlineKeyboardButton("😌 Channel", url="https://t.me/NT_BOT_CHANNEL"),
                ],
                [InlineKeyboardButton("👤 My Boss", url="https://t.me/NT_BOT_ADMIN")],
            ]
        ),
    )
