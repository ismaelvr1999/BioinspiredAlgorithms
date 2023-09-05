#Villalpando Rivera Ismael
#Cutonala. ALgoritmos Bioinspirados. 2023-B
from PSLib import AlgBio
# import numpy as np
import random
class ParamLib:
    def __init__(self) -> None:
        pass

    class ParamAlg:

        def __init__(self,Algoritmo) -> None:
            self.MasApt = ()
            self.Individuos = []
            self.Nueva_Generacion = []
            self.tasa_mutacion = 0.1
            self.AlgoritmoGen = Algoritmo

        def funObj(self,Individuos):
            Aptitud = {}
            for x in range(0,30):
                eval = pow(Individuos[x],2)+2
                Aptitud[ eval ] = Individuos[x]

            mayor =max(Aptitud)
            self.MasApt = (Aptitud[mayor],mayor)
            print(Aptitud)
            print("Mas apto = Evaluacion: "+str(self.MasApt[1])+" Genotipo: "+str(self.MasApt[0]))
            return Aptitud

        def run(self):
            print("Primera generacion")
            self.Individuos = self.AlgoritmoGen.GenerarInd()
            print(self.Individuos)
            self.funObj(self.Individuos)
            print("------------Cruza---------------")
            self.Nueva_Generacion = self.AlgoritmoGen.Cruza(self.Individuos,self.tasa_mutacion)
            print("--------------Nueva generacion-------------")
            print(self.Nueva_Generacion)
            self.funObj(self.Nueva_Generacion)

    class TSPObjectiveFunction:
        def __init__(self, graph):
            self.graph = graph

        def evaluate(self, tour):
            distance = 0

            for i in range(len(tour) - 1):
                from_city = tour[i]
                to_city = tour[i + 1]
                distance += self.graph[from_city][to_city]

            return distance
        
# Prueba algoritmo genetico       
# AlgGen = AlgBio.AlgGen()
# obj = ParamLib.ParamAlg(AlgGen)
# obj.run()


# prueba Algoritmo de colonia de hormigas
graph = [
    [0, 12, 4, 7],
    [12, 0, 8, 6],
    [4, 8, 0, 11],
    [7, 6, 11, 0]
]


objective_function = ParamLib.TSPObjectiveFunction(graph)
colony = AlgBio.AntColony(num_ants=10, num_iteraciones=50, tasa_evaporacion_feromona=0.2, alpha=1, beta=1, graph=graph)


best_tour, best_distance = colony.run()

print(f"Mejor distancia encontrada: {best_distance}")
print(f"Mejor camino encontrado: {best_tour}")



