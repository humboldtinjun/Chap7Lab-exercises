def vigenere_header(alphabet):
    """Prints the header row"""
    alpha_len = len(alphabet)
    print('|   ', end='')
    for i in range(alpha_len):
        print(f"| {alphabet[i]}", end=' ')
    print('|')
    print(f"{'|---'*(alpha_len + 1)}|")

def vigenere_sq(alphabet):
    """ generates and prints the full vigenere square by shifting them on each row"""
    alpha_len = len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                c = alphabet[(i + shift) % alpha_len]
                print(f"| {c}", end=' ')
                print(f"| {c}", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
        print("|")

def letter_to_index(letter, alphabet:str):
    """returns the index of a given letter in the alphabet"""
    return alphabet.lower().index(letter.lower())

def index_to_letter(index, alphabet):
    """returns the letter that the index gives """
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''


def vigenere_index(key_letter, plaintext_letter, alphabet):
    """computes the vigenere cipher index by shifting the letters by the key letter"""
    return (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    """encrypts the plaintext using the cipher with the given key"""
    cipher_text = ''
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text += ' '
        elif(c.upper() in alphabet):
            # print(f'{c}, {key[counter % len(key)]}')
            cipher_text += index_to_letter(vigenere_index(key[counter % len(key)], c, alphabet), alphabet)
            counter += 1
    return cipher_text


key = 'BLUESMURF'
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = 'Hello World, I am here'


#print(letter_to_index('h', alphabet))
#print(letter_to_index('7', alphabet))
#print(vigenere_index('b', 'h', alphabet))

print(encrypt_vigenere(key, message, alphabet))





#vigenere_sq(alphabet)