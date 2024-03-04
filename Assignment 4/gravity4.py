# gravity4.py

'''
title: Ceaser/A1Z26/Atbash Cipher
Author: Abbas Rizvi
date: 2024/03/03
This program is a ceaser/atbash/A1Z26 cipher, combining all 3
'''

import string
# lists of letters
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
        flag = False # checks to see if character is a letter in the alphabet
        for j in range(len(capital_letters)):
            if letter == capital_letters[j]:
                text_list.append(capital_letters[(j-shift)%26]) # shifts letter by 3
                flag = True
        for j in range(len(lower_letters)):
            if letter == lower_letters[j]:
                text_list.append(lower_letters[(j-shift)%26])
                flag = True
        if not flag:
            # if character is not shiftable we just append the character in the final list
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
    # Reverses list to have corresponding letters match
    capital_letters_reverse = capital_letters[::-1]
    lower_letters_reverse = lower_letters[::-1]
    text_list =[]
    atbash = ''

    for letter in text:
        flag = False # checks to see if letter is swappable
        for j in range(len(capital_letters)):
            if letter == capital_letters[j]:
                text_list.append(capital_letters_reverse[j]) # lists are parallel
                flag = True
        for j in range(len(lower_letters)):
            if letter == lower_letters[j]:
                text_list.append(lower_letters_reverse[j])
                flag = True
        if not flag:
            # appends original character if character is not swappable
            text_list.append(letter)

    for i in range(len(text_list)):
        atbash += text_list[i]

    return atbash

def decrypt_a1z26(text):
    """
    Decipher a text (A1Z26 cipher).
    :param text: (str)
    :return: (str)
    """

    text_list = []
    a1z26 = ''
    period = ''

    if not text[-1].isnumeric():
        # removes character at end of the string if it is not a number it is removed then saved
        period = text[-1]
        text = text.rstrip(text[-1])


    text1 = text.split() # creates list of text, split by white space

    for i in range(len(text1)):
        word = text1[i].split('-') # splits each word into numbers
        for j in range(len(word)):
            if word[j][0].isnumeric():
                #tests to see if input is in right format
                index = int(word[j])
                text_list.append(capital_letters[index-1])
            else:
                # just returns original
                return (text+period)
        text_list.append(' ')

    for i in range(len(text_list)):
        a1z26 += text_list[i]
    a1z26 = a1z26.rstrip() + period

    return a1z26

def main():
    """
    Main program.
    """
    # takes input
    text = input("Enter a text to decipher: ")
    print("Let's try all the methods we have:")

    # different combinations of cyphers
    ceaser = decrypt_caesar(text,3)
    atbash = decrypt_atbash(text)
    combined_ceaser_atbash = decrypt_atbash(decrypt_caesar(text,3))
    combined_atbash_ceaser = decrypt_caesar(decrypt_atbash(text),3)
    a1z26 = decrypt_a1z26(text)
    combined_a1z26_ceaser = decrypt_caesar(decrypt_a1z26(text),3)
    combined_a1z26_atbash = decrypt_atbash(decrypt_a1z26(text))
    combined_a1z26_atbash_ceaser = decrypt_caesar(decrypt_atbash(decrypt_a1z26(text)),3)
    combined_a1z26_ceaser_atbash = decrypt_atbash(decrypt_caesar(decrypt_a1z26(text),3))

    #prints results
    print(f"Ceaser Cipher: {ceaser}")
    print(f"Atbash Cipher: {atbash}")
    print(f"Combined: 1) Caesar; 2) Atbash cipher: {combined_ceaser_atbash}")
    print(f"Combined: 1) Atbash; 2) Caesar cipher: {combined_atbash_ceaser}")
    print(f"A1Z26 Cipher: {a1z26}")
    print(f"Combined: 1) A1Z26; 2) Caesar cipher: {combined_a1z26_ceaser}")
    print(f"Combined: 1) A1Z26; 2) Atbash cipher: {combined_a1z26_atbash}")
    print(f"Combined: 1) A1Z26; 2) Atbash; 3) Caesar cipher: {combined_a1z26_atbash_ceaser}")
    print(f"Combined: 1) A1Z26; 2) Caesar; 3) Atbash cipher: {combined_a1z26_ceaser_atbash}")
main()



