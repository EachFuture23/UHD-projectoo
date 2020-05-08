# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def show_weighted_graph(G):
    pos = nx.planar_layout(G)
    nx.draw(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_network_edge_labels(G,
                                pos,
                                edge_labels = labels)
    plt.show()
    
def draw_subtree(G, T):
    pos = nx.planar_layout(G)
    nx.draw_neworkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_network_edge_labels(G,
                                pos,
                                edeg_labels = labels,)
    nx.draw_neworkx_edges(G,pos,
                                edeglist=T.edges(),
                                width=8, alpha=0.5,
                                edge_color= labels,)
    nx.draw_networkx_nodes(G,
                           pos,
                           nodelist=T.nodes(),
                           node_color='r', 
                           node_size=500,
                           alpha=0.8)
    plt.show