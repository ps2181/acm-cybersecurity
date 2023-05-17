from Crypto.Cipher import DES
from PIL import Image
import os

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB mode (if it's not already)
    image = image.convert('RGB')

    # Convert the image data to bytes
    image_bytes = image.tobytes()

    # Calculate the required padding size
    block_size = DES.block_size
    padding_size = (block_size - len(image_bytes) % block_size) % block_size

    # Pad the image bytes with zero bytes
    padded_image_bytes = image_bytes + bytes([0] * padding_size)

    # Create a cipher object
    cipher = DES.new(key, DES.MODE_ECB)

    # Encrypt the image
    encrypted_image_bytes = cipher.encrypt(padded_image_bytes)

    # Create a new image from the encrypted bytes
    encrypted_image = Image.frombytes('RGB', image.size, encrypted_image_bytes)

    return encrypted_image

def decrypt_image(encrypted_image, key):
    # Convert the encrypted image to bytes
    encrypted_image_bytes = encrypted_image.tobytes()

    # Create a cipher object for decryption
    cipher = DES.new(key, DES.MODE_ECB)

    # Decrypt the image
    decrypted_image_bytes = cipher.decrypt(encrypted_image_bytes)

    # Remove the zero padding bytes from the decrypted bytes
    unpadded_image_bytes = decrypted_image_bytes.rstrip(b'\x00')

    # Create a new image from the decrypted bytes
    decrypted_image = Image.frombytes('RGB', encrypted_image.size, unpadded_image_bytes)

    return decrypted_image

# Example usage
image_path = r'D:\file_encrypt_decrypt\1.jpg'  
key = b'\x91\x1fV#\x11\x86\x7f\x8f'  

try:
    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)
    encrypted_image.save(r'D:\file_encrypt_decrypt\encrypt.png')

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    decrypted_image.save(r'D:\file_encrypt_decrypt\decrypt.png')

    decrypted_image.show()  # Display the decrypted image

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Error occurred: {str(e)}")
