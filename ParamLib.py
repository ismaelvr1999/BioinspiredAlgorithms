#Villalpando Rivera Ismael
#Cutonala. ALgoritmos Bioinspirados. 2023-B
from PSLib import AlgBio
import json
import random
import math
class ParamLib:
    def __init__(self):
        pass
#-----------Algoritmo genetico -----------
    class ParamAlgGenetico:

        def __init__(self,Algoritmo,Iteraciones,tasaMutacion) -> None:
            self.MasApt = ()
            self.Individuos = []
            self.Nueva_Generacion = []
            self.tasa_mutacion = tasaMutacion
            self.AlgoritmoGen = Algoritmo
            self.Iteraciones = Iteraciones

        def funObjGenetico(self,Individuos):
            Aptitud = {}
            for x in range(0,30):
                eval = pow(Individuos[x],2)+2
                Aptitud[ eval ] = Individuos[x]

            mayor =max(Aptitud)
            self.MasApt = (Aptitud[mayor],mayor)
            print(Aptitud)
            print("Mas apto = Evaluacion: "+str(self.MasApt[1])+" Genotipo: "+str(self.MasApt[0]))
            return Aptitud

        def GenerarGeneraciones(self):
            print("Poblacion inicial")
            self.Individuos = self.AlgoritmoGen.GenerarInd()
            Poblacion = self.Individuos.copy()
            print(Poblacion)
            self.funObjGenetico(Poblacion)

            for x in range(self.Iteraciones):
                print(f"--------------Generacion {x}-------------")
                self.Nueva_Generacion = self.AlgoritmoGen.Cruza(Poblacion,self.tasa_mutacion)
                print(self.Nueva_Generacion)
                self.funObjGenetico(self.Nueva_Generacion)
                Poblacion = self.Nueva_Generacion.copy()
#  -----------Algoritmo de colonia de hormigas -----------
    class ParamAlgAntColony:
        def __init__(self, graph):
            self.graph = graph

        def calcular_distancia_recorrido(self, tour):
            distance = 0

            for i in range(len(tour) - 1):
                from_city = tour[i]
                to_city = tour[i + 1]
                distance += self.graph[from_city][to_city]
            return distance
#  -----------Algoritmo Recocido Simulado -----------
    class ParamAlgRecocidoSimulado:

        def __init__(self,ciudades):
            self.ciudades = ciudades

        def distancia(self, ciudad1, ciudad2):
            x1 =ciudad1[0]
            y1 = ciudad1[1]
            x2 = ciudad2[0]
            y2 = ciudad2[1]
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        def costo_total(self, solucion):
            costo = 0
            for i in range(len(solucion)):
                costo += self.distancia(self.ciudades[solucion[i]], self.ciudades[solucion[(i + 1) % len(solucion)]])
            return costo
#  -----------Algoritmo Sistema inmunologico  -----------
    class ParamAlgSistemaInmunologico:
        def __init__(self) -> None:
            pass
        def calcular_afinidad(self, antigeno,anticuerpos,longitud_anticuerpo):
            afinidades = []
            for anticuerpo in anticuerpos:
                afinidad = sum([1 for i in range(longitud_anticuerpo) if anticuerpo[i] == antigeno[i]])
                afinidades.append(afinidad)
            print(afinidades)
            return afinidades

    def leerJSON(self,NombreArch):
        with open(NombreArch) as archivo:
            datos = json.load(archivo)
        return datos
    

parametros = ParamLib()
datos = parametros.leerJSON("Conf.json")

# -----------Prueba Algoritmo genetico -----------     
# AlgGen = AlgBio.AlgGen()
# tasaMutacion = datos["AlgGen"]["TasaMutacion"]
# iteraciones = datos["AlgGen"]["Iteraciones"]
# obj = ParamLib.ParamAlgGenetico(AlgGen,iteraciones,tasaMutacion)
# obj.GenerarGeneraciones()


#  -----------Prueba Algoritmo de colonia de hormigas -----------
# graph = [
#     [0, 5, 2, 10],
#     [5, 0, 6, 3],
#     [2, 6, 0, 8],
#     [10, 3, 8, 0]
# ]
# num_ants = datos["AlgAntColony"]["NumAnts"]
# Iteraciones = datos["AlgAntColony"]["Iteraciones"]
# tasa_evaporacion = datos["AlgAntColony"]["TasaEvaporacion"]
# alpha = datos["AlgAntColony"]["Alpha"]
# beta = datos["AlgAntColony"]["Beta"]


# funcionObjetivo = ParamLib.ParamAlgAntColony(graph)
# colony = AlgBio.AntColony(num_ants=num_ants, num_iteraciones=Iteraciones, tasa_evaporacion_feromona=tasa_evaporacion , alpha=alpha, beta=beta, graph=graph,funcion_objetivo=funcionObjetivo)
# best_tour, best_distance = colony.run()
# print(f"Mejor distancia encontrada: {best_distance}")
# print(f"Mejor camino encontrado: {best_tour}")

# ----------- Prueba Recocido Simulado-------------

# ciudades = [(0, 0), (1, 2), (3, 1), (2, 3), (5, 2)]  # Coordenadas de las ciudades
# temperatura_inicial = datos["AlgRecocidoSimulado"]["TempIni"]
# factor_enfriamiento = datos["AlgRecocidoSimulado"]["FactEnfr"]
# iteraciones = datos["AlgRecocidoSimulado"]["Iteraciones"]
# funcObj = ParamLib.ParamAlgRecocidoSimulado(ciudades)

# recocido = AlgBio.RecocidoSimulado(ciudades, temperatura_inicial, factor_enfriamiento, iteraciones,funcObj)
# mejor_solucion, mejor_costo = recocido.recocido_simulado()
# print("Mejor solución encontrada:", mejor_solucion)
# print("Costo de la mejor solución:", mejor_costo)

# ----------- Prueba Algoritmo Sistema inmunologico-------------

num_anticuerpos = 10
longitud_anticuerpo = 8
functObt = ParamLib.ParamAlgSistemaInmunologico();
sistema = AlgBio.SistemaInmunologico(num_anticuerpos, longitud_anticuerpo,functObt)
antigeno = [1, 0, 1, 0, 1, 0, 1, 0]
seleccionados = sistema.seleccionar_anticuerpos(antigeno, num_anticuerpos // 2)
print("Anticuerpos seleccionados:")
for anticuerpo in seleccionados:
    print(anticuerpo)

probabilidad_mutacion = 0.1
sistema.mutar_anticuerpos(probabilidad_mutacion)
print("\nAnticuerpos después de la mutación:")
for anticuerpo in sistema.anticuerpos:
    print(anticuerpo)




