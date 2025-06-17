import flet as ft
from UI.view import View
from model.modello import Model
import networkx as nx


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model

    def fillDD(self):
        listChromosome = self.model.passChromosome()
        for chromosome in listChromosome:
            self.view.dd_min_ch.options.append(ft.dropdown.Option(key=chromosome, text=chromosome))
            self.view.dd_max_ch.options.append(ft.dropdown.Option(key=chromosome, text=chromosome))
        self.view.update_page()

    def handle_graph(self, e):
        self.view.txt_result1.clean()
        if self.view.dd_min_chValue is None or self.view.dd_max_chValue is None:
            self.view.txt_result1.controls.append(
                ft.Text(f"Seleziona i valori"))
        else:
            self.model.createGraph(int(self.view.dd_min_chValue), int(self.view.dd_max_chValue))
            graph = self.model.graph
            self.view.txt_result1.controls.append(
                    ft.Text(f"Creato grafo con {graph.number_of_nodes()} nodi e {graph.number_of_edges()} archi"))
            listOfNodesAndTotalWeight = []
            for source in graph.nodes():
                sumEdges = 0
                sumEdgesWeight = 0
                for u, v, data in graph.out_edges(source, data=True): #attenzine
                    sumEdges += 1
                    sumEdgesWeight += data.get('weight', 1)
                listOfNodesAndTotalWeight.append((source, sumEdges, sumEdgesWeight))
            sortedListOfNodesAndTotalWeight = sorted(listOfNodesAndTotalWeight, key=lambda x: x[1], reverse=True)
            for i in range(0, 5):
                self.view.txt_result1.controls.append(
                    ft.Text(f"{sortedListOfNodesAndTotalWeight[i][0].__str__()} | {sortedListOfNodesAndTotalWeight[i][1]} | {sortedListOfNodesAndTotalWeight[i][2]}"))


        self.view.update_page()



    def handle_dettagli(self, e):
        pass


    def handle_path(self, e):
        pass