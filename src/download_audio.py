import yt_dlp as youtube_dl
import os

def download_audio(youtube_url, output_path):
    if os.path.exists(output_path + '.mp3'):
        os.remove(output_path + '.mp3')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    if os.path.exists(output_path + '.mp3'):
        os.rename(output_path + '.mp3', output_path) 
