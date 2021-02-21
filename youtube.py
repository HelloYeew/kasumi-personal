import pytube
from pytube import YouTube
from pathlib import Path
import time
import urllib.request
import os
import wget

def fetch_data(url):
    print("Start fetching data...")
    clip = YouTube(url)
    for i in tqdm(range(1), desc="Fetching data...", ascii=False, ncols=100):
        clip.prefetch()
    for j in tqdm(range(10), desc="Printing...", ascii=True, ncols=100):
        time.sleep(0.15)
    print(f"Title : {clip.title}")
    clip_min = float(clip.length / 60)
    print(f"Length : {clip.length} seconds ({clip_min} minutes)")
    print(f"Views : {clip.views}")
    print(f"Author : {clip.author}")
    print(f"Rating : {clip.rating}")
    print(f"Thumbnail URL : {clip.thumbnail_url}")
    print(f"Video ID : {pytube.extract.video_id(url)}")
    if len(clip.caption_tracks) == 0:
        print("Available Captions : No caption available")
    else:
        print(f"Available Captions : {len(clip.caption_tracks)} languages include")
        for i in range(len(clip.caption_tracks)):
            print(f"{i+1}.{clip.caption_tracks[i]}")
    print(f"Streams Availability : {len(clip.streams)} streams include")
    for i in range(len(clip.streams)):
        print(f"{i + 1}.{clip.streams[i]}")
    print(f"Video Description :")
    print(clip.description)
    print()
    print("Complete!")
    print()


def download_thumbnail(url):
    print("Fetching data...")
    clip = YouTube(url)
    for i in tqdm(range(100),
                  desc="Start downloading thumbnail...",
                  ascii=False, ncols=100):
        time.sleep(0.0001)
    urllib.request.urlretrieve(clip.thumbnail_url, f"{os.getcwd()}/thumbnail.jpg")
    print("Download complete!")
    print(f"File directory : {os.getcwd()}/thumbnail.jpg")
    os.system(f"open {os.getcwd()}/thumbnail.jpg")
    print()

def download_mp4(url):
    print("Fetching data...")
    yt_url = url
    yt_obj = YouTube(yt_url)
    # fetch resolution
    print("Available Streams")
    for stream in yt_obj.streams:
        print(stream)
    print()
    # filter data
    print("Filter data")
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    for mp4_filter in filters:
        print(mp4_filter)
    print()
    # Download video
    for i in tqdm(range(1), desc="Downloading video...", ascii=False, ncols=100):
        filters.get_highest_resolution().download()
    print("Download complete!")
    print(f"File directory : {os.getcwd()}/{yt_obj.title}.mp4")
    print(f"File Size : {Path(f'{os.getcwd()}/{yt_obj.title}.mp4').stat().st_size} bytes")
    os.system(f"open '{os.getcwd()}/{yt_obj.title}.mp4'")
    print()

