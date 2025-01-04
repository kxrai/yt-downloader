# YouTube Downloader 🎥🎶

## Overview 📋
This Python script allows you to download YouTube videos or audio files for personal use. It gives you the option to choose between:

1. **Video in 1080p resolution** 🎥
2. **Audio in MP4 format** 🎵

The script uses the `pytube` library for handling YouTube downloads and is designed to run in a Python environment.

---

## How to Use 🛠️

### Step 1: Install Dependencies
Ensure you have Python installed. To verify, run:
```bash
python3 --version
```

Install the required library using `pip`:
```bash
python3 -m pip install pytube
```

### Step 2: Run the Script
Run the script by executing:
```bash
python3 youtube_download_script.py
```

### Step 3: Choose an Option
When prompted, select an option:
- Enter `1` to download the video in **1080p**.
- Enter `2` to download only the **audio** in MP4 format.

Provide the YouTube URL when asked, and the download will begin. 🎉

---

## Features ✨
- Simple and intuitive terminal interface.
- Downloads videos in 1080p resolution.
- Extracts high-quality audio in MP4 format.

---

## Troubleshooting 🐞

### Common Issues
1. **Video Title Retrieval Error**:
   - Update `pytube` to the latest version:
     ```bash
     python3 -m pip install --upgrade pytube
     ```

2. **`pip` or `pytube` Not Found**:
   - Ensure Python and `pip` are installed.
   - Use a virtual environment to isolate dependencies:
     ```bash
     python3 -m venv yt-env
     source yt-env/bin/activate
     python3 -m pip install pytube
     ```

3. **Persistent Issues**:
   - Switch to an alternative library like `yt-dlp`. Replace the script logic accordingly.

---

## License 📝
This script is provided for personal use only. Ensure compliance with YouTube's Terms of Service.

---

Enjoy downloading your favorite content! 🚀
