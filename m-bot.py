import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

import mbot_settings

from lib.singleton import MusicBot
from lib.youtubeplayer import Youtube

mbot = MusicBot()
mbot.settings = mbot_settings

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter('022b94ff52c4f97b4a107ed49ed43e30', "/slack/events", app)
slack_web_client = WebClient(token='xoxb-67993168260-1297162771264-M1z0QI5kMa24rTkzvtLyOpE0')


@slack_events_adapter.on("message")
def message(payload):
    event = payload.get("event", {})
    print(event)
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    if 'play' in text:
        mbot.player = Youtube(uri=text[text.index('<h')+1:-1])
        mbot.player.play()
    if 'pause' in text:
        mbot.player.pause()
    if 'stop' in text:
        mbot.player.stop()
    if 'resume' in text:
        mbot.player.play()


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(port=3000, debug=True)
