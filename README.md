# Simple Image Encryption Tool

This is a simple image encryption and decryption tool implemented in Python. The tool uses pixel manipulation by applying an XOR operation on each pixel's RGB values with a user-provided key. Because XOR is its own inverse, the same key can be used to both encrypt and decrypt images.

## Features

- Encrypt any image by XOR-ing pixel values with a key (0-255)
- Decrypt images encrypted by this tool using the same key
- Simple command-line interface
- Supports most common image formats (JPEG, PNG, BMP, etc.)

## Requirements

- Python 3.x
- Pillow (PIL) library

Install the Pillow library with pip if you don't have it:

```bash
pip install Pillow
