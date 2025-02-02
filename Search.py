import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("youtube-api-key")


def listvideo(query):
    URL = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={
        query}&type=video&key={API_KEY}"

    response = requests.get(url=URL)

    response.raise_for_status()

    return response.json()["items"][0]["id"]["videoId"]
