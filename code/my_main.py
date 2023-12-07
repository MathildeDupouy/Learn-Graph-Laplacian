# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 01:28:17 2023

@author: mathi
"""
import numpy as np
import matplotlib.pyplot as plt
from data_loader import synthetic_data_gen
import pdb
from cvxopt import matrix, solvers
import networkx as nx
from tqdm import tqdm

from main import *
from utilities import create_graph_from_laplacian

solvers.options['show_progress'] = False
syn = synthetic_data_gen(10)
num_nodes = syn.num_vertices

np.random.seed(3)
graph_signals_er, graph_signals_ba, graph_signals_rand = syn.get_graph_signals()
L_er, Y_er = gl_sig_model(graph_signals_er, 1000, syn.alpha_er, syn.beta_er)
L_ba, Y_ba = gl_sig_model(graph_signals_ba, 1000, syn.alpha_er, syn.beta_er)
L_rnd, Y_rnd = gl_sig_model(graph_signals_rand, 1000, syn.alpha_rnd, syn.beta_rnd)

L_er_gt = nx.laplacian_matrix(syn.er_graph)
L_ba_gt = nx.laplacian_matrix(syn.ba_graph)
L_rnd_gt = nx.laplacian_matrix(syn.random_graph)

gt_graph = syn.er_graph
est_graph = create_graph_from_laplacian(L_er)
subax1 = plt.subplot(121)
nx.draw(syn.er_graph, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
# nx.draw_shell(syn.er_graph, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

subax2 = plt.subplot(122)
nx.draw(est_graph, with_labels=True, font_weight='bold')