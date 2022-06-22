start = """👋 Hi, I'm Threadkiller!

I'm a bot designed to keep all messages in a group inside of a reply thread.

To use my features, <a href="https://t.me/{bot_name}?startgroup=yes">add me to a group</a>!

If you give me the <b>Delete Messages</b> permission, I will delete all messages sent outside of reply threads, otherwise, I'll just notify the users.

If you add me to a <b>channel discussion group</b>, I will suggest that your users use the Comment feature of your channel.

If you give me the <b>Pin Messages</b> permission, I will pin all messages starting with /thread.

Be aware that by using me, it might become impossible to forward messages in the group, since messages <u>cannot be forwarded inside threads</u>.
"""

error_missing_title = """🚫 You cannot create threads without a title."""

error_no_threads_allowed = """🚫 Threads cannot be created in this group."""

notify_comments = """⚠️ This is a comment group for a channel, but your message was not in reply to any post, so it won't probably be seen by anybody...

Please <b>comment</b> on posts of the associated channel instead!"""

notify_threads = """⚠️ This is a threaded group, but your message is not in a thread, so it is likely that people will not notice your message...

Either create a new /thread, or send your message as a reply to an existing message instead!"""

delete_comments = """⛔️ Sending regular messages in this group is not allowed.

Please <b>comment</b> on posts of the associated channel instead.""" 

delete_threads = """⛔️ Sending regular messages in this group is not allowed.

All messages must either start a new /thread, or be replies to messages in a thread."""

