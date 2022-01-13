# import other necessery modules
import random
# modules for encryption and decryption
import base64
import onetimepad
import pyDes

def reverseEncrypt(inputMessage):
    strInput = str(inputMessage)
    reversStr = strInput[::-1]
    return str(reversStr)

def reverseDecrypt(inputMessage):
    strInput = str(inputMessage)
    reversStr = strInput[::-1]
    return str(reversStr)

def caeserCipherEncrypt(string, shift):
    cipher = ''
    for char in string:
        if char==' ':
            cipher=cipher+' '
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return str(cipher)

def caeserCipherDecrypt(string, shift):
    cipher = ''
    shift = -shift
    for char in string:
        if char==' ':
            cipher=cipher+' '
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return str(cipher)


def base64Encryption(msg):
    sample_string = (msg)
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return str(base64_string)

def base64Decryption(decode_entry):
    base64_string = decode_entry
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")    
    return sample_string
