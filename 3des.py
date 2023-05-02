from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from PIL import Image

def encrypt_image(image_file, key):
    with open(image_file, 'rb') as f:
        image_bytes = f.read()
    iv = b'00000000'
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    encrypted_image = cipher.encrypt(pad(image_bytes, DES3.block_size))
    with open('encrypted_image.png', 'wb') as f:
        f.write(encrypted_image)
    return encrypted_image

def decrypt_image(image_file, key):
    with open(image_file, 'rb') as f:
        encrypted_image = f.read()
    iv = b'00000000'
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_image = unpad(cipher.decrypt(encrypted_image), DES3.block_size)
    with open('decrypted_image.png', 'wb') as f:
        f.write(decrypted_image)
    return decrypted_image

# Example usage
key = b'1234567' # 16 or 24 bytes
image_file = 'original_image.png'
encrypted_image = encrypt_image(image_file, key)
decrypted_image = decrypt_image('decrypted_image.png', key)

# Display images
original_image = Image.open(image_file)
original_image.show()
#encrypted image file link in open
encrypted_image = Image.open('')
encrypted_image.show()
#decrytped image file link in open
decrypted_image = Image.open('')
decrypted_image.show()
