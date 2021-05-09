from youtube_concatenate.pipeline.steps.get_vedio_list import GetVedioList
from youtube_concatenate.pipeline.steps.step import StepException
from youtube_concatenate.pipeline.pipeline import Pipeline

CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [
        GetVedioList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
