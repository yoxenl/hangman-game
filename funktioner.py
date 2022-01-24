import json #finna ord.json filen
import turtle #grafik gui osv
from random import * #slumpmässa saker och ting

def welcome(): #välkomnar spelaren
    #fråga om den vill spela själv, mot datorn eller avsluta programmet
    tema = input('\nVälkommen till hänga gubbe!\nBörja spelet genom att välja ett tema:\nDjur, känsla, stad, titel eller färg\nSkriv in \'q\' för att avsluta :)\n')
    return tema

def hide_brushes(t, t1, t2):
    t.hideturtle()
    t1.hideturtle()
    t2.hideturtle()

def show_brushes(t, t1, t2):
    t.showturtle()
    t1.showturtle()
    t2.showturtle()

def choose_word(tema): #väljer ordet slumpmässigt
    f = open('ord.json', 'r')
    ord = json.load(f)
    tema = tema.lower()
    try:
        MAX = len(ord[tema])
    except: 
        MAX = len(ord)
    ordet = ord[tema][randint(0, MAX)]
    f.close()
    return ordet

def gissning(ord, tema): #gissa ordet funktionen
    ordet = list(ord)
    lista_ordet = []
    MAX = len(ordet)
    for i in range(MAX):
        lista_ordet.append('_')

    gissade = [] #tom lista där gissade bokstäver hamnar

    def print_guessed(): #skriver ut gissade bokstäver
        längd = len(gissade)
        print('-------------------------------------------------------\nRedan gissade: ')
        for i in range(längd):
            print(gissade[i], end=' ')

    incompleted = True 
    while incompleted: #loop som körs till ordet är komplett
        print(f'\nTemat är: {tema}')
        for i in range(MAX):
            print(lista_ordet[i], end=' ')
        print(f'({MAX} bokstäver)')
        bokstav = (input('\nGissa en bokstav: '))
        
        if bokstav in gissade: #kollar om bokstaven redan är gissad
            print('Du har redan gissat den här bokstaven')
            print_guessed()
            continue

        antal_fel = 0

        for index, i in enumerate(ordet): #hitta indexen för bokstaven/bokstäverna i ordet
            if ordet[index] == bokstav: #kolla om bokstaven finns i ordet
                lista_ordet.insert(index, bokstav) #byta ut linjen mot bokstaven
                lista_ordet.pop(index + 1)
            else:
                antal_fel += 1
        
        gissade.append(bokstav)

        if ordet == lista_ordet: #kollar om ordet är komplett
            print(f'\nBra jobbat! Ordet var:')
            for i in range(MAX):
                print(ordet[i], end='')
            incompleted = False
        else:
            print_guessed()
            
def play_again(): #spela igen?

    def tvinga_svar(svar):
        svar = svar.upper()
        if svar == 'Y':
            return True
        elif svar == 'N':
            return False
        else: 
            svar = input('\nAnge Y eller N\nVill du spela igen? Y/N: ')
            return tvinga_svar(svar)

    svar = input('\nVill du spela igen? Y/N: ')
    return tvinga_svar(svar)

def exit(scr): #avluta turtle
    scr.clear()

    #writes thanks for playing

    scr.bye()

#this is the end of the game