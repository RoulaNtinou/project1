#Lexeis
import random

def print_hint(hint):
    r=''
    for x in hint:
        r=r+x+' '
    return r

words=['bootcamp','pasparakis','algorithm']

#to secret einai i lexi pou dialexe
secret=random.choice(words)


#to hint pou deixnoume ston paixti
hint=[]
for i in range(len(secret)):
    hint.append('_')

#to plithos ton prospatheivn pou apomenoun
guesses=7
used_letters=[]
while guesses>0 and '_' in hint:
    print(guesses,'guesses remaining!')
    print('Hint is ',print_hint(hint))
    choice=input('Give a letter: ')
    while len(choice)!=1 or not choice.isalpha() and not choice.islower() or choice in used_letters:
        choice=input('Give a letter: ')

    used_letters.append(choice)
    if choice in secret:
        for i in range(len(secret)):
            if secret[i]==choice:
               hint[i]=choice
        print('You guessed right!')
    else:
        guesses=guesses-1
        print('Wrong guess!')
if guesses>0:
    print('You win!')
else:
    print('You lost!')

