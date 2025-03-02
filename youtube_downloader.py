# Install yt-dlp if not installed
try:
    import yt_dlp
except ModuleNotFoundError:
    import os
    os.system('pip install yt-dlp')
    import yt_dlp

from google.colab import files
import os

# Prompt user for the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Set download options
download_options = {
    'format': 'bestvideo+bestaudio/best',  # Highest quality
    'outtmpl': '%(title)s.%(ext)s',        # Save file with video title
    'merge_output_format': 'mp4'           # Ensure output is in MP4 format
}

# Download the video
with yt_dlp.YoutubeDL(download_options) as ydl:
    info = ydl.extract_info(video_url, download=True)
    filename = ydl.prepare_filename(info)

# Download the file to your system
if os.path.exists(filename):
    files.download(filename)
    print(f"Downloaded {filename} to your local system.")
else:
    print("File not found.")
