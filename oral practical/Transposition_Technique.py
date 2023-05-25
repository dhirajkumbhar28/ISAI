'''
The provided Python code demonstrates a basic columnar transposition cipher for encryption and decryption. Here's an explanation of the code:

1. `encrypt` Function: This function takes a `plain_text` string and a `key` list as input and returns the encrypted cipher text.

2. Variable Declarations: The function initializes variables such as `cipher_text` (empty string), `num_cols` (number of columns in the transposition matrix), and `num_rows` (number of rows in the transposition matrix).

3. Creating the Transposition Matrix: The function creates an empty matrix using a nested list comprehension. The matrix has `num_rows` rows and `num_cols` columns. Each cell in the matrix is initially empty.

4. Filling the Transposition Matrix: The function iterates over the plain text character by character and fills the matrix in a column-wise manner. The `idx` variable keeps track of the index in the plain text string. Each character is placed in the appropriate cell of the matrix until all characters are processed.

5. Building the Cipher Text: The function iterates over the columns of the matrix based on the given `key`. For each column, it retrieves the column index from the key and iterates over the rows. It appends each character in the column to the `cipher_text` string.

6. Returning the Cipher Text: The function returns the `cipher_text` string, which represents the encrypted message.

7. `decrypt` Function: This function takes a `cipher_text` string and a `key` list as input and returns the decrypted plain text.

8. Variable Declarations: The function initializes variables such as `plain_text` (empty string) and `matrix` (an empty matrix similar to the one used in encryption).

9. Building the Transposition Matrix: The function iterates over the columns of the matrix based on the given `key`. For each column, it retrieves the column index from the key and iterates over the rows. It assigns each character from the cipher text to the corresponding cell in the matrix.

10. Building the Plain Text: The function iterates over the rows and columns of the matrix and appends each character to the `plain_text` string.

11. Returning the Plain Text: The function returns the `plain_text` string, which represents the decrypted message.

12. Example Usage: The code demonstrates an example usage of the `encrypt` and `decrypt` functions. It encrypts the plain text "Hello World" using a key [3, 1, 4, 2] and prints the cipher text. Then, it decrypts the cipher text using the same key and prints the decoded plain text.

In summary, the Python code provides functions for encrypting and decrypting messages using a columnar transposition cipher. The encryption process rearranges the characters of the plain text into a matrix column-wise, based on a given key. The decryption process reconstructs the original message by reading the matrix row-wise, again based on the key.
'''
def encrypt(plain_text, key):
    cipher_text = ""
    num_cols = len(key)
    num_rows = len(plain_text) // num_cols + 1
    matrix = [["" for j in range(num_cols)] for i in range(num_rows)]
    idx = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if idx < len(plain_text):
                matrix[i][j] = plain_text[idx]
                idx += 1
            else:
                break
    for j in range(num_cols):
        col_idx = key.index(j + 1)
        for i in range(num_rows):
            cipher_text += matrix[i][col_idx]
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    num_cols = len(key)
    num_rows = len(cipher_text) // num_cols
    matrix = [["" for j in range(num_cols)] for i in range(num_rows)]
    idx = 0
    for j in range(num_cols):
        col_idx = key.index(j + 1)
        for i in range(num_rows):
            matrix[i][col_idx] = cipher_text[idx]
            idx += 1
    for i in range(num_rows):
        for j in range(num_cols):
            plain_text += matrix[i][j]
    return plain_text


# Example usage
plain_text = "Hello World"
key = [3, 1, 4, 2]
cipher_text = encrypt(plain_text, key)
print("Cipher text: " + cipher_text)
decoded_text = decrypt(cipher_text, key)
print("Decoded text: " + decoded_text)
