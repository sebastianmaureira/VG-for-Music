import from_nx as medidas
import networkx as nx
import numpy as np
from threading import Lock, Thread


class VGAnalyzer:
    def __init__(self, nombre, link_list):
        
        self.lock_medidas = Lock()

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
        # Create Threads
        threads = []
        t0 = Thread(target=self.add_nodos)
        threads.append(t0)
        t1 = Thread(target=self.add_enlaces)
        threads.append(t1)
        t2 = Thread(target=self.add_clust)
        threads.append(t2)
        t3 = Thread(target=self.add_av_degree)
        threads.append(t3)
        t4 = Thread(target=self.add_radius)
        threads.append(t4)
        t5 = Thread(target=self.add_dia)
        threads.append(t5)
        t6 = Thread(target=self.add_com)
        threads.append(t6)
        t7 = Thread(target=self.add_modularidad)
        threads.append(t7)

        #Start threads
        for thread in threads:
            thread.start()

        #Join threads
        for thread in threads:
            thread.join()


    def add_nodos(self):
        nodos = nx.number_of_nodes(self.graph)
        with self.lock_medidas:
            self.measures["Cant. nodos"] = nodos
    
    def add_enlaces(self):
        enlaces = nx.number_of_edges(self.graph)
        with self.lock_medidas:
            self.measures["Cant. enlaces"] = enlaces
    
    def add_clust(self):
        clust = nx.average_clustering(self.graph)
        with self.lock_medidas:
            self.measures["Clusterización promedio"] = clust

    def add_av_degree(self):
        deg = nx.degree_centrality(self.graph)
        count = 0
        suma = 0
        for key in deg:
            count += 1
            suma += deg[key]
        with self.lock_medidas:
            self.measures["Grado promedio"] = suma / count
    
    def add_radius(self):
        with self.lock_medidas:
            self.measures["Radio"] = nx.radius(self.graph)
    
    def add_dia(self):
        with self.lock_medidas:
            self.measures["Diametro"] = nx.diameter(self.graph)

    
    def add_com(self):
        coms = medidas.get_cant_comunities(self.graph)
        with self.lock_medidas:
            self.measures["Cant. Comunidades"] = coms
    
    def add_modularidad(self):
        mod = medidas.get_modularity(self.graph)
        with self.lock_medidas:
            self.measures["Modularidad"] = mod

if __name__ == "__main__":

    G = nx.path_graph(6)  # or DiGraph, MultiGraph, MultiDiGraph, etc
    G.degree[0]  # node 0 has degree 1

    a = list(G.degree([0, 1, 2,3, 4, 5]))
    print(a)
    print(nx.degree_centrality(G))