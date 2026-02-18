# Bitadao Meme Maker

## Overview

This project generates a video from a sequence of images and an audio track, using a timeline specification. The main script is [`video_maker.py`](./video_maker.py), and the timeline is defined in [`timeline.txt`](./timeline.txt).

## How It Works

- [`timeline.txt`](./timeline.txt) specifies the order and duration (in frames) for each image or group.
- [`video_maker.py`](./video_maker.py) reads the timeline, loads images from [`input/images/`](./input/images/), and combines them into a video.
- The script attempts to find an audio file in `input/audio.mp3` (or other supported formats) and adds it to the video.
- The final video is saved as `output.mp4`.

## Usage

1. Place your images in the [`input/images/`](./input/images/) directory.
2. Place your audio file in the [`input/`](./input/) directory (named `audio.mp3`, `audio.wav`, etc.).
3. Edit [`timeline.txt`](./timeline.txt) to specify the sequence and duration for each image: (file provided is already good)
   ```
   image_name frame_count
   ```
   Example:
   ```
   14_close_up 2
   4 1
   12 1
   ```
4. Run the script:
   ```
   python video_maker.py
   ```
5. The output video will be saved as `output.mp4`.

## Requirements

- Python 3
- Packages: `opencv-python`, `moviepy`, `numpy`

## Example Timeline

Reference: [`timeline.txt`](./timeline.txt) (already set up for use)

## Script Details

- The script supports image formats: jpg, jpeg, png, bmp, webp.
- If an image name refers to a folder, the first image inside is used.
- All frames are resized to match the first image's size.
- Warnings are printed if images are missing or fail to load.
