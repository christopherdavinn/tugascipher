import re
import random
import string

alphabetUppercase = list(string.ascii_uppercase)


def textCleaning(text):
    text = text.upper()
    text = re.sub(r'\s*\d+\s*', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace(' ', '')
    return text


def postProcess(text):
    text = [text[i:i+5] for i in range(0, len(text), 5)]
    text = ' '.join(text)

    return text


def generateKey(text, key):
    key = list(key)
    if len(text) == len(key):
        return(key)
    else:
        for i in range(len(text)-len(key)):
            key.append(key[i % len(key)])
    retVal = "".join(key)
    retVal.upper()

    return(retVal)


def generateFullVigenereMatrix():
    matrix = []
    for i in range(26):
        isDuplicate = True
        while isDuplicate:
            tempAlpha = alphabetUppercase
            random.shuffle(tempAlpha)
            tempStr = ''.join(tempAlpha)
            if tempStr not in matrix:
                isDuplicate = False
        matrix.append(tempStr)

    return matrix


def encrypt(text, key, matrix):
    text = textCleaning(text)
    key = generateKey(text, key).upper()
    # text is cleaned

    cipher = ''

    for i in range(len(text)):
        idxKey = i % len(key)
        col = string.ascii_uppercase.index(text[i])
        row = string.ascii_uppercase.index(key[idxKey])

        cipher += matrix[row][col]

    cipher = postProcess(cipher)

    return cipher


def decrypt(cipher, key, matrix):
    cipher = textCleaning(cipher)
    key = generateKey(cipher, key).upper()
    # ciphertext is cleaned

    plaintext = ''

    for i in range(len(cipher)):
        idxKey = i % len(key)
        row = string.ascii_uppercase.index(key[idxKey])
        vRow = matrix[row]
        idxLetter = vRow.index(cipher[i])

        plaintext += string.ascii_uppercase[idxLetter]

    plaintext = postProcess(plaintext)

    return plaintext
            
def main():
    matrix = generateFullVigenereMatrix();
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         print('{}'.format(matrix[i][j]), end='')
    #     print()
    
    # arrmat = matrix.split('\n')
    while 1 :
        choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT \n"))
        if choice==1:
            # matrix = generateFullVigenereMatrix();
            plaintext = input('Insert Plaintext :')
            key = input('Insert Key : ')
            print('Result : ' + encrypt(plaintext, key, matrix))
        elif choice==2:
            # matrix = generateFullVigenereMatrix();
            cipher = input("Insert Ciphertext : ")
            key = input('Insert Key : ')
            print('Result : ' + decrypt(cipher, key, matrix))
        elif choice==3:
            exit()
        else:
            print("Choose correct choice")
    return 0



# key=input("Enter key")

if __name__ == '__main__':
    main()
