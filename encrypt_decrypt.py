from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from PIL import Image

#generating a random key
key = b'\x91\x1fV#\x11\x86\x7f\x8f\xfa@\x85\x9a\x15\x0e\xd6Y1kI\xfe\xdc\xcf\xea\xe1p\x01\x12\x08\x9e\xf9\x91'

original_image_path=""

#opening the file in bytes
with open(original_image_path,'rb') as f:
    original_image_bytes = f.read()

#padding the bytes to 16 according to AES algo
padded_image_bytes=pad(original_image_bytes,AES.block_size)

#creating a cipher object
cipher = AES.new(key,AES.MODE_ECB)

#encrypt the image
encrypted_image_bytes = cipher.encrypt(padded_image_bytes)

with open('','wb') as f:
    f.write(encrypted_image_bytes)

#decrypting the image
decrypted_image_bytes = cipher.decrypt(encrypted_image_bytes)

#removing the padded bits
unpadded_image_bytes = unpad(decrypted_image_bytes, AES.block_size)

#decrypting the image
decrypted_image = Image.frombytes('RGB',(512,512),unpadded_image_bytes)

decrypted_image.save('')
