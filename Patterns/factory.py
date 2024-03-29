# https://realpython.com/factory-method-python/

import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id: int, title: str, artist: str):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song: Song, formatt: str) -> object:
        if formatt == 'JSON':
            return _serialize_to_json(song)
        elif formatt == 'XML':
            return _serialize_to_xml(song)
        else:
            raise ValueError(formatt)


def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)


def _serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')


a_song = Song(1, 'A Good Song', 'GoodSinger')
json_serializer = SongSerializer()
json_serializer.serialize(a_song, 'JSON')
json_serializer.serialize(a_song, 'YAML')

