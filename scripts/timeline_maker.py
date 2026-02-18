import os

def make_timeline(similarity_groups_dir, output_file):
    # Get all group folders and sort them for consistent order
    group_folders = [f for f in os.listdir(similarity_groups_dir) if os.path.isdir(os.path.join(similarity_groups_dir, f))]
    
    # Map frame to group
    frame_to_group = {}
    for group in group_folders:
        group_path = os.path.join(similarity_groups_dir, group)
        for img in os.listdir(group_path):
            if img.endswith('.jpg'):
                frame_to_group[img] = group

    # Build timeline by frame order
    frames = sorted(frame_to_group.keys())
    timeline = []
    prev_group = None
    count = 0
    for frame in frames:
        group = frame_to_group[frame]
        if group == prev_group:
            count += 1
        else:
            if prev_group is not None:
                timeline.append((prev_group, count))
            prev_group = group
            count = 1
    if prev_group is not None:
        timeline.append((prev_group, count))

    # Write to file
    with open(output_file, 'w') as f:
        for group, count in timeline:
            f.write(f"{group} {count}\n")

if __name__ == "__main__":
    make_timeline("similarity_groups", "timeline.txt")
