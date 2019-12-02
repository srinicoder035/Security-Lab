import math
import re

def formatText(text):
    text = text.upper()
    text = re.sub(" ","",text)
    return text

def isPrime(x):
    if x == 2:
        return True
    else:
        for number in range(3,x):
            if x % number == 0 or x % 2 == 0:
                return False
        return True


def gcd(a,b):
    while(b):
        a , b = b , a % b
    return a

def getInput():
    state = False
    while state == False:
        print("Enter two prime numbers ")
        in1 = int(input())
        in2 = int(input())
        if isPrime(in1) == True and isPrime(in2) == True:
            state = True
            return in1 , in2
        if state == False:
            print("Enter Valid Inputs")

def getPublicKey():
    a,b = getInput()
    return a * b

def phi(n):
    result = 1
    for i in range(2,n):
        if gcd(i,n) == 1:
            result+=1
    return result

def getPublicKey2(n):
    totient = phi(n)
    i = n - 1
    while i > 0:
        if gcd(i,totient) == 1:
            return i
        i -= 1
    raise "Co prime of the number not found"

def toCipher(m , e, n):
    return ((ord(m) - 65) ** e) % n

def encrypt(text, key):
    text = formatText(text)
    e, n = key[0],key[1]
    cipherText = []
    for i in text:
        cipherText.append(toCipher(i,e,n))
    return cipherText

def inverseMod(a, b):
    for i in range(1,b):
        if (a*i)%b == 1:
            return i
    raise "Inverse not found"

def findD(e,n):
    totient = phi(n)
    return inverseMod(e,totient)

def toText(val, d, n):
    return chr( 65 + ((val ** d) % n))

def decrypt(cipher,key):
    text = ""
    e, n = key[0],key[1]
    d = findD(e, n)
    for i in cipher:
        text+= toText(i,d,n)
    return text
    
text = input("Enter the text\n")
n = getPublicKey()
e = getPublicKey2(n)
key = (e,n)
cipher = encrypt(text,key)
print(cipher)
print(decrypt(cipher,key))