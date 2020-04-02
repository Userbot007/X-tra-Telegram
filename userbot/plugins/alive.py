"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, Set it first"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`Abey Saale ψ Zinda hu mei ! Maaf krna gusse mei idhr udhr ho jata hu !.. (｀∇´)ψ`**\n\n"
                     "`Telethon version: 69.69 LMFAO\nPython:69.9\nHacked by SHadow Broker\n"
                     "`Bot created by:`Machintosh \n"
                     "`Database Status: What is a database btw ?!\n\nAlways with you, my master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "Tanya izz only Mine")
