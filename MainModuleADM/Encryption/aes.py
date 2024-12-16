# from Crypto.Cipher import AES
from Cryptodome.Cipher import AES
import sys
import base64
import os

# AES 'pad' byte array to multiple of BLOCK_SIZE bytes
__key = 'MGP@ssW0rd30182933123213'

def pad(byte_array):
    block_size = 16
    pad_len = block_size - len(byte_array) % block_size
    return byte_array + (bytes([pad_len]) * pad_len)


# Remove padding at end of byte array
def unpad(byte_array):
    last_byte = byte_array[-1]
    return byte_array[0:-last_byte]


def encrypt(key, message) -> str:
    """
    Melakukan Enkripsi Plain String dengan metode AES128-CBC menggunakan
    random vi, mengembalikan nilai cipher dalam bentuk base64 encoded string

    All arguments must be of equal length.
    :param key: secret key untuk enkripsi dengan panjang 16 (*AES-128*), 24 (*AES-192*), or 32 (*AES-256*) bytes long.
    :param message: secret message yang akan di dekripsi
    :return: base64 encoded encrypted String
    """

    byte_array = message.encode("UTF-8")

    padded = pad(byte_array)

    # generate a random iv and prepend that to the encrypted result.
    # The recipient then needs to unpack the iv and use it.
    iv = os.urandom(AES.block_size)
    cipher = AES.new(key.encode("UTF-8"), AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    # Note we PREPEND the unencrypted iv to the encrypted message
    return base64.b64encode(iv + encrypted).decode("UTF-8")


def decrypt(key, message) -> str:
    """
    Melakukan Dekripsi Cipher String dengan metode AES128-CBC,
    mengembalikan nilai plain dalam bentuk string

    All arguments must be of equal length.
    :param key: secret key untuk enkripsi dengan panjang 16 (*AES-128*), 24 (*AES-192*), or 32 (*AES-256*) bytes long.
    :param message: secret message yang akan di dekripsi
    :return: string plain secret message setelah di dekripsi
    """

    byte_array = base64.b64decode(message)

    iv = byte_array[0:16]  # extract the 16-byte initialization vector

    messagebytes = byte_array[16:]  # encrypted message is the bit after the iv

    cipher = AES.new(key.encode("UTF-8"), AES.MODE_CBC, iv)

    decrypted_padded = cipher.decrypt(messagebytes)

    decrypted = unpad(decrypted_padded)

    return decrypted.decode("UTF-8")
