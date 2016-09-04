#!/usr/bin/python3
import os
import logging
import requests
from youtube_dl import YoutubeDL


class TrackNotFound(Exception):

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "'" + url + "' couldn't be downloaded"


def get_youtubeinmp3_url(video_url):
    return "http://www.youtubeinmp3.com/fetch/?format=JSON&video=" + video_url


def create_track_objects(url, dir):
    """
    Create new Track instances.
    If the url points to a playlist, change the dir and create a new track for each item.
    """
    if 'list' not in url:
        return [Track(url, dir)]
    else:
        tracks = []
        ydl_opts = {'ignoreerrors': True, 'quiet': True}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.add_default_info_extractors()
            info = ydl.extract_info(url, download=False)
            if not info:
                raise TrackNotFound(url)
            logging.info("Playlist: %s", info['title'])
            dir = os.path.join(dir, info['title'])
            for entry in info['entries']:
                if entry is not None:
                    tracks.append(Track('http://youtu.be/' + entry['id'], dir))
        return tracks


class Track:
    """
    Track takes care of syncing the videos to the local mp3 files.
    """

    def __init__(self, url, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
        self.dir = dir
        res = requests.get(get_youtubeinmp3_url(url))
        try:
            res.raise_for_status()
            self.link = res.json()['link']
            self.title = res.json()['title']
            self.path = os.path.join(dir, self.title + '.mp3')
            logging.info("Track: %s", self.title)
        except (requests.exceptions.HTTPError, KeyError):
            raise TrackNotFound(url) from None

    def is_already_there(self):
        """
        Check if the mp3 has already be downloaded.
        """
        return os.path.exists(self.path)

    def sync(self):
        """
        Sync the online video to the local audio file.
        """
        if not self.is_already_there():
            logging.info("Downloading...")
            res = requests.get(self.link)
            res.raise_for_status() # should be ok though
            with open(self.path, 'wb') as f:
                f.write(res.content)
        logging.info("OK")
