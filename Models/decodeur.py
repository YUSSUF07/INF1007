# models/decoder.py
class Decoder:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.channels = []

    def add_channel(self, channel):
        if channel not in self.channels:
            self.channels.append(channel)

class DecoderRepository:
    decoders = [
        Decoder(1, "Décodeur Hôtel 1"),
        Decoder(2, "Décodeur Hôtel 2")
    ]

    @classmethod
    def find_by_id(cls, decoder_id):
        return next((d for d in cls.decoders if d.id == decoder_id), None)

    @classmethod
    def get_all(cls):
        return cls.decoders