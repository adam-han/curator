import yt_dlp
import tkinter as tk
from tkinter import filedialog

def Download_Video(url, save_path):
    """
    Download_Video(): downloads the video in mp4 and 1080p quality
    - url: the url of the video
    - save_path: where to save the video to
    """
    ydl_opts = {
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'noplaylist': True,
        # add a progress hook
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])




