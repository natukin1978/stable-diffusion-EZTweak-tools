import sys
from PIL import Image


def extract_parameters(image_path):
    img = Image.open(image_path)
    if "parameters" in img.text:
        parameters = img.text["parameters"]
        print(parameters)
    else:
        print("No parameters found in tEXt chunk.", file=sys.stderr)


# Example usage
if len(sys.argv) != 2:
    print("Usage: python extract_parameters.py (image file path)", file=sys.stderr)
    exit(1)

image_path = sys.argv[1]
extract_parameters(image_path)
