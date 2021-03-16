import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities



def get_modularity(nx_graph):
    communities_list = list(greedy_modularity_communities(nx_graph))
    adjacency = nx.adjacency_matrix(nx_graph).todense().getA()
    m = len(nx_graph.edges())
    suma = 0
    grados = {}
    for i in range(len(adjacency)):
        grado = 0
        for elem in adjacency[i]:
            grado += elem
        grados[i] = grado
    for i in range(len(adjacency)):
        for j in range(len(adjacency)):
            ki = grados[i]
            kj = grados[j]
            delta = 0
            for comunidad in communities_list:
                if i in list(comunidad) and j in list(comunidad):
                    delta = 1
            A = adjacency[i][j]
            suma += delta * (A - ki * kj / (2 * m))
    modularidad = suma / (2 * m)
    return modularidad


def get_cant_comunities(nx_graph):
    communities_list = list(greedy_modularity_communities(nx_graph))
    cant_communities = len(communities_list)
    return cant_communities