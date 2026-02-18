import os
import json
from PIL import Image
import numpy as np

VIDEO_DIR = 'video'
SIMILARITY_THRESHOLD = 0.9997  # Change this value as needed (1.0 = identical, 0.0 = completely different)
RESIZE_TO = (64, 64)  # Resize images for faster comparison

def image_to_array(filepath):
    with Image.open(filepath) as img:
        img = img.convert('RGB').resize(RESIZE_TO)
        return np.asarray(img, dtype=np.float32) / 255.0

def cosine_similarity(a, b):
    a_flat = a.flatten()
    b_flat = b.flatten()
    dot = np.dot(a_flat, b_flat)
    norm_a = np.linalg.norm(a_flat)
    norm_b = np.linalg.norm(b_flat)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

def main():
    files = [f for f in os.listdir(VIDEO_DIR) if f.lower().endswith('.jpg')]
    arrays = [image_to_array(os.path.join(VIDEO_DIR, f)) for f in files]
    groups = []
    assigned = [False] * len(files)
    for i, arr in enumerate(arrays):
        if assigned[i]:
            continue
        group = [files[i]]
        assigned[i] = True
        for j in range(i+1, len(arrays)):
            if assigned[j]:
                continue
            sim = cosine_similarity(arr, arrays[j])
            if sim >= SIMILARITY_THRESHOLD:
                group.append(files[j])
                assigned[j] = True
        groups.append(group)
    with open('similarity_groups.json', 'w') as f:
        json.dump(groups, f, indent=2)
    print(f"Similarity groups written to similarity_groups.json. {len(groups)} groups found.")

if __name__ == '__main__':
    main()
