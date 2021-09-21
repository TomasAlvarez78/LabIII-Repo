from os import initgroups
import requests
from config import *
class API():
    
    def __init__(self) -> None:
        self.listaAPI = list()
        self.rlistaAPI = list()
        self.minDeaths = 0
        self.maxDeaths = 0

    def requestAPI(self):
        print("Comienza la API")
        response = requests.get(api_link)
        if response.status_code == 200:
            respuesta = response.json()
            muertes = dict()
            for pais in respuesta['Countries']:
                muertes.setdefault(pais['TotalDeaths'],[]).append(pais['Country'])

            self.listaAPI = sorted(muertes.items())
            self.rlistaAPI = list(reversed(self.listaAPI))
            self.minDeaths = self.listaAPI[0][0]
            self.maxDeaths = self.listaAPI[len(self.listaAPI)-1][0]
            print(f"Menor cant de muertes: {self.minDeaths}")
            print(f"Mayor cant de muertes: {self.maxDeaths}")
        else:
            print(f"Hubo un error en el request ({response.status_code})")

    def topmenor10(self):
        print("Top 10 ranking de menos muertos")
        for i in range(0,10):
            print(self.listaAPI[i])

    def topmayor10(self):
        print("Top 10 ranking de mas muertos")
        for i in range(0,10):
            print(self.rlistaAPI[i])
