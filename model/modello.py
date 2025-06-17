from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.DAO = DAO()
        self.listGenes = self.DAO.get_all_genes()
        self.idMapGenes = {}
        for g in self.listGenes:
            identity = g.GeneID + g.Function
            self.idMapGenes[identity] = g
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
            gene1 = self.idMapGenes[edge[0] + edge[1]]
            gene2 = self.idMapGenes[edge[2] + edge[3]]
            if  gene1.Chromosome < gene2.Chromosome:
                self.graph.add_edge(gene1, gene2, weight=edge[4])
            elif gene1.Chromosome > gene2.Chromosome:
                self.graph.add_edge(gene2, gene1, weight=edge[4])
            else:
                self.graph.add_edge(gene1, gene2, weight=edge[4])
                self.graph.add_edge(gene2, gene1, weight=edge[4])

