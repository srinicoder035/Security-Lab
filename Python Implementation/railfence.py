pt = input("Enter the plain text: ")
key = int(input("Enter the key: "))

rail_fence = [['#' for i in range(len(pt))] for j in range(key)]

i = 0
row, col = 0, 0
isDown = False
while i < len(pt):
    if row == key-1 or row == 0:
        isDown = not isDown
    rail_fence[row][col] = pt[i]
    if isDown == True:
        row += 1
    else:
        row -= 1
    col += 1
    i += 1

print("Rail Fence:")

for i in range(key):
    for j in range(len(pt)):
        print(rail_fence[i][j] + "\t")
    print("\n")
        
cipher = ""
for i in range(key):
    for j in range(len(pt)):
        if rail_fence[i][j] != '#':
            cipher += rail_fence[i][j]

print("Cipher Text: ", cipher)

row, col = 0, 0
isDown = False
while col < len(cipher):
    if row == key-1 or row == 0:
        isDown = not isDown
    rail_fence[row][col] = '*'
    if isDown == True:
        row += 1
    else:
        row -= 1
    col += 1

index = 0
for i in range(key):
    for j in range(len(pt)):
        if rail_fence[i][j] == '*':
            rail_fence[i][j] = cipher[index]
            index += 1

            
plain_text = ""            
row, col = 0, 0
isDown = False
while col < len(cipher):
    if row == key-1 or row == 0:
        isDown = not isDown
    plain_text += rail_fence[row][col]
    if isDown == True:
        row += 1
    else:
        row -= 1
    col += 1

print("Plain Text: ", plain_text)
