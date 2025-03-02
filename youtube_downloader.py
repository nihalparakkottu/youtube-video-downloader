# Install yt-dlp if not installed
try:
    import yt_dlp
except ModuleNotFoundError:
    import os
    os.system('pip install yt-dlp')
    import yt_dlp

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
    ydl.download([video_url])

print("Download complete!")
