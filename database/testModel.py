import networkx as nx

from model.modello import Model

model = Model()
model.createGraph(3,7)
print(model.graph.number_of_nodes())
print(model.graph.number_of_edges())

