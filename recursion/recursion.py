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
from copy import deepcopy


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
Permettere all’utente di inserire una durata complessiva dTOT, espressa in minuti. 
Alla pressione del bottone “Set di Album”, utilizzare un algoritmo ricorsivo per 
estrarre un set di album dal grafo che abbia le seguenti caratteristiche:
• includa a1;
• includa solo album appartenenti alla stessa componente connessa di a1;
• includa il maggior numero possibile di album;
• abbia una durata complessiva, definita come la somma della durata degli album 
    in esso contenuti, non superiore dTOT.
'''


def get_best_set(self, a1, d_tot):
    self._nodi_candidati = self.fill_set_album_candidati(a1)  # set di nodi candidati a entrare nel best_set
    temp_set = set()  # definisco un set temporaneo
    temp_set.add(a1)  # aggiungo al set temporaneo a1
    durata_temp = a1.durata
    self.ricorsione(temp_set, durata_temp, d_tot, 0)
    return self._best_set


def fill_set_album_candidati(self, a1):
    # individuo il set che rappresenta la componente connessa al nodo a1
    componente = self.get_componente_connessa(a1)
    # creo una lista in cui inserisco tutti i nodi candidati a entrare nel best_set,
    # tranne a1 che ovviamente deve essere parte del best_set
    nodi_candidati = []
    for album in componente:
        if album != a1:
            nodi_candidati.append(album)
    return nodi_candidati


def ricorsione(self, temp_set, durata_temp, d_tot, indice):
    # Se la dimensione corrente è migliore, aggiorno la variabile best_set
    if len(temp_set) > len(self._best_set):
        self._best_set = temp_set.copy()

    # Se sono finiti i candidati, esco dalla ricorsione
    if indice == len(self._nodi_candidati):
        return

    # calcolo durata del temp_set con l'inserimento del nuovo candidato
    for i in range(indice, len(self._nodi_candidati)):
        album_corrente = self._nodi_candidati[i]
        nuova_durata = durata_temp + album_corrente.durata

        # se la durata del nuovo temp_set è inferiore a dTot
        if nuova_durata <= d_tot:
            # Aggiungo l'album_corrente al temp_set e continuo la ricorsione
            temp_set.add(album_corrente)
            self.ricorsione(temp_set, nuova_durata, d_tot, i + 1)
            # Backtracking: tolgo album_corrente e provo altri
            temp_set.remove(album_corrente)
            return

'''
LAB_14:
l’applicazione visualizza il cammino più lungo partendo da un nodo. Il nodo è selezionato
dall’apposito menù a tendina.
'''
def get_longest_path(self, order_id):
    starting_node = self._id_map_ordini[int(order_id)]
    self._percorso_max = []
    percorso_temp = []
    percorso_temp.append(starting_node)
    for vicino in self._grafo.successors(starting_node):
        percorso_temp.append(vicino)
        self.ricorsione(percorso_temp)
        percorso_temp.pop()
    return self._percorso_max


def ricorsione(self, percorso_temp):
    if len(percorso_temp) > len(self._percorso_max):
        self._percorso_max = deepcopy(percorso_temp)
    ultimo = percorso_temp[-1]
    for vicino in self._grafo.successors(ultimo):
        if vicino not in percorso_temp:
            percorso_temp.append(vicino)
            self.ricorsione(percorso_temp)
            percorso_temp.pop()

'''
LAB_14:
si implementi una procedura ricorsiva che calcoli un percorso di peso massimo. 
Il vertice di partenza è quello selezionato nel punto 1.c e il peso degli archi 
nel percorso deve essere strettamente decrescente.
N.B.: un vertice può entrare una volta sola nel percorso
'''
def get_heavier_path(self, order_id):
    starting_node = self._id_map_ordini[int(order_id)]
    self._heavier_path = []
    self._best_weight = 0

    parziale = []
    parziale.append(starting_node)
    for vicino in self._grafo.successors(starting_node):
        parziale.append(vicino)
        self.ricorsione_by_peso(parziale)
        parziale.pop()
    return self._heavier_path


def ricorsione_by_peso(self, parziale):
    if (new_peso := self.peso(parziale)) > self._best_weight:
        self._best_weight = new_peso
        self._heavier_path = deepcopy(parziale)
    ultimo = parziale[-1]
    for vicino in self._grafo.successors(ultimo):
        if self.is_valid(vicino, parziale):
            parziale.append(vicino)
            self.ricorsione_by_peso(parziale)
            parziale.pop()


def is_valid(self, vicino, parziale):
    # il nodo vicino non deve essere già contenuto nella lista parziale
    # il peso dell'arco che voglio inserire deve essere minore di quello dell'ultimo arco inserito nel percorso parziale
    peso_corrente = self._grafo[parziale[-1]][vicino]["weight"]
    peso_precedente = self._grafo[parziale[-2]][parziale[-1]]["weight"]
    if vicino not in parziale and peso_corrente < peso_precedente:
        return True
    return False


def peso(self, parziale):
    # calcolo il peso della lista parziale per ogni arco
    peso = 0
    for i in range(0, len(parziale) - 1):
        peso += self._grafo[parziale[i]][parziale[i + 1]['weight']]
    return peso