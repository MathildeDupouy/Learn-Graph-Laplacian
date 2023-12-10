# Context

This code was written as part of the final project for the course Geometric Data Analysis of the Master MVA (2023) by Adrien RAMANANA RAHARY and Mathilde DUPOUY.

We conducted several experiments to evaluate how the smoothness of a signal on a graph affects its reconstruction through a graph signal processing reconstruction approach.

The solver used to compute an underlying graph given signal samples is an adaptation of the code available here: https://github.com/TheShadow29/Learn-Graph-Laplacian?fbclid=IwAR0117ZvUag6RAW8p6sJOujPdNarhIZRHyF12eZ8KG4HhS_zWP7yXs0DQAc

This code is an implementation of the paper  Learning Laplacian Matrix in Smooth Graph Signal Representations 
https://arxiv.org/pdf/1406.7842.pdf

The original code can be found on the authors website [web.media.mit.edu/~xdong/pub.html](https://web.media.mit.edu/~xdong/pub.html)

Besides, we make use of the Gromov-Wasserstein distance to compute distance between graphs and have used the implementation available here: https://github.com/tvayer/FGW

THis repositorie contains the original scripts : code/solver.py and code/data_loader.py. We proposed another script to generate graph with a heat diffusion process (synthetic_graphs) and different tests were conducted on three different notebooks. The notebook code/main.ipynb contains in particular the main experiments discussed in our report.
