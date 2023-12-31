import os
import sys
from PIL import Image
from PIL.PngImagePlugin import PngInfo


def compare_resolution(image1, image2):
    return image1.size == image2.size


def copy_SD_prompt(from_folder, to_folder):
    from_files = os.listdir(from_folder)
    to_files = os.listdir(to_folder)

    if len(from_files) != len(to_files):
        print("Error: Number of files in 'from' and 'to' folders is not the same.")
        return

    print(f"From Folder Contents: {from_files}")
    print(f"To Folder Contents: {to_files}")

    for from_filename, to_filename in zip(from_files, to_files):
        from_path = os.path.join(from_folder, from_filename)
        to_path = os.path.join(to_folder, to_filename)

        from_img = Image.open(from_path)
        to_img = Image.open(to_path)

        if "parameters" in from_img.text:
            if compare_resolution(from_img, to_img):
                print(f"Copying SD parameters from {from_path} to {to_path}")
                metadata = PngInfo()
                metadata.add_text("parameters", from_img.text["parameters"])
                to_img.save(to_path, pnginfo=metadata)
                print(f"SD parameters copied successfully.")
            else:
                print(f"Resolution mismatch for {from_path} and {to_path}. Stopping.")
                break


def main():
    if len(sys.argv) != 3:
        print("Usage: python copy_SD_prompt.py (from folder) (to folder)")
        exit(1)

    from_folder = sys.argv[1]
    to_folder = sys.argv[2]

    user_confirmation = input(
        f"Copy SD parameters\n"
        f"from folder: {from_folder}\n"
        f"to folder:   {to_folder}\n"
        f"Proceed? (y/n): "
    )

    if user_confirmation.lower() == "y":
        copy_SD_prompt(from_folder, to_folder)
    else:
        print("Operation canceled.")


if __name__ == "__main__":
    main()
