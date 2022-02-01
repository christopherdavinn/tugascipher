import re

def textCleaning(text):
    text = text.upper()
    text = re.sub(r'\s*\d+\s*', '',text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace(' ', '')
    return text

def postProcess(text):
    text = [text[i:i+5] for i in range(0, len(text), 5)]
    text = ' '.join(text)

    return text

# Extended Euclidean Algorithm
def egcd(a, b):
    # example egcd(7,26) = 15
    #Basis
    if a == 0 :
        return b,0,1
    
    #Recursive
    gcd, x1, y1 = egcd(b%a, a)

    x = y1 - (b//a)*x1
    y = x1

    return gcd,x,y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse doesn't exist
    else:
        return x % m
 
 
def affineEncrypt(text, key):
    # C = (a*P + b) % 26
    cipher = ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])

    cipher = postProcess(cipher)

    return cipher
 
 
def affineDecrypt(cipher, key):
    # P = (a^-1 * (C - b)) % 26
    plainText = ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])
    
    plainText = postProcess(plainText)

    return plainText
 
 
def main():
    text = 'kripto kelas pa rin'
    key = [17, 26]
 
    affine_encrypted_text = affineEncrypt(text, key)
 
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
 
    print('Decrypted Text: {}'.format(affineDecrypt(textCleaning(affine_encrypted_text), key) ))
 
 
if __name__ == '__main__':
    main()