#!/usr/bin/python3
import os
import re
import sys
import argparse


_CONFIG_FILENAME = ".youtube_mp3.list"


class NotAValidUrl(Exception):

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return "'" + url + "' does not appear to be a valid YouTube URL"


def is_yt_url(url):
    regex = 'https?://(www\.)?((youtu\.be)|(youtube\.(\w{2,3})))/.*'
    return re.fullmatch(regex, url) is not None


def parse_cli():
    """
    Parse CLI args
    """
    argparser = argparse.ArgumentParser(description='Syncs YouTube videos and playlists to local mp3 files.')
    argparser.add_argument('-d', '--directory', default=os.get_cwd(), help='Target directory, defaults to ./')

    args = argparser.parse_args()
    return args.directory


def parse_config(dir):
    """
    Parse config file URLs
    """
    config = os.path.join(dir, _CONFIG_FILENAME)
    if not os.path.isdir(dir):
        raise FileNotFoundError("No such directory: " + dir)
    if not os.path.exists(config):
        raise FileNotFoundError("Could not find a " + _CONFIG_FILENAME + " in " + dir)
    urls = []
    with open(config) as f:
        for line in f.readlines():
            line = re.sub('# .*', '', line)
            line = line.lstrip().rstrip()
            if not line:
                continue
            elif not is_yt_url(line):
                raise NotAValidUrl(line)
            else:
                urls.append(line)
    return urls


def parse():
    dir = parse_cli()
    urls = parse_config(dir)
    return dir, urls


if __name__ == '__main__':
    parse_cli()
