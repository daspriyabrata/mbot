from __future__ import unicode_literals

import pafy
import vlc


class Song:
    def __init__(self, uri):
        self.uri = uri


class Youtube:

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

