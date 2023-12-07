import os
import cv2
import tkinter as tk
from tkinter import filedialog

def convert_to_video(image_folder, fps):
    # Allow both JPG and PNG extensions
    valid_extensions = (".jpg", ".jpeg", ".png")
    images = [img for img in sorted(os.listdir(image_folder)) if img.lower().endswith(valid_extensions)]

    if not images:
        print("No valid images found in the specified folder. Exiting.")
        return

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Set the output video file in the same folder as the images
    output_video = os.path.join(image_folder, "output_video.mp4")

    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)
        video.write(frame)

    cv2.destroyAllWindows()
    video.release()

def main():
    root = tk.Tk()
    root.withdraw()

    # Ask for the image folder using a dialog box
    image_folder = filedialog.askdirectory(title="Select Image Folder")

    if not image_folder:
        print("Image folder not selected. Exiting.")
        return

    # Ask for the desired FPS
    fps_option = input("Enter the desired FPS (30 or 60): ")
    try:
        fps = int(fps_option)
        if fps not in [30, 60]:
            raise ValueError("Invalid FPS. Please enter 30 or 60.")
    except ValueError as e:
        print(e)
        return

    # Convert images to video
    convert_to_video(image_folder, fps)

    print("Video successfully created in the same folder as input images.")

if __name__ == "__main__":
    main()
