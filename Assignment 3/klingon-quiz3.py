# klingon-quiz3.py

'''
title: klingon quiz 3
author: Abbas Rizvi
date: 2024/02/12
'''

# List of consonants and opening the file
consonants = 'b,ch,D,gh,H,j,l,m,n,p,q,Q,r,S,t,v,w,y'
consonants = consonants.split(',')
f = open("klingon-english.txt", "r", encoding='utf-8')
f = f.readlines()

def ask_consonant():
    '''
    Asks user for a klingon consonant, keeps asking if user puts an invalid entry
    :return:
    '''
    loop = False # Flag variable
    user_consonant = ''

    while not loop:
        user_consonant = input("Which consonant do you want to practice with?")
        for i in range(len(consonants)):
            if user_consonant == consonants[i]:
                loop = True
            else:
                pass
        if loop:
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
        english_words.append(s[1][:-1]) #removes the /n from the english word

    con = ask_consonant()
    engl_word = ''
    klingon_word = ''
    for i,j in zip(klingon_words, english_words):
        if i[0] == con[0]: # klingon_words and english_words are parallel lists
            engl_word = j
            klingon_word = i

    return engl_word, klingon_word
def askTranslate(engl_word, klingon_word):
    '''
        This function tests if the user translates the english word to klingon properly, as well displays hints for wrong answers
        :param engl_word: str
        :param klingon_word: str
        :return:
    '''
    n=0
    censor = klingon_word[0]+(len(klingon_word)-2)*"*"+klingon_word[-1] # creates a censored version the word
    for i in range(3):
        translate = input(f"How do you translate {engl_word} to klingon?")
        if translate == klingon_word:
            print("Correct")
            break
        else:
            n+=1
            if n < 3:
                print(f"Sorry you're wrong! The correct answer is {censor}")
            elif n == 3:
                print(f"Sorry you're wrong! The correct answer is {klingon_word}")
            else:
                pass

if __name__ == "__main__":
    english, klingon = findWord()
    askTranslate(english, klingon)


