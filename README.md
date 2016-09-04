# YouTube MP3

This small script aims to synchronize YouTube videos and playlists with local mp3 files.

These audio tracks can then be transefered elsewhere, for example to a smartphone using BitTorrent's Sync.

It is intended to be run periodically (eg with cron).


## Installation
```bash
> pip3 install git+https://github.com/dryvenn/youtube_mp3
```


## Usage

```bash
> youtube_mp3 -d TARGET_DIRECTORY
```


## Configuration

> As the script doesn't support any authentication, make sure all playlists are either 'Public' or 'Unlisted'.

The script will look for a configuration file named `.youtube_mp3.list` under `TARGET_DIRECTORY` (which is the working directory when not specified).

This file must contain one YouTube video or playlist URL per line (blank lines and comments preceded by "# " are allowed).

`TARGET_DIRECTORY` will get populated with the files (for single videos) and directories (for playlists).
