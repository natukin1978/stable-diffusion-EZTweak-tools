# Stable Diffusion EZTweak tools

Tools to easily address the needs of Stable Diffusion.

EZ: Easy
Tweak: Fine-tuning

## Requirements

* Pillow

## Installation

Go to project directory and install the module.

```
python -m pip install -r requirements.txt
```

## copy_prompt.py

`copy_prompt.py` is a tool that reads prompt information from image files in the specified folder for Stable Diffusion and performs a copy of the prompt information to image files in a different folder.

When you edit images in graphic editing software, sometimes the prompt information might be lost. While some AI image sharing platforms automatically extract and display the prompts used, they may not include prompts if the image was edited to remove them.

This tool is designed for scenarios where you want to preserve the prompt information from the original image by copying it to a separate file.

### Usage

```
python copy_prompt.py (from_folder) (to_folder)
```

(from_folder): Path to the source folder for copying

(to_folder): Path to the target folder for copying

Specify the source and target folders as command-line arguments.

The tool will seek user confirmation and proceed with copying if approved.

## move_file_model.py

`move_file_model.py`is a tool that reads prompt information from image files in the specified folder for Stable Diffusion, extracts the model name, and moves the image files to corresponding subfolders.

By default, the model names are represented as hash values. If you want to output human-readable model names, please modify the settings in Stable Diffusion (AUTOMATIC1111).

### Usage

```
python move_file_model.py (folder_path)
```

(folder_path): Path to the folder for processing

Specify the target folder as a command-line argument.

## Contributing

If you would like to contribute to Stable Diffusion EZTweak tools, please open an issue to discuss your ideas or submit a pull request.

## Author

ナツキソ

- Twitter: [@natukin1978iai](https://twitter.com/natukin1978iai)
- Mastodon: [@natukin1978iai@pawoo.net](https://pawoo.net/web/accounts/2199670)
- GitHub: [@natukin1978](https://github.com/natukin1978)
- Mail: natukin1978iai@gmail.com

## License

Stable Diffusion EZTweak tools is released under the [MIT License](https://opensource.org/licenses/MIT).
