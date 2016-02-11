import base64
import sys
import getpass

#RC4
def rc4_crypt( data , key ):
    S = range(256)
    j = 0
    out = []
    #Algoritmo pseudo aleatorio
    for i in range(256):
        j = (j + S[i] + ord( key[i % len(key)] )) % 256
        S[i] , S[j] = S[j] , S[i]
    #Algoritmo de 1 clave
    i = j = 0
    for char in data:
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))
        
    return ''.join(out)


def encrypt( data , key , encode = base64.b64encode ):
    data = rc4_crypt(data , key)
    if encode:
        data = encode(data)
    return data

def decrypt(data , key, decode = base64.b64decode ):
    if decode:
        data = decode(data)
    return rc4_crypt(data , key)
    
p = getpass.getpass()
print 'Has introducido:', p

codif= rc4_crypt('hola' , p)
codif= base64.b64encode(codif)
print(codif)

decodif = base64.b64decode('SWRsbw==')
decodif = rc4_crypt(decodif,p)
print(decodif)