import time
from pytube import YouTube
from youtube_concatenate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        ## download the package by: pip install pytube
        for yt in data:
            if utils.caption_file_exists(yt):
                print('caption exist:skip')
                continue

            print('processing url', yt.url)
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError, UnboundLocalError):
                print('Error when downloading')
                continue
            except Exception as e:
                print('!!!! Unknown "{}" Error when downloading'.format(e))
                continue

            # save the caption to a file
            text_file = open(yt.get_caption_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('runtime:', end - start, 'sec')
        return data
