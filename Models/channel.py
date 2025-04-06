# models/channel.py
class Channel:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ChannelRepository:
    channels = [
        Channel(1, "TVA"),
        Channel(2, "RCI"),
        Channel(3, "CBC")
    ]

    @classmethod
    def find_by_id(cls, channel_id):
        return next((c for c in cls.channels if c.id == channel_id), None)

    @classmethod
    def get_all(cls):
        return cls.channels
