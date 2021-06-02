import os
import telegram.ext
from telegram.ext import Filters


def yeetus_deletus(update: telegram.Update, _context: telegram.ext.CallbackContext):
    update.message.reply_text('⚠️ To send messages in this group, please Comment on posts of the associated'
                              ' channel.')
    update.message.delete()


updater = telegram.ext.Updater(token=os.environ["TG_TOKEN"])
updater.dispatcher.add_handler(
    telegram.ext.MessageHandler(~Filters.reply & Filters.group & ~Filters.status_update, yeetus_deletus)
)


updater.start_polling()
