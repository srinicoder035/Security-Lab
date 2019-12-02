def to_binary(val):
    b = bin(val)
    b = b[2:len(b)-2]
    return b

def get_binary(text):
    binary_list = list()
    for i in text:
        ascii = ord(i)
        ascii_bin = to_binary(ascii)
        ascii_bin = "0"*(8-len(ascii_bin)) + ascii_bin
        for bit in ascii_bin:
            binary_list.append(bit)
    return binary_list

def padding(text):
    bit_list = get_binary(text)
    rem = len(bit_list)%512
    pad_len = 448 - rem
    padding = [0] * (pad_len-1)
    padding = [1] + padding
    padded_list = bit_list + padding
    rem =   len(bit_list) % (2**64)
    length_pad = to_binary(rem)
    length_pad = "0" * (64-len(length_pad)) + length_pad
    for bit in length_pad:
        padded_list.append(bit)
    return padded_list
    
def circular_shift(n,b):
    s = bin(n)
    s = s[2:]
    b = b%len(s)
    s = s[b:len(s)] + s[0:b]
    return int(s,2)    

def f(x,y,z,i):
    if i < 20:
        return (x & y)|(~y & z)
    elif i < 40:
        return x ^ y ^ z
    elif i < 60:
        return (x & y)|(y & z)|(x & z)
    elif i < 80:
        return x ^ y ^ z

def k(i):
    s1 = 2**10 + 100
    s2 = 2**9 + 89
    s3 = 2**4 + 3789
    s4 = 2**10 + 900
    
    if i < 20:
        return s1
    elif i < 40:
        return s2
    elif i < 60:
        return s3
    elif i < 80:
        return s4
        
def hexa(val):
    h = hex(val)
    return h[2:len(h)-2]

def sha1(text):
    l = padding(text)
    h1 = 2**8+98
    h2 = 2**7+76
    h3 = 2**22+332
    h4 = 2**6+5
    h5 = 2**7+21
    words=[]
    i = 0
    while i < len(l):
        words.append(l[i:i+512])
        i+=512
    for word in words:
        w=[]
        i=0
        while i<len(word):
            s=""
            for c in word[i:i+32]:
                s+=str(c)
            w.append(int(s,2))
            i+=32
        for i in range(16,80):
            val = w[i-3]^w[i-8]^w[i-14]^w[i-16]
            val = circular_shift(val,1)
            w.append(val)
        a=h1
        b=h2
        c=h3
        d=h4
        e=h5
        for t in range(0,80):
            temp = circular_shift(a,5)+f(b,c,d,i)+w[i]+k(t)
            e = d
            d = c
            c = circular_shift(b,30)
            b = a
            a = temp
        h1 = h1+a
        h2 = h2+b
        h3 = h3+c
        h4 = h4+d
        h5 = h5+e
    return hexa(h1)+hexa(h2)+hexa(h3)+hexa(h4)+hexa(h5)
            

if __name__ == "__main__":
    text = input("Enter the string to be hashed: ")
    hashed_text = sha1(text)
    print("Hashed text: ", hashed_text)
