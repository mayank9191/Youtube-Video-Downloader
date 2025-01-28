import os
import fnmatch


def find_files_with_keyword(directory, keyword):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Matches files with keyword anywhere
            if fnmatch.fnmatch(file, f"*{keyword}*"):
                matching_files.append(os.path.join(root, file))
    return matching_files.pop()


b = "[TAKE#B | 4K]  KISS OF LIFE (키스오브라이프) - Igloo.mp4"

print(b[0:5])
print(find_files_with_keyword(
    directory=r"C:\Users\Mayank\OneDrive\Desktop\YOUTUBE VIDEO DOWNLOADER\static\videos", keyword="[TAKE").replace("\\", "/"))
