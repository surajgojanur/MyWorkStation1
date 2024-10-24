#pip install moviepy

import os
from moviepy.editor import *

# Function to convert MP3 to MP4 with black screen
def mp3_to_mp4_with_black_screen(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.mp3'):
            mp3_path = os.path.join(input_folder, filename)
            mp4_filename = os.path.splitext(filename)[0] + '.mp4'
            mp4_path = os.path.join(output_folder, mp4_filename)

            # Load audio file
            audio = AudioFileClip(mp3_path)

            # Create a black screen video of the same duration as the audio
            video = ColorClip(size=(640, 480), color=(0, 0, 0), duration=audio.duration)

            # Set the audio to the video
            video = video.set_audio(audio)

            # Export the video
            video.write_videofile(mp4_path, codec="libx264", fps=24, audio_codec="aac")

            print(f"Converted {mp3_path} to {mp4_path}")

# Paths to the input folder and output folder
input_folder = 'path/to/your/mp3/folder'
output_folder = 'path/to/save/mp4/files'

# Call the function
mp3_to_mp4_with_black_screen(input_folder, output_folder)
