import sys
from PIL import Image
from PIL.PngImagePlugin import PngInfo


def write_parameters(image_path, text_file_path):
    img = Image.open(image_path)

    with open(text_file_path, "r") as text_file:
        parameters = text_file.read().strip()

    metadata = PngInfo()
    metadata.add_text("parameters", parameters)
    img.save(image_path, pnginfo=metadata)
    print("Parameters written successfully.")


# Example usage
if len(sys.argv) != 3:
    print("Usage: python write_prompt.py (image file path) (text file path)")
    exit(1)

image_path = sys.argv[1]
text_file_path = sys.argv[2]
write_parameters(image_path, text_file_path)
