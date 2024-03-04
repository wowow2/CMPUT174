# gravity2.py

'''
title: Atbash Cipher
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
def decrypt_atbash(text):
    """
    Decipher a text (Atbash cipher).
    :param text: (str)
    :return: (str)
    """
    capital_letters_reverse = capital_letters[::-1]
    lower_letters_reverse = lower_letters[::-1]
    text_list =[]
    atbash = ''

    for letter in text:
        flag = False
        for j in range(len(capital_letters)):
            if letter == capital_letters[j]:
                text_list.append(capital_letters_reverse[j])
                flag = True
        for j in range(len(lower_letters)):
            if letter == lower_letters[j]:
                text_list.append(lower_letters_reverse[j])
                flag = True
        if not flag:
            text_list.append(letter)

    for i in range(len(text_list)):
        atbash += text_list[i]

    return atbash

def main():
    """
    Main program.
    """
    text = input("Enter a text to decipher: ")
    print("Let's try all the methods we have:")
    ceaser = decrypt_caesar(text,3)
    atbash = decrypt_atbash(text)
    print(f"Ceaser Cipher: {ceaser}")
    print(f"Ceaser Cipher: {atbash}")
main()



