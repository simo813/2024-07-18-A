from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.DAO = DAO()
        self.listGenes = self.DAO.get_all_genes()
        self.idMapGenes = {}
        for g in self.listGenes:
            self.idMapGenes[g.GeneID] = g
        self.graph = None

    def passGenes(self):
        return self.listGenes, self.idMapGenes

    def passChromosome(self):
        listChromosome = self.DAO.get_all_chromosoma()
        return listChromosome

    def createGraph(self, minChromosome, maxChromosome):
        self.graph = nx.DiGraph()
        listNodes = self.DAO.getNodes(minChromosome, maxChromosome)
        self.graph.add_nodes_from(listNodes)
        listEdges = self.DAO.getEdges(minChromosome, maxChromosome)
        for edge in listEdges:
            if self.idMapGenes[edge[0]].Chromosome < self.idMapGenes[edge[1]].Chromosome:
                self.graph.add_edge(edge[0], edge[1], weight=edge[2])
            elif self.idMapGenes[edge[1]].Chromosome < self.idMapGenes[edge[0]].Chromosome:
                self.graph.add_edge(edge[1], edge[0], weight=edge[2])
            else:
                self.graph.add_edge(edge[0], edge[1], weight=edge[2])
                self.graph.add_edge(edge[1], edge[0], weight=edge[2])

