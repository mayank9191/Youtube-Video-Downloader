from yt_dlp import YoutubeDL
import os

# Video URL
# url = input("Enter the video URL you want to download ->")


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
        'outtmpl': 'static/videos/%(title)s.%(ext)s'
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
