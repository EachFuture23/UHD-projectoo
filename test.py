import networkx as nx
from functions.drawings import show_weighted_graph
from functions.drawings import draw_subtree
from functions.prims_functions import *


'''G = nx.Graph()

G.add_edge(0, 1, weight = 1.0)
G.add_edge(0, 2, weight = 1.0)
G.add_edge(1, 2, weight = 4.0)
G.add_edge(2, 3, weight = 4.0)

show_weighted_graph(G)
nx.draw(G)'''


G = nx.read_weighted_edgelist('data/G8.txt',
                              nodetype = int)
T = nx.Graph()
T.add_node(2)
 

print('Iteration 1')
for e in set((G.edges())) - set(T.edges()):
     for v in T.nodes():
         if v in e:
             print(f'Edge {e} has cost {cost(G, e)}')
                       
             
print('')             
T. add_edge(0, 2, weight = cost(G, (0,2)))

draw_subtree(G, T)



print('Iteration 2')
for e in set((G.edges())) - set(T.edges()):
    for v in T.nodes():
         if v in e:
             print(f'Edge {e} has cost {cost(G, e)}')
             
print('')             
T. add_edge(0, 1, weight = cost(G, (0,1)))

draw_subtree(G, T)
             
             
             
print('Iteration 3')
for e in set((G.edges())) - set(T.edges()):
    for v in T.nodes():
         if v in e:
             print(f'Edge {e} has cost {cost(G, e)}')
                         
print('')             
