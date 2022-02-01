import numpy as np
import re

alphabet = "abcdefghijklmnopqrstuvwxyz"

global char_to_num, num_to_char
char_to_num = dict(zip(alphabet, range(len(alphabet))))
num_to_char = dict(zip(range(len(alphabet)), alphabet))


def clean_text(text: str) -> str:
    res = text

    # Convert to lowercase
    res = res.lower()

    # Remove whitespace
    res.strip()

    res = res.replace(" ", "")

    # Remove number
    res = ''.join([i for i in res if not i.isdigit()])

    # Remove punctuation
    res = re.sub(r'[^\w\s]', '', res)

    return res


def egcd(m, n):
    if m == 0:
        return n, 0, 1

    gcd, x_hat, y_hat = egcd(n % m, m)

    x = y_hat - (n // m) * x_hat
    y = x_hat

    return gcd, x, y


def modinv(a, m):
    """
        modinv is a function for calculate a^-1 mod m, this function will return result and
        if error this function will return -inf.
    """

    gcd, x, _ = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def matrix_modulo_invers(matrix: np.ndarray, modulus: int = 26) -> np.ndarray:
    matrix_determinant = int(np.round(np.linalg.det(matrix)))
    matrix_adjoint = np.round(
        matrix_determinant * np.linalg.inv(matrix)
    ).astype(int)
    modulo_invers_determinant = modinv(matrix_determinant % modulus, modulus)

    if(not(modulo_invers_determinant)):
        return None

    matrix_result = modulo_invers_determinant * matrix_adjoint

    return (matrix_result % modulus)


def hill_cipher_encrypt(plain_text: str, key: np.ndarray, modulus=26) -> str:
    cipher_text = ""
    plain_text = clean_text(plain_text)

    n, _ = key.shape
    plain_text_num = [char_to_num[el] for el in plain_text]
    plain_text_matrix = []

    for i in range(0, len(plain_text), n):
        plain_text_arr = []
        for j in range(i, i + n):
            plain_text_arr.append(plain_text_num[j])

        plain_text_matrix.append(plain_text_arr)

    plain_text_matrix = np.array(plain_text_matrix)
    for el in plain_text_matrix:
        el = el.reshape(-1, 1)

        curr_res = np.dot(key, el) % modulus
        curr_res = curr_res.flatten()

        for num in curr_res:
            cipher_text += num_to_char[num]

    return cipher_text


def hill_cipher_decrypt(cipher_text: str, key: np.ndarray, modulus=26) -> str:
    plain_text = ""

    key_invers = matrix_modulo_invers(key)

    n, _ = key.shape
    cipher_text_num = [char_to_num[el] for el in cipher_text]
    cipher_text_matrix = []

    for i in range(0, len(cipher_text), n):
        cipher_text_arr = []
        for j in range(i, i + n):
            cipher_text_arr.append(cipher_text_num[j])

        cipher_text_matrix.append(cipher_text_arr)

    cipher_text_matrix = np.array(cipher_text_matrix)
    for el in cipher_text_matrix:
        el = el.reshape(-1, 1)

        curr_res = np.dot(key_invers, el) % modulus
        curr_res = curr_res.flatten()

        for num in curr_res:
            plain_text += num_to_char[num]

    return plain_text
