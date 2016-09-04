#!/usr/bin/python3
import os
import tempfile
import unittest

from youtube_mp3 import track


class TestTrack(unittest.TestCase):

    def setUp(self):
        here = os.path.dirname(os.path.abspath(__file__))
        self._dir = tempfile.TemporaryDirectory(dir=here)
        self.dir = self._dir.name
        self.sample_url0 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        self.sample_title0 = "Rick Astley - Never Gonna Give You Up"
        self.sample_path0 = os.path.join(self.dir, self.sample_title0 + '.mp3')
        open(self.sample_path0, 'w').close()
        self.sample_url1 = "https://www.youtube.com/watch?v=eYuUAGXN0KM"
        self.sample_title1 = "Rick Astley - Take Me to Your Heart"
        self.sample_path1 = os.path.join(self.dir, self.sample_title1 + '.mp3')
        self.sample_size1 = 5050816

    def tearDown(self):
        self._dir.cleanup()

    def test_raise_on_invalid_url(self):
        with self.assertRaises(track.TrackNotFound):
            track.Track('https://google.com', './')

    def test_can_get_info(self):
        t = track.Track(self.sample_url0, self.dir)
        self.assertEqual(t.title, self.sample_title0)

    def test_is_already_there(self):
        t = track.Track(self.sample_url0, self.dir)
        self.assertTrue(t.is_already_there())

    def test_downloads_file(self):
        t = track.Track(self.sample_url1, self.dir)
        self.assertFalse(t.is_already_there())
        t.sync()
        self.assertTrue(t.is_already_there())
        self.assertEqual(os.path.getsize(self.sample_path1), self.sample_size1)


    def test_create_track_objects(self):
        ts = track.create_track_objects(self.sample_url0, self.dir)
        self.assertEqual(len(ts), 1)
