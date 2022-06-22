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
            "thread",
            handlers.pin_thread,
            block=False,
        )
    )

    application.add_handler(
        telegram.ext.MessageHandler(
            ~filters.REPLY & filters.ChatType.GROUPS & ~filters.User(user_id=777000) & ~filters.StatusUpdate.ALL & ~filters.COMMAND,
            handlers.purge,
            block=False,
        )
    )

    application.run_polling()


if __name__ == "__main__":
    main()
