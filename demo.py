import datetime
import logging
import time

import pafy
import vlc
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter('022b94ff52c4f97b4a107ed49ed43e30', "/slack/events", app)
slack_web_client = WebClient(token='xoxb-67993168260-1297162771264-M1z0QI5kMa24rTkzvtLyOpE0')

class YT:
    def __init__(self, uri=None):
        self.uri = uri
        video = pafy.new(self.uri)
        best = video.getbest()
        play_url = best.url
        Instance = vlc.Instance()
        self.yt_player = Instance.media_player_new()
        Media = Instance.media_new(play_url)
        Media.get_mrl()
        self.yt_player.set_media(Media)

    def play(self):
        self.yt_player.play()

    def stop(self):
        self.yt_player.stop()

    def pause(self):
        self.yt_player.pause()

    def resume(self):
        self.yt_player.play()


onboarding_tutorials_sent = {}



@slack_events_adapter.on("message")
def message(payload):
    event = payload.get("event", {})
    print(event)
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    if 'play' in text:
        global yt
        yt = YT(uri=text[text.index('play')+6:-1])
        yt.play()



if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(port=3000, debug=True)
