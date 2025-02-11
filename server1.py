from flask import Flask, render_template,  redirect, request, url_for
from Search import listvideo
from Yt_Video_Downloader import download_yt_combined
import fnmatch
from urllib.parse import quote
import os

app = Flask(__name__)

# I have to merge server and server1


def find_files_with_keyword(keyword, directory=r"C:\Users\Mayank\OneDrive\Desktop\YOUTUBE VIDEO DOWNLOADER\static\videos"):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Matches files with keyword anywhere
            if fnmatch.fnmatch(file, f"*{keyword}*"):
                matching_files.append(os.path.join(root, file))
    return matching_files[-1] if matching_files else None


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        name = request.form["video_name"]

        video_list = listvideo(name)

        return render_template("index1.html", list=video_list)

    return render_template("index1.html")

# In this video is being Served on this route


@app.route("/<video_id>", methods=["GET", "POST"])
def video(video_id):

    url_fetched = f"https://www.youtube.com/watch?v={video_id}"

    name = download_yt_combined(url_fetched)
    # print(name)

    if not name:
        # Return an error message or handle the failure gracefully
        return render_template("index1.html", error="Video download failed, please try again.")

    final_path = find_files_with_keyword(
        keyword=name[0:8]).replace("\\", "/").split("DOWNLOADER/")[1]

    # print(final_path)

    encoded_filename = quote(final_path)
    # print(encoded_filename)

    return render_template("index1.html", video=encoded_filename)


if __name__ == "__main__":
    app.run(debug=True)
