from slackbot.bot import respond_to
from lib.singleton import MusicBot
from lib.youtubeplayer import Youtube

mbot = MusicBot()

@respond_to('^(p|play) (.*)$')
def play_song(message,cmd,text,*args):

    if len(result):
        mbot.player.play(result[0])
    else:
        message.reply(u'No results for: {0}'.format(text))

@respond_to('^(p|play(ing)?)$')
def playing(message,cmd,*args):
    if not mbot.bot.verify(message):
        return
    if cmd == "playing":
        message.reply(u'[{0}] Currently playing: {1}'.format(mbot.player.mode,mbot.player.current))
    elif mbot.player.current != None:
        mbot.player.playpause()
    else:
        message.reply('No song currently playing')

@respond_to('^pause$')
def pause(message,*args):
    if not mbot.bot.verify(message):
        return
    if mbot.player.current != None:
        mbot.player.playpause()
    else:
        message.reply('No song currently playing')


def stop(message,*args):
    if not mbot.bot.verify(message):
        return
    mbot.player.stop()
