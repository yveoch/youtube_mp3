#!/usr/bin/python3
import os
import sys
import unittest
import tempfile

from youtube_mp3 import parser


class TestParser(unittest.TestCase):

    def setUp(self):
        here = os.path.dirname(os.path.abspath(__file__))
        self._config_dir = tempfile.TemporaryDirectory(dir=here)
        self.config_dir = self._config_dir.name
        self.config = os.path.join(self.config_dir, parser._CONFIG_FILENAME)
        self.urls = [
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'https://www.youtube.com/playlist?list=PLjqNIb_ZU6K8Jh_Q01s4qXPV6n9Y1a-JW',
            'https://youtu.be/oHg5SJYRHA0'
        ]
        with open(self.config, 'w') as f:
            for url in self.urls:
                print('# a comment', file=f)
                print(url + ' # another comment', file=f)

    def tearDown(self):
        self._config_dir.cleanup()

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

    def test_retrieves_urls(self):
        urls = parser.parse_config(self.config_dir)
        self.assertEqual(urls, self.urls)


if __name__ == '__main__':
    unittest.main()
