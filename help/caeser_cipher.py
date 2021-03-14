plaintext = input()
key = int(input())
ciphertext = ''

for character in plaintext.lower():
    ciphertext += chr((ord(character) - ord('a') + key) % 26 + ord('a')).upper()

print(ciphertext)
