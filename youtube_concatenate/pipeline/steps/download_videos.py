from pytube import YouTube
from youtube_concatenate.pipeline.steps.step import Step
from youtube_concatenate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        yt_set = set([found.yt for found in data])
        print('videos to download:', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')

            print('downloading', url)
            try:
                YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
            except Exception as e:
                print('find error:', e)
                continue

        return data
