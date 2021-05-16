from youtube_concatenate.pipeline.steps.step import Step
from youtube_concatenate.model.yt import YT


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]
