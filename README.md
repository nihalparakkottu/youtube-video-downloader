🎬 YouTube Video Downloader
This is a simple Python program that downloads YouTube videos in the highest available quality with both audio and video combined. The script uses the powerful yt-dlp library, a modern fork of youtube-dl, to fetch and download videos directly from YouTube.

🌟 Features
High-Quality Downloads: Combines the best video and audio streams for the highest resolution output.
User Input: Prompts the user to enter a YouTube video link when the script is run.
Auto Package Installation: Automatically installs yt-dlp if it's not already available.
MP4 Output: Merges audio and video streams into a single .mp4 file.
Error Handling: Basic error handling for missing dependencies.
🚀 How to Use
Clone the repository:

bash
Copy
Edit
git clone https://github.com/nihalparakkottu/youtube-video-downloader.git
cd youtube-video-downloader
Run the Python script:

bash
Copy
Edit
python youtube_downloader.py
Enter the YouTube video URL when prompted.

The video will be downloaded in the same directory as the script, with the title of the video as the filename.

🛠️ Requirements
Python 3.7 or above
Internet connection
The script will automatically install yt-dlp if it's not found.

📦 Installation
If you'd like to manually install yt-dlp:

bash
Copy
Edit
pip install yt-dlp
Or you can run the script directly — it'll install the package on its own if necessary.

📚 How it Works
The script:

Prompts the user for a YouTube video URL.
Sets download options for the best video and audio quality.
Uses yt-dlp to fetch and download the video.
Merges the streams into a .mp4 file.
Saves the file with the same name as the YouTube video title.
🧩 Contributing
Feel free to fork the repository, make improvements, and submit a pull request. Suggestions for adding new features (like selecting quality options or batch downloading) are always welcome!

📜 License
This project is licensed under the MIT License — feel free to use and modify it!

