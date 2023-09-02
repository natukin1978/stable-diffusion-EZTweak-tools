import sys
import argparse
from PIL import Image
from PIL.PngImagePlugin import PngInfo


def replace_parameters(parameters, replace_from, replace_to):
    # 文字列の置換を行います
    parameters = parameters.replace(replace_from, replace_to)
    return parameters


def write_parameters(image_path, text_file_path, replace_from=None, replace_to=None):
    img = Image.open(image_path)

    with open(text_file_path, "r") as text_file:
        parameters = text_file.read().strip()

    if not parameters:
        return
    # オプションの置換を行います
    if replace_from and replace_to:
        parameters = replace_parameters(parameters, replace_from, replace_to)

    metadata = PngInfo()
    metadata.add_text("parameters", parameters)
    img.save(image_path, pnginfo=metadata)
    print("Parameters written successfully.")


def main():
    parser = argparse.ArgumentParser(description="Write parameters to a PNG image.")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument(
        "text_file_path", help="Path to the text file containing parameters"
    )
    parser.add_argument("--replace-from", help="Text to replace in the parameters")
    parser.add_argument("--replace-to", help="Replacement text for the parameters")

    args = parser.parse_args()
    write_parameters(
        args.image_path, args.text_file_path, args.replace_from, args.replace_to
    )


if __name__ == "__main__":
    main()
