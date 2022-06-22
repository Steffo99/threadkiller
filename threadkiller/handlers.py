import asyncio
import re
import telegram
import telegram.error
import telegram.ext
from . import config


async def purge(update: telegram.Update, _context: telegram.ext.CallbackContext):
    comments = bool(update.effective_chat.linked_chat_id)

    try:
        await update.message.delete()
    except (telegram.error.Forbidden, telegram.error.BadRequest):
        notify = True
    else:
        notify = False
    
    if notify and comments:
        reply = await update.effective_chat.send_message('⚠️ This is a comment group for a channel, but your message was not in reply to any post, so it won\'t probably be seen by anybody: please Comment on posts of the associated channel instead!', disable_notification=True)
    elif notify:
        reply = await update.effective_chat.send_message('⚠️ This is a threaded group, but your message is not in a thread, so it is likely that people will not notice your message: either create a /thread or send your message as a reply to an existing message instead!', disable_notification=True)
    elif comments:
        reply = await update.effective_chat.send_message('⛔️ Sending regular messages in this group is not allowed: please Comment on posts of the associated channel instead.', disable_notification=True)
    else:
        reply = await update.effective_chat.send_message('⛔️ Sending regular messages in this group is not allowed: all messages should start with /thread or be replies to other messages.', disable_notification=True)
    
    await asyncio.sleep(config.TK_NOTIFY_SECS)

    await reply.delete()


async def pin_thread(update: telegram.Update, _context: telegram.ext.CallbackContext):
    # Check
    try:
        (_, title) = update.effective_message.text.split(" ", 1)
    except ValueError:
        reply = await update.message.reply_text('🚫 You cannot create threads without a title.')
        await asyncio.sleep(config.TK_NOTIFY_SECS)
        await reply.delete()
        return
    
    await update.effective_message.pin(disable_notification=True)


__all__ = (
    "purge",
    "pin_thread",
)
