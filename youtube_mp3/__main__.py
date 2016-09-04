#!/usr/bin/python3
import sys
import logging
import parser
import track


def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    try:
        dir, urls = parser.parse()
    except (FileNotFoundError, NotAValidUrl) as e:
        logging.critical(e)
        exit(1)

    for u in urls:
        try:
            tracks = track.create_track_objects(u, dir)
        except track.TrackNotFound as e: # playlist not found
            logging.error(e)
            continue
        for t in tracks:
            try:
                t.sync()
            except track.TrackNotFound as e: # track not found
                logging.error(e)
                continue


if __name__ == '__main__':
    main()
