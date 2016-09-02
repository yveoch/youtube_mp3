#!/usr/bin/python3
import sys
import unittest

from youtube_mp3 import parser


class TestParser(unittest.TestCase):

    def test_config_must_exist(self):
        sys.argv = ['--config ./does-not-exist']
        with self.assertRaises(FileNotFoundError):
            parser.parse()


if __name__ == '__main__':
    unittest.main()
