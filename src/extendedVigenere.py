import vignere_cipher as vc

BYTE_MAX = 256

def extended_vignere_cipher_encrypt(src_path: str, key: str, dest_path: str) -> bool :
    try:
        f = open(src_path, 'rb')

        fileData = bytearray(f.read())
        newKey = vc.generate_key_standard(fileData, vc.clean_text(key))

        for idx, plainText in enumerate(fileData):
            fileData[idx] = (plainText + ord(newKey[idx])) % BYTE_MAX

        f.close()

        f = open(dest_path, 'wb')
        f.write(fileData)
        f.close()

        return True
    except Exception as e:
        return False

def extended_vignere_cipher_decrypt(src_path: str, key: str, dest_path: str) -> str :
    try:
        f = open(src_path, 'rb')

        fileData = bytearray(f.read())
        newKey = vc.generate_key_standard(fileData, vc.clean_text(key))

        for idx, cipherText in enumerate(fileData):
            fileData[idx] = (cipherText - ord(newKey[idx])) % BYTE_MAX

        f.close()

        f = open(dest_path, 'wb')
        f.write(fileData)
        f.close()

        return True
    except:
        return False