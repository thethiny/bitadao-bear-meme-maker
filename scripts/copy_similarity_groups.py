import os
import json
import shutil

VIDEO_DIR = 'video'
GROUPS_JSON = 'similarity_groups.json'
OUTPUT_DIR = 'similarity_groups'

def main():
    if not os.path.exists(GROUPS_JSON):
        print(f"{GROUPS_JSON} not found.")
        return
    with open(GROUPS_JSON, 'r') as f:
        groups = json.load(f)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for idx, group in enumerate(groups, 1):
        group_dir = os.path.join(OUTPUT_DIR, f'group_{idx:03d}')
        os.makedirs(group_dir, exist_ok=True)
        for filename in group:
            src = os.path.join(VIDEO_DIR, filename)
            dst = os.path.join(group_dir, filename)
            if os.path.exists(src):
                shutil.copy2(src, dst)
    print(f"Copied files into {len(groups)} group folders under '{OUTPUT_DIR}'.")

if __name__ == '__main__':
    main()
