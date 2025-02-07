import cv2
import numpy as np
from PIL import Image
import argparse
import os

def extract_frames(video_path, num_frames):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if total_frames == 0:
        print("Error: Could not read video or video is empty.")
        return []
    
    frame_indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)
    frames = []
    
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    cap.release()
    return frames

def create_collage(frames, output_path, cols=5):
    if not frames:
        print("No frames extracted, collage cannot be created.")
        return
    
    num_frames = len(frames)
    rows = (num_frames + cols - 1) // cols  # Calculate required rows
    
    frame_height, frame_width, _ = frames[0].shape
    collage_width = cols * frame_width
    collage_height = rows * frame_height
    
    collage = Image.new('RGB', (collage_width, collage_height))
    
    for i, frame in enumerate(frames):
        img = Image.fromarray(frame)
        x_offset = (i % cols) * frame_width
        y_offset = (i // cols) * frame_height
        collage.paste(img, (x_offset, y_offset))
    
    collage.save(output_path)
    print(f"Collage saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Create a collage from video frames.')
    parser.add_argument('video_path', type=str, help='Path to the video file')
    parser.add_argument('num_frames', type=int, help='Number of frames to extract')
    parser.add_argument('output_path', type=str, help='Path to save the collage PNG file')
    args = parser.parse_args()
    
    frames = extract_frames(args.video_path, args.num_frames)
    create_collage(frames, args.output_path)

if __name__ == "__main__":
    main()

