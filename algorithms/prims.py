# -*- coding: utf-8 -*-
import networkx as nx
from  functions.drawings import draw_subtree
from functions.prims_functions import cost, possible_prims_edges


def prims_algorithm(G, starting_node, draw = False, attrib = False):
    
    T = nx.Graph()
    T.add_node(starting_node)
    
    if draw == True:
        draw_subtree(G, T)
        
    while set(T.nodes()) != set(G.nodes()):
        e = min_prims_edge(G, T)
        T.add_edge(e[0], e[1], weight = cost(G, e))
        if draw == True:
            draw_subtree(G, T)
            
    if attrib == True:
        total_cost = sum(cost(G, e) for e in T.edges())
        print('-----------------   Properties of the tree T-----------')
        print('-------------------------------------------------------')
        print(f'V(T) = {list(T.nodes())}')
        print(f'E(T) = {list(T.edges())}')
        print(f'Total Cost = {Total_cost}')
        print('--------------------------------------------------------')
        
    return T

def draw_subtree(G, T):
    pos = nx.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = labels,)
    nx.draw_networkx_edges(G, pos,
                            edgelist=T.edges(),
                            width=8, alpha=0.5,
                            edge_color='r',)
    nx.draw_networkx_nodes(G,
                           pos,
                           nodelist=T.nodes(),
                           node_color='r',
                           node_size=500,
                           alpha=0.8)
    plt.show()