from numpy import matrix
import numpy

plain_text = input("Enter the plaintext: ")
key = input("Enter the key(nxn size): ")

key_matrix = list()
n = len(plain_text)

for i in range(n):
    row = list()
    for j in range(n):
        row.append(ord(key[i*n+j])%65)
    key_matrix.append(row)

pt_vector = list()
for i in range(n):
    pt_vector.append(ord(plain_text[i])%65)

cipher_vector = list()
for i in range(n):
    temp = 0
    for j in range(n):    
        temp += round(key_matrix[i][j] * pt_vector[j])
    temp %= 26
    cipher_vector.append(temp)

cipher_text = ""
for i in range(n):
    cipher_text += str(chr(cipher_vector[i] + 65))
    
print("Cipher Text: ", cipher_text)

key_numpy = matrix(key_matrix)
key_numpy = key_numpy.I
inverse_matrix = key_numpy.tolist()
print("inverse Matrix\n", inverse_matrix)

plaintext_vect = list()
for i in range(n):
    temp = 0
    for j in range(n):    
        temp += inverse_matrix[j][i] * cipher_vector[j]
    temp = int(temp)
    temp %= 26
    plaintext_vect.append(temp)

print(plaintext_vect)
pt_text = ""
for i in range(n):
    pt_text += str(chr(pt_vector[i] + 65))
    
print("Decrypted Text: ", pt_text)
