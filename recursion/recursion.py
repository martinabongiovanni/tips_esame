'''
LAB_11:
Dato il grafo costruito al punto precedente, si vuole identificare un percorso su grafo tale per cui,
dato un vertice di partenza (selezionato dall'apposita tendina), si identifichi il percorso più lungo
in termini di numero di archi, composto da archi dal peso sempre crescente.

• La valutazione della soluzione migliore è rappresentata dal numero di archi attraversati (senza considerare il
relativo peso).
• Un arco può essere aggiunto al percorso se e solo se il suo peso è maggiore uguale a tutti i pesi degli archi già
aggiunti al percorso.
'''
def getPercorsoMaxRecursive(self, prodotto):
    nodo = self._idMap[int(prodotto)]
    self._percorsoMax = []
    percorso_temp = [nodo]
    for vicino in self._grafo.neighbors(nodo):
        percorso_temp.append(vicino)
        self.ricorsione(percorso_temp, self._grafo[nodo][vicino]['weight'])
    return len(self._percorsoMax) - 1  # per ottenere il numero di archi del cammino


def ricorsione(self, percorso_temp, peso_arco_precedente):
    if len(percorso_temp) > len(self._percorsoMax):
        self._percorsoMax = list(percorso_temp)  # per avere uan copia profonda di quello che è il nuovo percorsoMax

    ultimo = percorso_temp[-1]
    for vicino in self._grafo.neighbors(ultimo):
        if (vicino not in percorso_temp
                and self.isValid(self._grafo[ultimo][vicino]['weight'], peso_arco_precedente)):
            percorso_temp.append(vicino)
            self.ricorsione(percorso_temp, self._grafo[ultimo][vicino]['weight'])
            percorso_temp.pop()


def isValid(self, peso_arco_corrente, peso_arco_precedente):
    if peso_arco_corrente >= peso_arco_precedente:
        return True
    return False

'''
LAB_13:
a. Facendo click sul pulsante "DreamTeam", individuare un dream team.
b. Definiamo come team un gruppo di K piloti. La dimensione K del team viene stabilita dall'utente con
l'apposita casella di testo.
c. Il tasso di sconfitta di un team è definito come il numero totale di vittorie di un qualsiasi pilota non
appartenente al team su un qualsiasi pilota appartenente al team.
d. Un dream team è un team di K piloti che abbia il minimo tasso di sconfitta.
'''
def getDreamTeam(self, dimensione):
    self._best_team = []
    self._best_score = 100000  # per inizializzare a un valore molto alto
    temp_team = []
    self.ricorsione(temp_team, dimensione)
    lista_drivers_best_team = []
    for driver in self._best_team:
        lista_drivers_best_team.append(self._id_map_drivers[driver.driverId])
    return self._best_team, self._min_score


def ricorsione(self, temp_team, dimensione):
    if len(temp_team) == dimensione:
        score = self.getScore(temp_team)
        if score < self._best_score:
            self._min_score = score
            self._best_team = copy.deepcopy(temp_team)
        return

    for driver in self._drivers:
        if driver not in temp_team:
            temp_team.append(driver)
            self.ricorsione(temp_team, dimensione)
            temp_team.pop()  # backtracking


def getScore(self, temp_team):
    score = 0
    for edge in self._grafo.edges(data=True):
        if edge[0] not in temp_team and edge[1] in temp_team:  # analizzo gli archi entranti nel team
            score += edge[2]["weight"]
    return score

'''
iTunes:
Permettere all'utente di inserire una durata complessiva dTOT, espressa in minuti. Alla pressione del bottone 
"Set di Album", utilizzare un algoritmo ricorsivo per estrarre un set di album dal grafo che abbia le seguenti 
caratteristiche:
• includa a1;
• includa solo album appartenenti alla stessa componente connessa di a1;
• includa il maggior numero possibile di album;
• abbia una durata complessiva, definita come la somma della durata degli album in esso contenuti, non
superiore dTOT.
'''
def getSetOfNodes(self, a1, soglia):
    self._bestSet = {}
    self._maxLen = 0

    parziale = {a1}
    cc = nx.node_connected_component(self._grafo, a1)

    cc.remove(a1)

    for n in cc:
        # richiamo la mia ricorsione
        parziale.add(n)
        cc.remove(n)
        self._ricorsione(parziale, cc, soglia)
        cc.add(n)
        parziale.remove(n)

    return self._bestSet, self._getDurataTot(self._bestSet)


def _ricorsione(self, parziale, rimanenti, soglia):
    # 1) verifico che parziale sia una soluzione ammissibile, ovvero se viola i vincoli.
    if self._getDurataTot(parziale) > soglia:
        return

    # 2) se parziale soddisfa i criteri, allora verifico se è migliore di bestSet
    if len(parziale) > self._maxLen:
        self._maxLen = len(parziale)
        self._bestSet = copy.deepcopy(parziale)

    # 3) aggiungo e faccio ricorsione
    for r in rimanenti:
        parziale.add(r)
        rimanenti.remove(r)
        self._ricorsione(parziale, rimanenti, soglia)
        parziale.remove(r)
        rimanenti.add(r)
