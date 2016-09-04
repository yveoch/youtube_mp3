from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='youtube_mp3',
    version='0.1.0',
    description='Syncs YouTube videos and playlists to local mp3 files',
    long_description=long_description,
    url='https://github.com/dryvenn/youtube_mp3',
    author='dryvenn',
    author_email='dryvenn@gmail.com',
    license='MIT',
    keywords='youtube video playlist download dl sync mp3 audio',
    packages=['youtube_mp3'],
    install_requires=[
        'youtube_dl',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'youtube_mp3=youtube_mp3.__main__:main',
        ],
    },
)
