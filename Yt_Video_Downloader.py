from yt_dlp import YoutubeDL
import os
from Search import listvideo

# Video URL
# search = input("Enter any video name on youtube: ")

# videoId = listvideo(search)

# url = f"https://www.youtube.com/watch?v={videoId}"


def download_yt_combined(url):

    # Create downloads folder if it doesn't exist
    os.makedirs('static/videos', exist_ok=True)

    # yt-dlp options
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': 'static/videos/%(title)s.%(ext)s'
    }

    try:
        # Download the video
        with YoutubeDL(options) as ydl:
            ydl.download([url])
            name = ydl.extract_info(url, download=False)['title']

            return f"{name}.mp4"

        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_yt_audio_only(url):
    # Create downloads folder if it doesn't exist
    os.makedirs('static/videos', exist_ok=True)

    # yt-dlp options
    options = {
        'format': 'bestaudio[ext=mp4]',
        'outtmpl': 'static/audio/%(title)s.%(ext)s'
    }

    try:
        # Download the video
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_yt_video_only(url):
    # Create downloads folder if it doesn't exist
    os.makedirs('static/videos', exist_ok=True)

    # yt-dlp options
    options = {
        'format': 'bestvideo[ext=mp4]',
        'outtmpl': 'static/videos/%(title)s.%(ext)s'
    }

    try:
        # Download the video
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_transcript(url, lang='en', auto_sub=True):
    options = {
        'writesubtitles': True,  # Enable subtitle download
        'subtitleslangs': [lang],  # Specify subtitle language
        'skip_download': True,  # Don't download the video
        'quiet': True,  # Suppress extra logs
        'outtmpl': 'static/transcript/%(title)s.%(ext)s'  # Set output folder
    }

    # Choose auto-generated or manually uploaded subtitles
    if auto_sub:
        # Download auto-generated subtitles
        options['writeautomaticsub'] = True
    else:
        # Download manually uploaded subtitles
        options['writeautomaticsub'] = False

    with YoutubeDL(options) as ydl:
        ydl.download([url])


def download_thumbnail(url):

    options = {
        'writethumbnail': True,  # Download thumbnail
        'skip_download': True,  # Don't download the video
        # Save the thumbnail in the specified folder
        'outtmpl': 'static/thumbnail/%(title)s.%(ext)s',
        'postprocessors': [{  # Post-processing step to convert to PNG
            'key': 'ImageConvertor',
            'format': 'png',  # Convert to PNG format
        }]
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])


def get_video_info(url):
    ydl_opts = {
        'quiet': True,  # Suppress output
    }

    with YoutubeDL(ydl_opts) as ydl:
        # Set download=False to prevent downloading
        info_dict = ydl.extract_info(url, download=False)

        info = {
            "id": info_dict['id'],
            "title": info_dict['title'],
            "uploader": info_dict['uploader'],
            "upload_date": info_dict['upload_date'],
            "description": info_dict['description'],
            "view_count": info_dict['view_count'],
            "like_count": info_dict['like_count'],
            "duration": info_dict['duration'],
            "tags": info_dict['tags'],
            "channel": info_dict['channel'],
            "channel_url": info_dict['channel_url'],
            "thumbnail": info_dict['thumbnail']
        }
        return info


# download_yt_combined(url)
# download_yt_video_only(url)
# download_yt_audio_only(url)
# download_thumbnail(url)
# download_transcript(url)
# print(get_video_info(url))
