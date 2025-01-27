from yt_dlp import YoutubeDL
import os

# Video URL
url = input("Enter the video URL you want to download ->")


def download_yt_video(url):

    # Create downloads folder if it doesn't exist
    os.makedirs('downloads', exist_ok=True)

    # yt-dlp options
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }

    try:
        # Download the video
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


download_yt_video(url)
