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
        else:
            print(f"Hubo un error en el request ({response.status_code})")

    def getMenor(self):
        return self.minDeaths

    def getMayor(self):
        return self.maxDeaths

    def topmenor10(self):
        print("Top 10 ranking de menos muertos")
        for i in range(0,10):
            print(self.listaAPI[i])

    def topmayor10(self):
        print("Top 10 ranking de mas muertos")
        for i in range(0,10):
            print(self.rlistaAPI[i])

    def entre_rangos(self,min=-1,max=-1):
        if min == -1:
            min = self.minDeaths
        if max == -1:
            max = self.maxDeaths

        listaTemp = list()
        for i in self.listaAPI:
            if i[0] >= min and i[0] <= max:
                listaTemp.append(i)
        
        for i in listaTemp:
            print(i)

    def askPais(self,pais):
        print(pais)
