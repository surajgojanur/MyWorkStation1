import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def get_folder_path(title):
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    folder_path = filedialog.askdirectory(title=title)
    return folder_path

def mute_audio_ffmpeg(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List of valid video file extensions
    valid_extensions = ('.mp4', '.avi', '.mkv', '.mov', '.wmv')

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            # Define the full path of the input video
            input_path = os.path.join(input_folder, filename)

            # Define the full path for the output video
            output_path = os.path.join(output_folder, filename)

            # Use FFmpeg to mute the audio
            cmd = [
                'ffmpeg',
                '-i', input_path,
                '-an',  # Disable audio
                '-c:v', 'copy',  # Copy video codec
                output_path
            ]

            subprocess.run(cmd)

if __name__ == "__main__":
    input_folder = get_folder_path(title="Select Input Folder")
    if not input_folder:
        print("No input folder selected. Exiting.")
    else:
        output_folder = get_folder_path(title="Select Output Folder")
        if not output_folder:
            print("No output folder selected. Exiting.")
        else:
            mute_audio_ffmpeg(input_folder, output_folder)
