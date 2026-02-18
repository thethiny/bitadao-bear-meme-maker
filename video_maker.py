import os
import cv2
import numpy as np
from moviepy.editor import ImageSequenceClip, AudioFileClip

def get_image_path(image_name, images_dir):
    # Try to find a file with the image_name (any extension)
    for ext in ['jpg', 'jpeg', 'png', 'bmp', 'webp']:
        path = os.path.join(images_dir, f"{image_name}.{ext}")
        if os.path.isfile(path):
            return path
    # If not found, check if it's a folder and use the first image inside
    folder_path = os.path.join(images_dir, image_name)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
                return os.path.join(folder_path, file)
    return None

def read_timeline(timeline_path):
    timeline = []
    with open(timeline_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                timeline.append((parts[0], int(parts[1])))
    return timeline

def main():
    timeline_path = 'timeline.txt'
    images_dir = os.path.join('input', 'images')
    audio_path = os.path.join('input', 'audio.mp3')  # fallback to any ext below
    # Try to find audio with any extension
    if not os.path.isfile(audio_path):
        for ext in ['mp3', 'wav', 'ogg', 'flac']:
            test_path = os.path.join('input', f'audio.{ext}')
            if os.path.isfile(test_path):
                audio_path = test_path
                break
    timeline = read_timeline(timeline_path)
    fps = 30
    frames = []
    for image_name, count in timeline:
        img_path = get_image_path(image_name, images_dir)
        if img_path is None:
            print(f"Warning: Image for '{image_name}' not found.")
            continue
        img = cv2.imread(img_path)
        if img is None:
            print(f"Warning: Failed to load image '{img_path}'.")
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Repeat the image for the number of frames
        frames.extend([img] * count)
    if not frames:
        print("No frames to make video.")
        return
    # Ensure all frames are the same size
    h, w, _ = frames[0].shape
    for i in range(len(frames)):
        if frames[i].shape != (h, w, 3):
            frames[i] = cv2.resize(frames[i], (w, h))
    clip = ImageSequenceClip(frames, fps=fps)
    if os.path.isfile(audio_path):
        audio = AudioFileClip(audio_path)
        clip = clip.set_audio(audio)
    clip.write_videofile('output.mp4', codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    main()
