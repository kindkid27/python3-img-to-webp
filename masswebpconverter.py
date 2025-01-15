import os
from PIL import Image

def convert_images_to_webp(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    supported_formats = {"jpeg", "jpg", "png", "bmp", "tiff"} # Gifs are not supporterd sadly :<

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    file_extension = filename.split(".")[-1].lower()
                    if file_extension in supported_formats:
                        output_filename = os.path.splitext(filename)[0] + ".webp"
                        output_path = os.path.join(output_dir, output_filename)

                        img.save(output_path, "webp")
                        print(f"Converted: {filename} -> {output_filename}")
                    else:
                        print(f"Unsupported format, skipping: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_directory = "./input"  # where the images come in
    output_directory = "./output"  # where the images com out

    print(f"Formatting all the images in '{input_directory}' to webp, and exporting to '{output_directory}'.")

    if not os.path.exists(input_directory):
        print(f"Input directory '{input_directory}' does not exist. Please create it and add images.")
    else:
        convert_images_to_webp(input_directory, output_directory)

