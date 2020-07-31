from slack import WebClient
from lib.youtubeplayer import Youtube


class Mbot(WebClient):

    def __init__(self, player, settings):
        super(Mbot, self).__init__()
        self._settings = settings
        self._player = player
        self.channelname = 'm-bot'
        self.channelid = None
        self._client = WebClient(token=self._settings.API_TOKEN)
        if self.channelname is not None:
            for c in self._client.channels:
                channel = self._client.channels[c]
                if "name" in channel and channel["name"] == self.channelname:
                    self.channelid = channel["id"]
                    break
            if self.channelid is None:
                raise Exception(u"Could not find '{0}' channel".format(self.channelname))
        self._player.on(Youtube.PLAY_TRACK, self._on_start)
        self._player.on(Youtube.PLAY_PAUSE, self._on_pause)
        self._player.on(Youtube.PLAY_PLAY, self._on_play)
        self._player.on(Youtube.PLAY_STOP, self._on_stop)

    def verify(self, message):
        if self.channelid is not None:
            if self.channelid != message.body["channel"]:
                message.reply(u"Incorrect channel, use {0}".format(self.channelname))
                return False
        return True

    def _on_start(self, song):
        if not song:
            return

        message = {'channel': self.channelid, 'message': u"Playing the song: {0}".format(song)}

        self._client.send_message(**message)

    def _on_pause(self, song):
        self._client.send_message(self.channelid, u"Pausing: {0}".format(song))

    def _on_play(self, song):
        self._client.send_message(self.channelid, u"Playing: {0}".format(song))

    def _on_stop(self, song):
        self._client.send_message(self.channelid, u"Stopping: {0}".format(song))

