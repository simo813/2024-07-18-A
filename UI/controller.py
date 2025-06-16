import flet as ft
from UI.view import View
from model.modello import Model


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
        self.model.createGraph(self.view.dd_min_chValue, self.view.dd_max_chValue)


    def handle_dettagli(self, e):
        pass


    def handle_path(self, e):
        pass