# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 01:30:16 2023

@author: mathi
"""
import numpy as np
import matplotlib.pyplot as plt
from data_loader import synthetic_data_gen
import pdb
from cvxopt import matrix, solvers
import networkx as nx
from tqdm import tqdm

def create_graph_from_laplacian(L) :
    G=nx.Graph()
    for i in range(len(L)) :
        G.add_node(i)
    for i in range(len(L)) :
        for j in range(i+1, len(L)) :
            if abs(L[i][j]) > 1e-2 :
                G.add_edge(i, j)
                G[i][j]['weight'] = -L[i][j]
    return G