def encrypt(text, shift):
    result = ""

    # traverse through each character in the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Leave non-alphabetic characters as is
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Example 
text = "Hi this is the orignal message"
shift = 3
encrypted = encrypt(text, shift)
decrypted = decrypt(encrypted, shift)

print("Original text:", text)
print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)
