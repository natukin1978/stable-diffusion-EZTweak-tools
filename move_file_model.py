import os
import sys
import shutil
from PIL import Image


def extract_model_name(text):
    start = text.find("Model:")
    if start != -1:
        end = text.find(",", start)
        if end != -1:
            model_name = text[start + len("Model:") : end].strip()
            return model_name
    return None


def process_images(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            img = Image.open(file_path)
            if "parameters" in img.text:
                model_name = extract_model_name(img.text["parameters"])
                if model_name:
                    target_folder = os.path.join(folder_path, model_name)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved {filename} to {target_folder}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python move_file_model.py (folder path)")
        exit(1)

    folder_path = sys.argv[1]
    process_images(folder_path)


if __name__ == "__main__":
    main()
