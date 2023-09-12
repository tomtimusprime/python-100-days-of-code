

def encrypt(inputWord, numberToShift):
    lettersInAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_word = ''
    for letter in inputWord:
        position = lettersInAlphabet.index(letter)
        new_position = position + numberToShift
        new_character = lettersInAlphabet[new_position]
        new_word += new_character

    return new_word

def decrypt(inputWord, numberToShift):
    lettersInAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_word = ''
    for letter in inputWord:
        position = lettersInAlphabet.index(letter)
        new_position = position - numberToShift
        new_character = lettersInAlphabet[new_position]
        new_word += new_character

    return new_word

print(encrypt("helloworld", 5))
encryptedWord = encrypt("helloworld", 5)
print(decrypt(encryptedWord, 5))

