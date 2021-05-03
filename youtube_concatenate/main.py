# Get channel id by : https://socialnewsify.com/get-channel-id-by-username-youtube/
# Code comes from : https://socialnewsify.com/get-channel-id-by-username-youtube/


import urllib.request
import json
from youtube_concatenate.settings import API_KEY

print(API_KEY)

CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"


def get_all_video_in_channel(channel_id):
    api_key = 'AIzaSyDcpbfpVO-PT79-wMaPHYgoskmzQghc0a8'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
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
    return video_links


vedio_list = get_all_video_in_channel(CHANNEL_ID)
print(len(vedio_list))
