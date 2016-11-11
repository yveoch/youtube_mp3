#!/usr/bin/python3
import sys
import logging
from . import parser
from . import track


logger = logging.getLogger('youtube_mp3')
logformatter = logging.Formatter('%(levelname)s %(name)s %(message)s')
loghandler = logging.StreamHandler(stream=sys.stdout)
loghandler.setLevel(logging.INFO)
loghandler.setFormatter(logformatter)
logger.addHandler(loghandler)


def main():
    try:
        dir, urls = parser.parse()
    except (FileNotFoundError, parser.NotAValidUrl) as e:
        logger.critical(e)
        exit(1)

    for u in urls:
        try:
            tracks = track.create_track_objects(u, dir)
        except track.TrackNotFound as e: # playlist not found
            logger.error(e)
            continue
        for t in tracks:
            try:
                t.sync()
            except track.TrackNotFound as e: # track not found
                logger.error(e)
                continue


if __name__ == '__main__':
    main()
