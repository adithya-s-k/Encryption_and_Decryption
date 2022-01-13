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

