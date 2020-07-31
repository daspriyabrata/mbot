from slackbot.bot import respond_to
from lib.singleton import MusicBot

mbot = MusicBot()


@respond_to('help')
def help(message, *args):
    message.reply("""Available commands:
- `stop`: stop playing
- `pause`: pause playing
- `play`: continue playing
- `play QUERY`: play a song now
""")
