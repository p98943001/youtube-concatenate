import os
from youtube_concatenate.settings import DOWNLOADS_DIR
from youtube_concatenate.settings import VIDEOS_DIR
from youtube_concatenate.settings import CAPTIONS_DIR


class Utils():
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    def video_list_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def caption_file_exists(self, yt):
        filepath= yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0
