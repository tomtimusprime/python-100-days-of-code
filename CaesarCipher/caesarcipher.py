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

keepPlaying = True
keepPlayingInput = ''
while keepPlaying == True: 
    inputWord = input("Input a word in all lowercase that you would like to encrypt (no spaces, please):")
    numberOfSpaces = int(input("How many letters would you like the letters to be shifted by?"))
    encryptedWord = encrypt(inputWord, numberOfSpaces)
    print(f"The following is your decrypted word: {encryptedWord}")
    print("\n")
    yesNo = input("Would you like to have your word decrypted? (y/n)").lower()
    if yesNo == 'y':
        print(decrypt(encryptedWord, numberOfSpaces))

    keepPlayingInput = input("Do you want encrypt another word? (y/n)").lower()
    print(keepPlayingInput)
    if keepPlayingInput == "n":
        keepPlaying = False
        
    

# encryptedWord = encrypt("trifle", 5)
# print(decrypt(encryptedWord, 5))

