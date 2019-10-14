from networkx.algorithms import bipartite
import networkx as nx
from matplotlib import pyplot as plt
from bipartite_graph import BipartiteGraph
from graph_edge import Edge
from graph_node import Node


bipartite_graph = BipartiteGraph([Node(1), Node(2), Node(3)], [Node('A'), Node('B'), Node('C')], [Edge(1, 'A', 5), Edge(1, 'B', 4), Edge(2, 'C', 9), Edge(3, 'C', 2), Edge(2, 'B', 2), Edge(3, 'A', 10)])
nx_graph = bipartite_graph.get_nx_graph()
nx_matching_graph = bipartite_graph.get_maximum_weighted_matching(maximum_cardinality=True)

# B = nx.Graph()
# # Add nodes
# B.add_nodes_from(['A','B','C','D','E'], bipartite=0)
# B.add_nodes_from([1,2,3,4], bipartite=1)
# # Add edges
# B.add_edges_from([('A',1),('B',1),('C',1),('C',3),('D',2),('E',3),('E',4)])


# X, Y = ['A','B','C','D','E'], [1, 2, 3, 4]
# pos = dict()
# pos.update((n, (1, i)) for i, n in enumerate(X)) # put nodes from X at x=1
# pos.update((n, (2, i)) for i, n in enumerate(Y)) # put nodes from Y at x=2
pos1 = nx.get_node_attributes(nx_graph, 'pos')
pos2 = nx.get_node_attributes(nx_matching_graph, 'pos')
labels = nx.get_edge_attributes(nx_graph, 'weight')
plt.figure(1)
nx.draw(nx_graph, pos=pos1)
nx.draw_networkx_edge_labels(nx_graph, pos1, edge_labels=labels)
plt.figure(2)
nx.draw(nx_matching_graph, pos=pos2)
plt.show()

# pos = nx.get_node_attributes(B, 'pos')
# nx.draw(B)
# plt.show()


# import networkx as nx
# from networkx import bipartite    

# def plotGraph(graph,ax,title):    
#     pos=[(ii[1],ii[0]) for ii in graph.nodes()]
#     pos_dict=dict(zip(graph.nodes(),pos))
#     nx.draw(graph,pos=pos_dict,ax=ax,with_labels=True)
#     ax.set_title(title)
#     return   

# if __name__=='__main__':    
#     #---------------Construct the graph---------------
#     g=nx.Graph()
#     edges=[
#             [(1,0), (0,0)],
#             [(1,0), (0,1)],
#             [(1,0), (0,2)],
#             [(1,1), (0,0)],
#             [(1,2), (0,2)],
#             [(1,2), (0,5)],
#             [(1,3), (0,2)],
#             [(1,3), (0,3)],
#             [(1,4), (0,3)],
#             [(1,5), (0,2)],
#             [(1,5), (0,4)],
#             [(1,5), (0,6)],
#             [(1,6), (0,1)],
#             [(1,6), (0,4)],
#             [(1,6), (0,6)]
#             ]

#     for ii in edges:
#         g.add_node(ii[0],bipartite=0)
#         g.add_node(ii[1],bipartite=1)

#     g.add_edges_from(edges)

#     #---------------Use maximal_matching---------------
#     match=nx.maximal_matching(g)    
#     g_match=nx.Graph()
#     for ii in match:
#         g_match.add_edge(ii[0],ii[1])

#     #----------Use bipartite.maximum_matching----------
#     match2=bipartite.maximum_matching(g)    
#     g_match2=nx.Graph()
#     for kk,vv in match2.items():
#         g_match2.add_edge(kk,vv)

#     #-----------------------Plot-----------------------
#     import matplotlib.pyplot as plt
#     fig=plt.figure(figsize=(10,8))

#     ax1=fig.add_subplot(2,2,1)
#     plotGraph(g,ax1,'Graph')

#     ax2=fig.add_subplot(2,2,2)
#     plotGraph(g_match,ax2,'nx.maximal_matching()')

#     ax3=fig.add_subplot(2,2,3)
#     plotGraph(g_match2,ax3,'bipartite.maximum_matching()')

#     plt.show()
