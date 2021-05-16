import os
from youtube_concatenate.settings import CAPTIONS_DIR \
    from youtube_concatenate.settings import VIDEOS_DIR


class YT():
    def __init__(self, url):
        self.url = url
        self.id = self.get_vedio_id_from_url(self.url)
        self.caption_filepath = self.get_caption_filepah()
        self.video_filepath = self.get_video_filepath()
        self.captions = None

    @staticmethod
    def get_vedio_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self, url):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + 'txt')
