def run():
    en_or_decryption()


def en_or_decryption():
    print("Encryption (Y) or Decryption (N)")
    user_input = input()
    if user_input.lower() == 'y':
        choose_encryption()
    else:
        choose_decryption()


def choose_decryption():
    print("Caesar or Vigenère (C/V)")
    verfahren = input()

    print("Wähle ein Wort zum Verschlüsseln: ")
    word = input()

    if verfahren.lower() == 'c':
        caesar_decrypt(word)
    else:
        vigenere_decrypt(word)


def choose_encryption():
    print("Caesar or Vigenère (C/V)")
    verfahren = input()

    print("Wähle ein Wort zum Verschlüsseln: ")
    word = input()

    if verfahren.lower() == 'c':
        caesar_encrypt(word)
    else:
        vigenere_encrypt(word)


def vigenere_encrypt(word: str):
    keyword = ""
    print("Wähle ein Verschlüsselungswort: ")
    while keyword == "":
        keyword = input()
        if len(keyword) != len(word):
            print("! Die Länge muss mit dem zu verschlüsselten Wort übereinstimmen !")
            keyword = ""
    result = ""

    for i in range(0, len(word)):
        temp = ord(word[i]) + ord(keyword[i])
        print(f"{ord(word[i])} + {ord(keyword[i])} = {temp}")
        while temp > 126:
            temp -= 95
        result += chr(temp)

    print(result)


def vigenere_decrypt(word: str):
    keyword = ""
    print("Wähle ein Entschlüsselungswort: ")
    while keyword == "":
        keyword = input()
        if len(keyword) != len(word):
            print("! Die Länge muss mit dem verschlüsselten Wort übereinstimmen !")
            keyword = ""
    result = ""

    for i in range(0, len(word)):
        temp = ord(word[i]) - ord(keyword[i])
        while temp < 32:
            temp += 95
        result += chr(temp)

    print(result)


def caesar_encrypt(word: str):
    print("Wähle einen Schlüssel: ")
    key = int(input())

    result = ""
    for c in word:
        temp = ord(c) + key
        while temp > 126:
            temp -= 95
        print(temp)
        result += chr(temp)

    print(result)


def caesar_decrypt(word: str):
    print("Wähle einen Schlüssel: ")
    key = int(input())

    result = ""
    for c in word:
        temp = ord(c) - key
        while temp < 32:
            temp += 95
        result += chr(temp)

    print(result)
