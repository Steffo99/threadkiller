import asyncio
import re
import telegram
import telegram.error
import telegram.ext
import telegram.constants
from . import config
from . import strings


async def ephemeral_reply_text(update: telegram.Update, msg, **kwargs):
    reply = await update.effective_chat.send_message(msg, parse_mode=telegram.constants.ParseMode.HTML, disable_notification=True, **kwargs)
    await asyncio.sleep(config.TK_NOTIFY_SECS)
    await reply.delete()


async def start(update: telegram.Update, context: telegram.ext.CallbackContext):
    await update.effective_chat.send_message(strings.start.format(bot_name=context.bot.username), parse_mode=telegram.constants.ParseMode.HTML, disable_web_page_preview=True)


async def purge(update: telegram.Update, _context: telegram.ext.CallbackContext):
    comments = bool(update.effective_chat.linked_chat_id)

    try:
        await update.message.delete()
    except (telegram.error.Forbidden, telegram.error.BadRequest):
        notify = True
    else:
        notify = False
    
    if notify and comments:
        msg = strings.notify_comments 
    elif notify:
        msg = strings.notify_threads
    elif comments:
        msg = strings.delete_comments
    else:
        msg = strings.delete_threads

    asyncio.create_task(ephemeral_reply_text(update, msg))


async def pin_thread(update: telegram.Update, _context: telegram.ext.CallbackContext):
    # Check
    try:
        (_, title) = update.effective_message.text.split(" ", 1)
    except ValueError:
        asyncio.create_task(ephemeral_reply_text(update, strings.error_missing_title))
        return
    
    # Pin
    try:
        await update.effective_message.pin(disable_notification=True)
    except (telegram.error.Forbidden, telegram.error.BadRequest):
        asyncio.create_task(ephemeral_reply_text(update, strings.error_no_threads_allowed))


__all__ = (
    "start",
    "purge",
    "pin_thread",
)
