def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Katta harflarni shifrlash
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Kichik harflarni shifrlash
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Sinab ko'rish
message = "HELLO CYBERSECURITY"
secret_key = 3
encrypted = caesar_cipher(message, secret_key)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
