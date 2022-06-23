import typing as t
import cfig


config = cfig.Configuration()


@config.required()
def TG_BOT_TOKEN(val: str) -> str:
    """
    Token used to authenticate as a Telegram bot.

    Obtain one at https://t.me/BotFather .
    """
    return val


@config.optional()
def TK_NOTIFY_SECS(val: t.Optional[str]) -> int:
    """
    Sets after how many seconds Threadkiller notifications should be deleted.

    Defaults to 30 if not specified.
    """
    if not val:
        return 30

    try:
        return int(val)
    except (ValueError, TypeError):
        raise cfig.InvalidValueError("Not an int.")


__all__ = (
    "TG_BOT_TOKEN",
    "TK_NOTIFY_SECS",
)


if __name__ == "__main__":
    config.cli()
