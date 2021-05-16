from youtube_concatenate.pipeline.steps.get_vedio_list import GetVedioList
from youtube_concatenate.pipeline.steps.download_captions import DownloadCaptions
from youtube_concatenate.pipeline.pipeline import Pipeline
from youtube_concatenate.pipeline.steps.step import StepException
from youtube_concatenate.utils import Utils
from youtube_concatenate.pipeline.steps.preflight import Preflight
from youtube_concatenate.pipeline.steps.postflight import Postflight
from youtube_concatenate.pipeline.steps.read_caption import ReadCaption
from youtube_concatenate.pipeline.steps.initialize_yt import InitializeYT


CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
    }

    steps = [
        Preflight(),
        GetVedioList(),
        InitializeYT()
        DownloadCaptions(),
        ReadCaption(),
        Postflight(),
    ]

    utils = Utils()

    ## start to run
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
