from PIL import Image
import sys

def encrypt_decrypt_image(input_path, output_path, key):
    """
    Encrypt or decrypt an image using XOR with the given key on each pixel.
    
    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the processed image.
        key (int): An integer key for XOR operation (0-255).
    """
    try:
        img = Image.open(input_path)
        img = img.convert("RGB")
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Apply XOR with the key on each color channel
            r_enc = r ^ key
            g_enc = g ^ key
            b_enc = b ^ key
            pixels[x, y] = (r_enc, g_enc, b_enc)

    try:
        img.save(output_path)
        print(f"Processed image saved to {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

def main():
    if len(sys.argv) != 5:
        print("Usage: python image_encryption_tool.py <encrypt|decrypt> <input_image> <output_image> <key>")
        print("Example: python image_encryption_tool.py encrypt input.jpg encrypted.png 123")
        sys.exit(1)

    operation = sys.argv[1].lower()
    input_image = sys.argv[2]
    output_image = sys.argv[3]

    try:
        key = int(sys.argv[4])
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Key must be an integer between 0 and 255.")
        sys.exit(1)

    if operation not in ("encrypt", "decrypt"):
        print("Operation must be 'encrypt' or 'decrypt'.")
        sys.exit(1)

    encrypt_decrypt_image(input_image, output_image, key)

if __name__ == "__main__":
    main()

