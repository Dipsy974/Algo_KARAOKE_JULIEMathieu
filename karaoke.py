from player import Player

class Karaoke:
    def __init__(self, listeChansons):
        self.__listeChansons = listeChansons
        self.__listeJoueurs = {}

    def getChansons(self):
        return self.__listeChansons
    
    def getJoueurs(self):
        return self.__listeJoueurs

    def addJoueur(self, joueur):
        newJoueur = Player(joueur)
        newJoueur.setChansons(self.__listeChansons)
        self.__listeJoueurs[joueur] = newJoueur
        return self.__listeJoueurs

    def removeJoueur(self, joueur):
        if len(self.__listeJoueurs) > 1:
            self.__listeJoueurs.pop(joueur)
            return True
        else:
            return False

    def getBestScoreChanson(self, chanson):
        best = 0
        bestPlayer = ""
        for index, player in self.__listeJoueurs.items():
            for k, v in player.getListScores().items():
                if k == chanson:
                    if v > best:
                        best = v
                        bestPlayer = player.getName()
        return bestPlayer, best

    def getBestTotal(self):
        bestTotal = 0
        bestPlayer = ""
        for index, player in self.__listeJoueurs.items():
            if player.getTotal() > bestTotal:
                bestTotal = player.getTotal()
                bestPlayer = player.getName()
        return bestPlayer, bestTotal

    def getBestScore(self):
        best = 0
        bestPlayer = ""
        for index, player in self.__listeJoueurs.items():
            for k, v in player.getListScores().items():
                if v > best:
                    best = v
                    bestPlayer = player.getName()
        return bestPlayer, best

    
    def getBestMoyenne(self):
        bestMoyenne = 0
        bestPlayer = ""
        for index, player in self.__listeJoueurs.items():
            if player.getMoyenne() > bestMoyenne:
                bestMoyenne = player.getMoyenne()
                bestPlayer = player.getName()
        return bestPlayer, bestMoyenne