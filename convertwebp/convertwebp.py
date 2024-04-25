from tkinter import Tk, filedialog
from PIL import Image
import os
#suraj gojanur
def convert_to_webp(input_path, output_path):
    for root, dirs, files in os.walk(input_path):
        rel_path = os.path.relpath(root, input_path)
        output_folder = os.path.join(output_path, rel_path)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for file in files:
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_folder, file.rsplit('.', 1)[0] + '.webp')

            try:
                img = Image.open(input_file_path)
                
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    img.save(output_file_path, 'WEBP')
                    print(f"Converted: {input_file_path} to {output_file_path}")
                
                elif file.lower().endswith('.gif'):
                    img.save(output_file_path, 'WEBP', save_all=True, append_images=img.getdata())
                    print(f"Converted: {input_file_path} to {output_file_path}")
            except Exception as e:
                print(f"Error converting {input_file_path}: {e}")

if __name__ == "__main__":
    # Ask for input folder
    root = Tk()
    root.withdraw()
    input_folder = filedialog.askdirectory(title="Select Input Folder")

    # Ask for output folder
    output_folder = filedialog.askdirectory(title="Select Output Folder")

    # Convert images to WebP
    convert_to_webp(input_folder, output_folder)
