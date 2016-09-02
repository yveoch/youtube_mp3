#!/usr/bin/python3
import os
import re
import argparse


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
    _base_dir = os.path.expanduser('~/Music/youtube_mp3/')
    try:
        _config_path = os.path.abspath(os.getenv('XDG_CONFIG_HOME'))
    except AttributeError:
        _config_path = os.path.abspath(os.path.expanduser('~/.config'))
    finally:
        _config_path = os.path.join(_config_path, 'youtube_mp3.ini')

    argparser = argparse.ArgumentParser(description='Syncs YouTube videos and playlists to local mp3 files.')
    argparser.add_argument('--destination', default=_base_dir, dest='base_dir', help='The output base folder. Defaults to \'' + _base_dir + '\'.')
    argparser.add_argument('--config', default=_config_path, dest='config_path', help='The config file location. Defaults to \'' + _config_path + '\'.')

    args = argparser.parse_args()
    return args.base_dir, args.config_path


def parse_config(config_path):
    """
    Parse config file URLs
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(config_path)


def parse():
    base_dir, config_path = parse_cli()
    re.lk


if __name__ == '__main__':
    parse_cli()
