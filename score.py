# -*- coding:UTF-8 -*-

import pickle as pk
import random
from random import *

scores = []
fichier = open("scores.txt","wb")
pickled = pk.Pickler(fichier)
pickled.dump(scores)
fichier.close()


MAX_SCORE = 0

SCORE = []

#une fonction qui affiche l'etat du jeu
def afficheretat(i, n):
    print(i, end='')
    print("|", end ='')
    print(" ", end ='')
    j=0
    while j<n:
        print("*", end='')
        j = j + 1
        
    print(" ", end ='')
    print("|", end ='')
    print(n)


#une fonction qui calcule le score du joueur gagnant
def somme1(n):
    S = 0
    for k in range(1,n+1):
        S +=(k * pow(10, k))
    return S


def display_bye_message():
    print("\n")
    print("***************************************")
    print("    Merci d'avoir joué, à bientôt.     ")
    print("***************************************")

print ("Jeu dans lequel 2 joueurs piochent à tour de rôle un nombre de pierres dans \n un éventail de choix imposé dans le but de rammasser le ou les derniers du tas.\n\n")
    

Termine = False

while not Termine:
    
    Nomjoueur = []
    #Demande aux joueurs s'ils veulent jouer
    
    print("Voulez-vous faire une partie du jeu  ? (o/n)")
  
    c = input()
    if c == 'o' :
             print( "TODO : Le déroulement d'une partie" )
             print (" le meilleur score est %s :"%MAX_SCORE)
             nbrpierres={};


             nbr = randint(3, 7)
             print("le nbr de tas est %s :"%nbr)
             i=1
             while i <= nbr:
                var = randint(5, 23)
                v=str(i);
                nbrpierres[v] = var
                i=i + 1



#qui sont les joueurs ?
             JOUEUR1 = input("Nom du Joueur 1 : ")
             JOUEUR2 = input("Nom du Joueur 2 : ")
             Nomjoueur.append(JOUEUR1)
             Nomjoueur.append(JOUEUR2)
             joueurActuel = sample(Nomjoueur, 1)
    
    
             choixValides = []

             nbcoupActuel = 0
             nbrcoup1 = 0
             nbrcoup2 = 0
    
# petite boucle principale 
             partieTerminee = False
             while not partieTerminee:
                 for cle,valeur in nbrpierres.items():
                      cle = int(cle)
                      valeur = int(valeur)
                      afficheretat(cle,valeur)
                    

    
                 print("choisissez le tas %s"%joueurActuel)
                 for cle in nbrpierres.keys():
                       print (cle)
                 rep = input()# 'raw_input() renvoie un objet String (numero de tas)
      
                 CHOIX_POSSIBLES = nbrpierres.get(rep) # accès à la valeur du dictionnaire par sa clé
                 choixPossible = int(CHOIX_POSSIBLES)
                 if len(choixValides) > 0:
                    del choixValides[0]
            
                 if int(nbrpierres[rep]) - choixPossible >= 0:
                    choixValides.append(choixPossible)

                 nbrCailloux = int(rep)

                 print (" ")
                 print ("Il y a %s cailloux"%nbrpierres[rep])
                 print ("Choix valides : ",choixValides)
    
    #on récupère un choix valide du joueur actuel
                 choixJoueur = 0 
                 while choixJoueur == 0:
                     choixJoueur = input("Votre choix %s ? : "%joueurActuel)
                     if not choixJoueur.isdigit() :
                         print ("Un chiffre svp ...")
                         choixJoueur = 0        
                     elif choixJoueur.isdigit() and int(choixJoueur)> choixValides[0] :
                         print ("Choix invalide !... ")
                         choixJoueur = 0

    
                 nbrPierres = choixValides[0] - int(choixJoueur)
                 nbrpierres[rep] = nbrPierres
   
                 m = 0
                 for valeur in nbrpierres.values():
                         if valeur == 0:
                             m = m + 1
                

        
                 if m ==nbr :
                     partieTerminee = True
                 else :
                     if joueurActuel == JOUEUR1:
                         joueurActuel = JOUEUR2
                         nbrcoup1 = nbrcoup1 + 1
                     else:
                         joueurActuel = JOUEUR1
                         nbrcoup2 = nbrcoup2 + 1
            

             print (" %s, vous avez perdu et votre score est nul!!!"%joueurActuel)
             if joueurActuel==JOUEUR1:
                 joueur = JOUEUR2
                 nbcoupActuel = nbrcoup2
             else:
                 joueur = JOUEUR1
                 nbcoupActuel = nbrcoup1

             print("%s,Felicitation vous avez gagné"%joueur, end='')
             print("  et votre score est:",somme1(nbcoupActuel))
             SCORE.append(somme1(nbcoupActuel))
             variable = len(SCORE)
             indice = 0
             while indice < variable:
                 if MAX_SCORE < SCORE[indice]:
                     MAX_SCORE = SCORE[indice]
                 indice = indice + 1

             with open("scores.txt","rb") as fichier: #On ouvre le fichier avec "r" pour le lire (et "b" pour en binaire, Pickle est parfois capricieux)
                 unpickled = pk.Unpickler(fichier)
                 scores = unpickled.load() #On récupère la variable
                 fichier.close() # Et on ferme le fichier
                 print(scores)
 
            ## Données
            # Ce bloc simule une partie (finie), le joueur a un nom et un score.
             name = joueur
             new_score = somme1(nbcoupActuel)
     
            ##test des données
             try:
                 name_list = [score[0] for score in scores] #on crée la liste des noms
                 index = name_list.index(name) # On cherche le joueur
                 #Si le joueur a un score:
                 print("Le joueur {} a déjà un score. il est à l'index n°{} de la liste".format(name,index))
                 if new_score > scores[index][1]: # et que son nouveau score est mieux
                     scores[index][1] = new_score
             except ValueError: #Si le joueur n'a pas de score précédent / index(name) renvoie une ValueError si il trouve pas name
                 print("Le joueur n'a pas de scores précédents")
                 scores.append([name,new_score]) #on ajoute son score
             print(scores)
 
             ## Enregistrement des données
             with open("scores.txt","wb") as fichier: #on ouvre le fichier avec "w" pour le réécrire
                 pickled = pk.Pickler(fichier)
                 pickled.dump(scores) # On inscrit notre variable dans le fichier
                 fichier.close() # Et on ferme le fichier



    else :
         display_bye_message()

         Termine = True

