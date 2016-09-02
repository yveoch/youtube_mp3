#!/usr/bin/python3
import sys
import unittest

from youtube_mp3 import parser


class TestParser(unittest.TestCase):

    def test_config_must_exist(self):
        with self.assertRaises(FileNotFoundError):
            parser.parse_config('./does-not-exist')

    def test_url_validity_checking(self):
        good_urls = [
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'http://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'https://youtube.com/watch?v=dQw4w9WgXcQ',
            'https://youtu.be/dQw4w9WgXcQ',
            'https://www.youtube.fr/watch?v=dQw4w9WgXcQ',
            'https://www.youtube.com/results?search_query=rickroll',
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLtn57NsUdLz7Phy4bzX0f3d5_eAQQ7FCA',
        ]
        bad_urls = [
            'https://www.yutube.com/watch?v=dQw4w9WgXcQ',
            'htps://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'https:/www.youtube.com/watch?v=dQw4w9WgXcQ',
            'https://www.youtu.be.com/watch?v=dQw4w9WgXcQ',
        ]
        for url in good_urls:
            self.assertTrue(parser.is_yt_url(url))
        for url in bad_urls:
            self.assertFalse(parser.is_yt_url(url))


if __name__ == '__main__':
    unittest.main()
