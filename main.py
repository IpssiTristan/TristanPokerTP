import pandas as pd
import random
import sys

deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

len(deck)

def argent():
    print("Combien voulez-vous mettre dans votre Bankroll ?")
    total_argent = int(input())
    print("Combien voulez-vous miser ?")
    mise = int(input())
    if mise <= total_argent:
        print("\ntu as miser", mise, "€\n")
        total_argent = total_argent - mise
    else:
        print("Vous ne pouvez pas miser plus que votre Bankroll")
        sys.exit(0);
    return total_argent, mise



def premier_tirage(deck):
    tirage = random.sample(deck, 5)
    for i in tirage:
        deck.remove(i)
    return tirage, deck

def choix_carte(tirage):
    print("Premier tirage :", tirage)
    jeu = []                #créé la liste jeu
    for i in tirage:        #boucle for du premier tirage
        print("\nCarte :", i)            #affiche premier carte tirage
        choix = input('Voulez vous garder la carte ?(y/n):') #affiche la demande pour garder la carte
        if choix == 'y':        #SI oui
            jeu.append(i)       # enregistrer la valeur dans carte dans la liste et refaire boucle

    return jeu  #retourne le jeu quand boucle fini

def deuxieme_tirage(jeu, deck):
    nb_carte = len(jeu)
    carte_a_tirer = 5 - nb_carte
    tirage_2 = random.sample(deck, carte_a_tirer)
    for i in tirage_2:
        jeu.append(i)
    return jeu

def afficher_tirage():
    print('\nVotre tirage final: ', jeu, "\n")


"""
def machine():
    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    tirage, deck = premier_tirage(deck)
    print(tirage)
    jeu = choix_carte(tirage)
    tirage_final = deuxieme_tirage(jeu, deck)
    print(tirage_final)
    return tirage_final
"""
def decompose_jeu(jeu):
        dic = {}
        keys = [1,2,3,4,5]
        valeur = []
        couleur = []
        for i,k in zip(jeu,keys):
            dic[k] = i.split('-')
        for key in dic.keys():
            valeur.append(dic[key][0])
            couleur.append(dic[key][1])
        return valeur, couleur



def convert_carte(valeur):
    for e,i in zip (valeur, range(0,5)):
        try:
            valeur[i] = int(e)
        except:
            if e == 'J':
                valeur[i] = 11
            elif e == 'Q':
                valeur[i] = 12
            elif e =='K':
                valeur[i] =13
            elif e == 'A':
                valeur[i] = 1
            else:
                continue
    return valeur

def quinte_flush_royale(jeu):
    valeur_gagnante = ['10','J','Q','K','A']
    valeur, couleur = decompose_jeu(jeu)
    if sorted(valeur_gagnante) == sorted(valeur) and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False



def quinte_flush(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('True') == 4 and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False



def carre(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
            count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [1, 4]:
        return True
    else:
        return False



def brelan(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
            count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 1, 3]:
        return True
    else:
        return False


def pair(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
            count.append(valeur.count(i))
    if len(uniques) == 4 and sorted(count) == [1, 1, 1, 2]:
        return True
    else:
        return False



def double_pair(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
            count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 2, 2]:
        return True
    else:
        return False



def full (jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [2, 3]:
        return True
    else:
        return False


def flush(jeu):
    valeur, couleur = decompose_jeu(jeu)
    if couleur.count(couleur[0]) == 5:
        return True
    else:
        return False



def quinte(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur) - 1)):
        if e + 1 == valeur[i + 1]:
            suite.append('True')
    if suite.count('True') == 4:
        return True
    else:
        return False



def calculer_gains(mise):
    total = 0
    if pair(jeu) == True:
        total = mise * 1
        print("Vous avez une paire !\n(Une fois la mise)\n", "Gain =", total, "€")
    elif double_pair(jeu) == True:
        total = mise * 2
        print("Vous avez une double paire !\n(2 fois la mise)\n", "Gain =", total, "€")
    elif brelan(jeu) == True:
        total = mise * 3
        print("Vous avez un brelan !\n(3 fois la mise)\n", "Gain =", total, "€")
    elif quinte(jeu) == True:
        total = mise * 4
        print("Vous avez une quinte !\n(4 fois la mise)\n", "Gain =", total, "€")
    elif flush(jeu) == True:
        total = mise * 6
        print("Vous aves un flush !\n(6 fois la mise)\n", "Gain =", total, "€")
    elif full(jeu) == True:
        total = mise * 9
        print("Vous avez un full !\n(9 fois la mise)\n", "Gain =", total, "€")
    elif carre(jeu) == True:
        total = mise * 25
        print("Vous avez un carre !\n(25 fois la mise)\n", "Gain =", total, "€")
    elif quinte_flush(jeu) == True:
        total = mise * 50
        print("Vous avez une quinte flush !\n(50 fois la mise)\n", "Gain =", total, "€")
    elif quinte_flush_royale(jeu) == True:
        total = mise * 250
        print("Vous avez une quinte flush royale !\n(250 fois la mise)\n", "Gain =", total, "€")
    else:
        total = mise * 0
        print("\nVous perdez votre mise...\n", "Gain =", total, "€\n")
    return total


def fin_partie(total_argent, total):
    total_argent = total_argent + total
    print("\nVotre nouvelle Bankroll =", total_argent, "€\n")
    print("Voulez-vous rejouer? (oui/non) :      ")
    jouer = input()
    if jouer in ["oui", "o", "yes"]:
        print("Nouvelle partie\n")
    elif jouer in ["non", "n", "nope"]:
        print ("Votre argent :", total_argent, "€")
        sys.exit(0);
    return total_argent


def nouvelle_mise(total_argent):
    print("Combien voulez-vous miser ?")
    mise = int(input())
    if mise <= total_argent:
        print("tu as miser", mise, "€")
        total_argent = total_argent - mise
    else:
        print("Vous ne pouvez pas miser plus que votre Bankroll")
        sys.exit(0);
    return total_argent, mise



total_argent,mise = argent()
while True:
    tirage, deck = premier_tirage(deck)  # défini le tirage et le nouveau deck
    jeu = choix_carte(tirage)
    jeu = deuxieme_tirage(jeu, deck)
    afficher_tirage()
    valeur, couleur = decompose_jeu(jeu)
    quinte_flush_royale(jeu)
    quinte_flush(jeu)
    carre(jeu)
    brelan(jeu)
    pair(jeu)
    double_pair(jeu)
    full(jeu)
    flush(jeu)
    quinte(jeu)
    total = calculer_gains(mise)
    total_argent = fin_partie(total_argent, total)
    total_argent, mise = nouvelle_mise(total_argent)







