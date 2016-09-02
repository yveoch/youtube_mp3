#!/usr/bin/python3
import os
import argparse

def parse():
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
    if not os.path.exists(args.config_path):
        raise FileNotFoundError(args.config_path)


if __name__ == '__main__':
    parse()
