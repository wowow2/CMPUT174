# gravity1.py

'''
title: Ceaser Cipher
Author: Abbas Rizvi
date: 2024/03/03
This program is a ceaser cipher
'''
import string
capital_letters = list(string.ascii_uppercase)
lower_letters = list(string.ascii_lowercase)
def decrypt_caesar(text, shift):
    """
    Decipher a text (Caesar cipher).
    :param text: (str)
    :param shift: (int)
    :return: (str)
    """
    ceaser = ''
    text_list = []

    for letter in text:
        flag = False
        for j in range(len(capital_letters)):
            if letter == capital_letters[j]:
                text_list.append(capital_letters[(j-shift)%26])
                flag = True
        for j in range(len(lower_letters)):
            if letter == lower_letters[j]:
                text_list.append(lower_letters[(j-shift)%26])
                flag = True
        if not flag:
            text_list.append(letter)
    for i in range(len(text_list)):
        ceaser += text_list[i]

    return ceaser


def main() -> None:
    """
    Main program.
    """
    text = input("Enter a text to decipher: ")
    ceaser = decrypt_caesar(text,3)
    print(ceaser)

main()



