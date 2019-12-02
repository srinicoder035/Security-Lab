pt = input("Enter the plain text: ")
key = int(input("Enter the key: "))

cipher_text = ""
for i in range(len(pt)):
    if pt[i] >= 'A' and pt[i] <='Z':
        cipher_text += chr(((ord(pt[i]) - 65) + key)%26 + 65)
    elif pt[i] >= 'a' and pt[i] <='z':
        cipher_text += chr(((ord(pt[i]) - 97) + key)%26 + 97)
    else: 
        cipher_text += chr(ord(pt[i]) + key)

print("Cipher text: ", cipher_text)

plain_text = ""
for i in range(len(pt)):
    if cipher_text[i] >= 'A' and cipher_text[i] <='Z':
        plain_text += chr(((ord(cipher_text[i]) - 65) - key)%26 + 65)
    elif cipher_text[i] >= 'a' and cipher_text[i] <='z':
        plain_text += chr(((ord(cipher_text[i]) - 97) - key)%26 + 97)
    else: 
        plain_text += chr(ord(cipher_text[i]) - key)

print("Decrypted text: ", plain_text)
