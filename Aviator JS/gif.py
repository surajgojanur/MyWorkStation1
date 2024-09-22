from PIL import Image
import os

def gif_to_frames(gif_path, output_folder):
    # Open the gif image
    gif = Image.open(r"C:\Users\suraj\Downloads\PROt\super_gif.gif")

    
    # Check if output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize frame counter
    frame = 0

    try:
        # Loop through the frames of the gif
        while True:
            # Save each frame as a separate image
            gif.save(f"{output_folder}/frame_{frame}.png", "PNG")
            frame += 1
            gif.seek(frame)  # Go to the next frame
    except EOFError:
        # End of gif frames
        print(f"Conversion complete. {frame} frames saved.")

# Example usage:
gif_path = "your_gif_file.gif"
output_folder = "output_frames"
gif_to_frames(gif_path, output_folder)
