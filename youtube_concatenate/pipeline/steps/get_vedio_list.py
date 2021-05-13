import urllib.request
import json

from youtube_concatenate.pipeline.steps.step import Step
from youtube_concatenate.pipeline.steps.step import StepException
from youtube_concatenate.settings import API_KEY


class GetVedioList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']

        ## url list exist
        if utils.video_list_exists(channel_id):
            print('find existing video list file of channel id:', channel_id)
            return self.read_file(utils.get_video_list_filepath(channel_id))

        ## get url list from 1-st
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                            channel_id)
        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)
        ## save video_links to file for 2-nd getting url list
        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links

    def write_to_file(self, video_links, filepath):
        with open(filepath, 'w') as f:
            for url in video_links:
                f.write(url + '\n')

    def read_file(self, filepath):
        video_links = []
        with open(filepath, 'r') as f:
            for url in f:
                video_links.append(url.strip())
        return video_links
