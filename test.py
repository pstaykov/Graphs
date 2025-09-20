from simpleGraph import simpleGraph

G = simpleGraph()
G.randomGraph(6, 0.1)

print("Random Graph:", G.graph)
print("Connected?", G.connectedGraph())
print("Components:", G.connectedComponents())
