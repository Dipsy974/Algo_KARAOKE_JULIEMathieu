from karaoke import Karaoke
from player import Player

#Exercice 1
player1 = Player("Mathieu")

print("Exercice 1 :")
print(player1.getName())

#Modification des scores qui sont initialement à 0. Les meilleurs scores sont remplacés, et un score < 50 est directement amené à 50.
player1.setScore(0,55)
player1.setScore(1,35)
player1.setScore(2,78)
player1.setScore(3,90)
player1.setScore(2,70)
player1.setScore(0,60)
print(player1.getListScores())
print(player1.getTotal())
print(player1.getMoyenne())
print(player1.bestScore())
print(player1.worstScore())


print()
#Exercice 2
#Ajout de la classe Karaoke, et ajout d'une méthode pour la classe Player pour actualiser les chansons correspondantes quand il est ajouté à un Karaoke

print("Exercice 2 :")

#Création du karaoké avec les différentes chansons
karaoke = Karaoke(["Bromance", "Barbie Girl", "Lalala"])

#Ajout d'un joueur au karaoké
karaoke.addJoueur("Orion")
print(karaoke.getJoueurs())

#Tentative de retrait d'un joueur du karaoké, mais il doit y en avoir un forcément.
if karaoke.removeJoueur("Orion"):
    print("Le joueur a été retiré.")
else:
    print("Il n'y a qu'un seul joueur pour l'instant, il ne peut pas être retiré. Créez en d'autres.")

#Ajout d'un autre joueur
karaoke.addJoueur("Mathieu")

#Voir les scores d'un joueur spécifique sur les différentes chansons
print(karaoke.getJoueurs()["Orion"].getListScores())

#Les deux joueurs chantent une chanson et sont notés

karaoke.getJoueurs()["Orion"].setScore("Barbie Girl", 60) #Orion est noté 60
karaoke.getJoueurs()["Mathieu"].setScore("Barbie Girl", 99) #Mathieu est noté 99

#Voir le meilleur score pour une chanson
print(karaoke.getBestScoreChanson("Barbie Girl"))

#Les deux joueurs chantent une autre chanson

karaoke.getJoueurs()["Orion"].setScore("Lalala", 98) #Orion est noté 98, il passe à 158
karaoke.getJoueurs()["Mathieu"].setScore("Barbie Girl", 35) #Mathieu est noté 35 mais sa note va être de 50, il passe à 149

#Voir le meilleur total

print(karaoke.getBestTotal()) #Avec la nouvelle chanson, c'est Orion qui a le meilleur score total. 
print(karaoke.getBestScore()) #Mathieu a le meilleur score sur toute chanson confondu

#Voir la meilleure moyenne

print(karaoke.getBestMoyenne()) 


