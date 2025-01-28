from flask import Flask, render_template, redirect, request
from Yt_Video_Downloader import download_yt_combined
from urllib.parse import quote
import os
import fnmatch

app = Flask(__name__)


def find_files_with_keyword(keyword, directory=r"C:\Users\Mayank\OneDrive\Desktop\YOUTUBE VIDEO DOWNLOADER\static\videos"):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Matches files with keyword anywhere
            if fnmatch.fnmatch(file, f"*{keyword}*"):
                matching_files.append(os.path.join(root, file))
    return matching_files.pop()


@app.route("/", methods=["POST", "GET"])
def home():

    if request.method == "POST":
        url_fetched = request.form["video-url"]

        name = download_yt_combined(url_fetched)

        final_path = find_files_with_keyword(
            keyword=name[0:8]).replace("\\", "/").split("DOWNLOADER/")[1]

        # print(final_path)

        encoded_filename = quote(final_path)
        # print(encoded_filename)

        return render_template("index.html", video=encoded_filename)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
