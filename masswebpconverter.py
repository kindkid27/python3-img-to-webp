import os
from PIL import Image

def convert_images_to_webp(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    supported_formats = {"jpeg", "jpg", "png", "bmp", "tiff", "webp"}  # Gifs are not supported sadly :<

    # Walk through all subdirectories and files in the input directory
    for root, _, files in os.walk(input_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                try:
                    with Image.open(file_path) as img:
                        file_extension = filename.split(".")[-1].lower()
                        if file_extension in supported_formats:
                            # Create a relative path for the output based on the subdirectory structure
                            relative_path = os.path.relpath(root, input_dir)
                            output_subdir = os.path.join(output_dir, relative_path)
                            if not os.path.exists(output_subdir):
                                os.makedirs(output_subdir)

                            # Define output filename and path
                            output_filename = os.path.splitext(filename)[0] + ".webp"
                            output_path = os.path.join(output_subdir, output_filename)

                            # Save the image as webp
                            img.save(output_path, "webp")
                            print(f"Converted: {file_path} -> {output_path}")
                        else:
                            print(f"Unsupported format, skipping: {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_directory = "./input"  # where the images come in
    output_directory = "./output"  # where the images come out

    print(f"Formatting all the images in '{input_directory}' to webp, and exporting to '{output_directory}'.")

    if not os.path.exists(input_directory):
        print(f"Input directory '{input_directory}' does not exist. Please create it and add images.")
    else:
        convert_images_to_webp(input_directory, output_directory)

    print(f"Thank you for using this quick little script!")
