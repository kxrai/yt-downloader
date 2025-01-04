import os
import subprocess

def download_youtube_video():
    print("Choose an option:")
    print("1. Download Video in 1080p")
    print("2. Download Audio in MP4 format")

    choice = input("Enter the option number (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return

    url = input("Enter the YouTube video URL: ")

    try:
        if choice == '1':
            subprocess.run(["yt-dlp", "-f", "bestvideo[height<=1080]+bestaudio/best", url])
        elif choice == '2':
            subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", url])

        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
