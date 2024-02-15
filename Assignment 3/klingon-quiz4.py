# klingon-quiz4.py

'''
title: klingon quiz 4
author: Abbas Rizvi
date: 2024/02/12
'''
import random

# Lists consonants and opens the file
consonants = 'b,ch,D,gh,H,j,l,m,n,p,q,Q,r,S,t,v,w,y'
consonants = consonants.split(',')
f = open("klingon-english.txt", "r", encoding='utf-8')
f = f.readlines()

def ask_consonant():
    '''
        Asks user for a klingon consonant, keeps asking if user puts an invalid entry
        :return:
    '''
    loop = False # flag variable
    user_consonant = ''

    while not loop:
        user_consonant = input("Which consonant do you want to practice with?")
        for i in range(len(consonants)):
            if user_consonant == consonants[i]:
                loop = True
            else:
                pass
        if loop:
            # If loop isnt true the while loop will repeat
            break

    return user_consonant

def findWord():
    '''
        Finds the corresponding klingon word and english translation for the user entry
        :return: str(engl_word), str(klingon_word)
    '''
    klingon_words = []
    english_words = []
    for i in range(len(f)):
        s = f[i].split("|") # Splits file lines into klingon word and english word
        klingon_words.append(s[0])
        english_words.append(s[1][:-1])

    con = ask_consonant()
    engl_word = ''
    klingon_word = ''
    for i,j in zip(klingon_words, english_words):
        if i[0] == con[0]: # klingon_words and english_words are parallel lists
            engl_word = j
            klingon_word = i


    return engl_word, klingon_word
def askTranslate(engl_word, klingon_word, censor, adv_censor):
    '''
        This function tests if the user translates the english word to klingon properly, as well displays hints for wrong answers
        :param engl_word: str
        :param klingon_word: str
        :return:
    '''
    n=0 # checks how many tries the user has used up

    for i in range(3):
        translate = input(f"How do you translate {engl_word} to klingon?")
        if translate == klingon_word:
            # if the comparison is true the loop ends
            print("Correct")
            break
        else:
            n+=1
            if n < 2:
                # uses the censor
                print(f"Sorry you're wrong! The correct answer is {censor}")
            elif n == 2:
                # uses the advanced censor
                print(f"Sorry you're wrong! The correct answer is {adv_censor}")
            else:
                pass
def censors(klingon_word):
    '''
    :param klingon_word: str
    :return: censor: str
             adv_censor_str: str
    '''
    censor = klingon_word[0] + (len(klingon_word)-2) * "*" + klingon_word[-1] # creates the censor

    adv_censor_index = random.randint(1, len(klingon_word) - 1)
    adv_censor = list(censor)
    adv_censor[adv_censor_index] = klingon_word[adv_censor_index] # replaces random part of censor with a letter

    adv_censor_str = ''
    for i in range(len(adv_censor)):
        adv_censor_str += adv_censor[i]

    return censor, adv_censor_str

if __name__ == "__main__":
    english, klingon = findWord()
    censor, adv_censor = censors(klingon)
    askTranslate(english, klingon, censor, adv_censor)

