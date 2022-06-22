import os
import telegram
import telegram.ext
from telegram.ext import filters
from . import config
from . import handlers


def main():
    config.config.proxies.resolve()
    application = telegram.ext.ApplicationBuilder().token(config.TG_BOT_TOKEN).build()

    application.add_handler(
        telegram.ext.CommandHandler(
            callback=handlers.pin_thread,
            command="thread",
            filters=filters.ChatType.GROUPS,
            block=False,
        )
    )

    application.add_handler(
        telegram.ext.CommandHandler(
            callback=handlers.start,
            command="start",
            filters=filters.ChatType.PRIVATE,
            block=False,
        )
    )

    application.add_handler(
        telegram.ext.MessageHandler(
            callback=handlers.purge,
            filters=~filters.REPLY & filters.ChatType.GROUPS & ~filters.User(user_id=777000) & ~filters.StatusUpdate.ALL & ~filters.COMMAND,
            block=False,
        )
    )

    application.run_polling()


if __name__ == "__main__":
    main()
