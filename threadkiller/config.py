import typing as t
import cfig
import enum


config = cfig.Configuration()

@config.required()
def TG_BOT_TOKEN(val: str) -> str:
    """
    Token used to authenticate as a Telegram bot.

    Obtain one at https://t.me/BotFather .
    """
    return val


@config.optional()
def TG_DEFAULT_LANG(val: t.Optional[str]) -> str:
    """
    Assume this to be the language of users for whom Telegram is not reporting a language code, or for whom a localization does not exist.

    Defaults to "en" if not specified.
    """
    return val or "en"


@config.optional()
def TG_FORCE_LANG(val: t.Optional[str]) -> t.Optional[str]:
    """
    If set, assume that all users have this language code, and show them messages in that language.
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
    "TG_DEFAULT_LANG",
    "TG_FORCE_LANG",
    "TK_NOTIFY_SECS",
)


if __name__ == "__main__":
    config.cli()
