import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv("youtube-api-key")


# used to find video by name giving lisrt
def listvideo(query):
    URL = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={
        query}&type=video&key={API_KEY}"

    response = requests.get(url=URL)

    response.raise_for_status()

    response = response.json()["items"]

    videos_list = []

    for i in range(0, len(response)):
        name = response[i]["snippet"]["title"]
        video_id = response[i]["id"]["videoId"]
        thumbnail = response[i]["snippet"]["thumbnails"]["high"]
        channel_title = response[i]["snippet"]["channelTitle"]
        description = response[i]["snippet"]["description"]
        publish_time = response[i]["snippet"]["publishTime"]

        video_details = {
            "video_name": name,
            "video_id": video_id,
            "video_thumbnail": thumbnail,
            "channel_title": channel_title,
            "description": description,
            "publish_time": publish_time
        }

        videos_list.append(video_details)

    return videos_list


# print(listvideo("ishq bulawa"))


# (From MY DESIGN OUTPUT LIST)
# [{'video_name': 'Ishq Bulaava Lyric Video - Hasee Toh Phasee|Parineeti, Sidharth|Sanam Puri, Shipra Goyal', 'video_id': 'QrExPG5O0dE', 'video_thumbnail': {'url': 'https://i.ytimg.com/vi/QrExPG5O0dE/hqdefault.jpg', 'width': 480, 'height': 360}, 'channel_title': 'SonyMusicIndiaVEVO', 'description': "Presenting Ishq Bulaava Lyric Video from Hasee Toh Phasee. “It's the heart and not the ears that hear when love beckons.", 'publish_time': '2014-02-12T08:00:01Z'}]

# -----------------------------------------------------------------------------------------------------

# (DATA COMMING FROM YOUTUBE DATA API)
# {'kind': 'youtube#searchResult', 'etag': 'nQKVYz7MHGbv49UuR9TCjUp8uAU', 'id': {'kind': 'youtube#video', 'videoId': 'hxMNYkLN7tI'}, 'snippet': {'publishedAt': '2024-10-24T11:30:37Z', 'channelId': 'UC_A7K2dXFsTMAciGmnNxy-Q', 'title': 'Aaj Ki Raat -Full Song |Stree 2|Tamannaah Bhatia|Rajkummar Rao|Sachin-Jigar|Madhubanti|Divya|Amitabh', 'description': 'Get ready to groove with the full song of Aaj Ki Raat from Stree 2! Starring Tamannaah Bhatia and her electrifying dance moves, ...', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/hxMNYkLN7tI/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/hxMNYkLN7tI/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/hxMNYkLN7tI/hqdefault.jpg', 'width': 480, 'height': 360}}, 'channelTitle': 'Saregama Music', 'liveBroadcastContent': 'none', 'publishTime': '2024-10-24T11:30:37Z'}}
