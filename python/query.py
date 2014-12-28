#! /usr/bin/python2.7
__author__ = 'louisjyli'
import networkx as nx
import sys

argv = sys.argv
# print argv

G = nx.read_edgelist(argv[1],delimiter="\t")
query = argv[2].split(",")
# print query
setSubNodes = set()
min_len = float('Inf')
for i in range(len(query)-1):
    for j in range(len(query) - i - 1):


        u = query[i]
        v = query[j+i+1]

#         print(str(i) + ', ' + str(i+j+1) + ', ' + u + ', ' + v)
        setSubNodes |= {u, v}
        try:
            path = nx.shortest_path(G, u, v)
            setSubNodes |= set(path)
            for node in path:
                setSubNodes |= nx.neighbors(G, node)
            if len(path) < min_len:
                min_len = len(path)
        except:
            pass

subG = G.subgraph(setSubNodes)
# setSubNodes |= set(subG.nodes())
#subG=G.subgraph(sys.argv)
print min_len
with open(argv[3], "w") as f:
    for i in subG.edges():
        f.write(str(i[0]) + "\t" + str(i[1]) + "\n")
# query=sys.argv
# 
# # G = nx.Graph()
# # G.add_path([0,1,2,3])
# 
# print('Argument List:'+str(query))
# 
# subG=G.subgraph(query)
# #subG=G.subgraph(sys.argv)
# subG.edges()
