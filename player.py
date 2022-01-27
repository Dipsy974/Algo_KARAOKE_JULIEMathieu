class Player:

    def __init__(self, name):
        self.__name = name
        self.__listeScores = {}
        for i in range(5):
            self.__listeScores[i] = 0

    def getName(self):
        return self.__name

    def getListScores(self):
        return self.__listeScores

    def getTotal(self):
        total = 0
        for k, v in self.__listeScores.items():
            total += v
        return total

    def getMoyenne(self):
        moyenne = self.getTotal()/len(self.__listeScores)
        return moyenne

    def bestScore(self):
        best = 0
        bestIndex = 0
        for k, v in self.__listeScores.items():
            if v > best:
                best = v
                bestIndex = k
        return bestIndex, best

    def worstScore(self):
        worst = 100
        worstIndex = 0
        for k, v in self.__listeScores.items():
            if v < worst:
                worst = v
                worstIndex = k
        return worstIndex, worst

    def setScore(self, index, score):
        if self.__listeScores[index] < score:
            if score > 50:
                self.__listeScores[index] = score
            else:
                self.__listeScores[index] = 50

        return self.__listeScores

    def setChansons(self, listeChansons):
        self.__listeScores = {}
        for i in range(len(listeChansons)):
            self.__listeScores[listeChansons[i]] = 0