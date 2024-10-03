import os
import subprocess
import sys
from PIL import Image

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    from PIL import Image

def convert_images_to_webp(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.jfif')):
            file_path = os.path.join(input_dir, filename)
            img = Image.open(file_path)

            webp_filename = os.path.splitext(filename)[0] + '.webp'
            webp_file_path = os.path.join(output_dir, webp_filename)

            img.save(webp_file_path, 'WEBP')
            print(f'Converted {filename} to {webp_filename}')

def handle_duplicates(output_dir):
    duplicates = []

    for filename in os.listdir(output_dir):
        if filename.lower().endswith('.webp') and 's' in filename.lower():
            duplicates.append(filename)

    if duplicates:
        print("The following duplicate files will be deleted:")
        for dup in duplicates:
            print(f"- {dup}")

        response = input("Do you want to delete all 's' duplicates? (yes/no): ")
        if response.lower() == 'yes':
            for dup in duplicates:
                os.remove(os.path.join(output_dir, dup))
                print(f'Deleted duplicate file: {dup}')

def main():
    input_directory = input("Please enter the input directory path: ")
    current_directory = os.getcwd()
    output_directory = os.path.join(current_directory, 'Converted')
    
    convert_images_to_webp(input_directory, output_directory)
    handle_duplicates(output_directory)

if __name__ == "__main__":
    main()
