
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import player
from helpers import wrap, State
from config import SUDO_FILTER
from strings import _


@Client.on_message(
    filters.command("pause", "/") & SUDO_FILTER
)
@wrap
def pause(client, message):
    if player.STATE in State.Playing:
        player.STATE = State.Paused
        player.pause_resume()
        message.reply_text(_("pause_1"))
    elif player.STATE == State.Paused:
        message.reply_text(_("pause_2"))
    else:
        message.reply_text(_("pause_3"))


@Client.on_message(
    (
        filters.command("resume", "/")
        | filters.command("play", "/")
    ) & SUDO_FILTER
)
@wrap
def resume(client, message):
    if player.STATE == State.Paused:
        player.STATE = State.Playing
        player.pause_resume()
        message.reply_text(_("pause_4"))
    else:
        message.reply_text(_("pause_5"))


@Client.on_message(
    filters.command("skip", "/") & SUDO_FILTER
)
@wrap
def skip(client, message):
    if player.STATE in (State.Playing, State.Streaming, State.Paused):
        player.STATE = State.Skipped
        player.abort()
        message.reply_text(_("skip_1"))
    else:
        message.reply_text(_("skip_2"))


__help__ = {
    "pause": [_("help_pause"), True],
    "resume": [_("help_resume"), True],
    "play": [_("help_play"), True],
    "skip": [_("help_skip"), True]
}
