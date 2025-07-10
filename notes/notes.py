# connettività: https://networkx.org/documentation/stable/reference/algorithms/component.html#connectivity
# - Componente connessa (iTunes: grafo non orientato, non pesato, componente connessa, ricorsione…)
#     - nx.number_connected_components(self._grafo) => dice solo quante componenti connesse ci sono nel grafo
#     - nx.node_connected_component(G, n) => restituisce un set di nodi, non una lista.
#           Ottengo l’insieme di nodi appartenenti alla stessa componente connessa del nodo n nel grafo G.
#           In pratica, ti dice "tutti i nodi che sono connessi a n" (cioè, tutti quelli raggiungibili da n).
#           Funziona SOLO per grafi NON orientati. Il nodo che passo come parametro è sempre compreso nel
#           set che viene restituito alla fine.
#     - nx.node_weakly_connected_component(G, n). Si applica a grafi orientati (directed).
#           Restituisce tutti i nodi che sono raggiungibili da n, o da cui n è raggiungibile,
#           ignorando la direzione degli archi. È come se rendessimo il grafo non orientato e
#           cercassimo la componente connessa. Per cui anche se tra due nodi c’è solo un arco entrante o uscente,
#           sono comunque considerati connessi.
#     - nx.node_strongly_connected_component(G, n). Si applica a grafi orientati (directed).
#           Restituisce tutti i nodi v tali che:
    #         - Esiste un cammino diretto da A a v, e
    #         - Esiste un cammino diretto da v a A.
    #         - Queste due condizioni devono essere verificate entrambe! v apparterrà alla componente connessa
    #           di A anche se nel cammino tra A e v e tra v e A ci sono altri nodi intermedi. Anche questi nodi
    #           intermedi saranno nella componente connessa.
    #         - È quindi una componente fortemente connessa: ogni nodo è raggiungibile da ogni altro seguendo
    #           le direzioni degli archi. Mi restituisce i nodi che costruiscono un ciclo che parte da A e ritorna in A.
    #           Se A è collegato ad altri nodi ma non in modo ciclico mi restituisce solo A!


# - Vicini:
#     * for n in G: scorre il grafico.
#     * for nbr in G[n]: scorre i vicini.

# - Cammino minimo sul grafo: https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
#
#   l'algoritmo di Dijkstra per trovare il percorso pesato più breve, esempio:
#     G = nx.Graph()
#     e = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]
#     G.add_weighted_edges_from(e)
#     print(nx.dijkstra_path(G, 'a', 'd'))
#   restituisce:
#     ['a', 'c', 'd']


# - funzioni un po' utili tipo degree o density: https://networkx.org/documentation/stable/reference/functions.html
