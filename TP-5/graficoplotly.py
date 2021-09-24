import plotly.graph_objects as go
# from plotly import graph_objs as go
from api import *

class GraficoBarra():

    def __init__(self) -> None:
        self.covidAPI = API()

    def requestAPI(self):
        self.covidAPI.requestAPI()

    def graficarMenor(self):
        lista = self.covidAPI.topmenor10()
        self.graficarLista(lista)

    def graficarMayor(self):
        lista = self.covidAPI.topmayor10()
        self.graficarLista(lista)

    def graficarLista(self,lista):
        fig = go.Figure([go.Bar(x=lista[1], y=lista[0])])
        fig.show()