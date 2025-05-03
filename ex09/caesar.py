import sys

def check_language(text):
    for char in text:
        if char.isalpha() and not ('a' <= char.lower() <= 'z'):
            raise Exception("The script does not support your language yet.")

def caesar_shift(char, shift):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return char

def caesar_cipher(text, shift, mode):
    check_language(text)
    if mode == 'decode':
        shift = -shift
    return ''.join(caesar_shift(c, shift) for c in text)

def main():
    if len(sys.argv) != 4:
        raise Exception("Incorrect number of arguments")
    
    mode = sys.argv[1].lower()
    text = sys.argv[2]
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer")

    if mode not in ['encode', 'decode']:
        raise Exception("First argument must be 'encode' or 'decode'")

    result = caesar_cipher(text, shift, mode)
    print(result)

if __name__ == "__main__":
    main()
