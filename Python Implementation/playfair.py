def get_position(a, key_matrix):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == a:
                return i,j

pt = input("Enter the plain text: ")
key = input("Enter the key: ")

key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"

alpha_used = dict()
for i in range(26):
    alpha_used[chr(65+i)] = 0

key_index = 0
key_matrix = list()

for i in range(5):
    temp = list()
    for j in range(5):
        while alpha_used[key[key_index]] == 1:
            key_index += 1
        alpha_used[key[key_index]] = 1
        temp.append(key[key_index])
        key_index += 1
    key_matrix.append(temp)

print("Key Matrix: \n", key_matrix)

if len(pt) % 2 != 0:
    pt += 'Z'

cipher_text = ""
for i in range(0,len(pt),2):
    if pt[i] == 'J':
        pt[i] = 'I'
    x1, y1 = get_position(pt[i], key_matrix)
    x2, y2 = get_position(pt[i+1], key_matrix)
    
    if x1 == x2:
        cipher_text += key_matrix[x1][(y1+1)%5]
        cipher_text += key_matrix[x2][(y2+1)%5] 
    elif y1 == y2:
        cipher_text += key_matrix[(x1+1)%5][y1]
        cipher_text += key_matrix[(x2+1)%5][y2]
    else:
        cipher_text += key_matrix[x1][y2]
        cipher_text += key_matrix[x2][y1]

print("Cipher Text: ", cipher_text) 

plain_text = ""
for i in range(0,len(pt),2):
    x1, y1 = get_position(cipher_text[i], key_matrix)
    x2, y2 = get_position(cipher_text[i+1], key_matrix)
    
    if x1 == x2:
        plain_text += key_matrix[x1][(y1-1)%5]
        plain_text += key_matrix[x2][(y2-1)%5] 
    elif y1 == y2:
        plain_text += key_matrix[(x1-1)%5][y1]
        plain_text += key_matrix[(x2-1)%5][y2]
    else:
        plain_text += key_matrix[x1][y2]
        plain_text += key_matrix[x2][y1]

print("Decrypted_text: ", plain_text)
