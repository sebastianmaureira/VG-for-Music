import from_nx as medidas
import networkx as nx
import numpy as np


class VGAnalyzer:
    def __init__(self, nombre, link_list):
        self.nombre = nombre
        self.link_list = link_list
        self.nodes = len(self.link_list)
        self.crear_grafo()
        self.measures = dict()
    
    def crear_grafo(self):
        self.adjacency_matrix = np.zeros((self.nodes, self.nodes))
        self.directed_adj_matrix = np.zeros((self.nodes, self.nodes))
        for link in self.link_list:
            self.adjacency_matrix[link[0] - 1, link[1] - 1]
            self.directed_adj_matrix[link[0] - 1, link[1] - 1]
            self.adjacency_matrix[link[1] - 1, link[0] - 1]
        self.graph = nx.from_numpy_matrix(self.adjacency_matrix)
        self.directed_graph = nx.from_numpy_matrix(self.directed_adj_matrix)
        self.graph.remove_nodes_from(list(nx.isolates(self.graph)))
        self.directed_graph.remove_nodes_from(list(nx.isolates(self.directed_graph)))

    def get_measures(self):
        self.measures["Cant. nodos"] = nx.number_of_nodes(self.graph)
        self.measures["Cant. enlaces"] = nx.number_of_edges(self.graph)
        self.measures["Clusterización promedio"] = nx.average_clustering(self.graph)
        deg = nx.degree_centrality(self.graph)
        count = 0
        suma = 0
        for key in deg:
            count += 1
            suma += deg[key]
        self.measures["Grado promedio"] = suma / count
        self.measures["Radio"] = nx.radius(self.graph)
        self.measures["Diametro"] = nx.diameter(self.graph)
        self.measures["Cant. Comunidades"] = medidas.get_cant_comunities(self.graph)
        self.measures["Modularidad"] = medidas.get_modularity(self.graph)

if __name__ == "__main__":

    G = nx.path_graph(6)  # or DiGraph, MultiGraph, MultiDiGraph, etc
    G.degree[0]  # node 0 has degree 1

    a = list(G.degree([0, 1, 2,3, 4, 5]))
    print(a)
    print(nx.degree_centrality(G))