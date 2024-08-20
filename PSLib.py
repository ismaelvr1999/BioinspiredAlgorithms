#Villalpando Rivera Ismael
import random
import math
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
class AlgBio:

    def __init__(self) -> None:
        pass
#-----------Genetic Algorithm -----------
    class AlgGen:

        def __init__(self) -> None:
            pass
        def GenerarInd(self):
            Individuos = [random.randint(0,15) for x in range(0,30)]

            return Individuos
        
        def Cruza(self,Individuos,tasa_mutacion):
            nuevaGeneracion = [] 
            for x in range(0,int(len(Individuos)/2)):
                IndRand1 = random.randint(0,29)
                IndRand2 = random.randint(0,29)
                PuntoCruzaR = random.randint(0,3)
                
                Padre1 = Individuos[IndRand1]
                Padre2 = Individuos[IndRand2]
                
                BinPadr1 = str(bin(Padre1))[2:]
                BinPadr2 = str(bin(Padre2))[2:]
                
                BinPadr1 = BinPadr1.zfill(4)
                BinPadr2 = BinPadr2.zfill(4)

                Hijo1 = BinPadr2[:PuntoCruzaR] + BinPadr1[PuntoCruzaR:]
                Hijo2 = BinPadr1[:PuntoCruzaR] +BinPadr2[PuntoCruzaR:]

                MutacionH1 = self.Mutacion(Hijo1,tasa_mutacion)
                MutacionH2 = self.Mutacion(Hijo2,tasa_mutacion)

                nuevaGeneracion.append(int(MutacionH1,2))
                nuevaGeneracion.append(int(MutacionH2,2))
                
            return nuevaGeneracion

        def Mutacion(self,Hijo,tasa_mutacion):
            HijoMutado = list(Hijo)
            for i in range(len(HijoMutado)):
                gen = HijoMutado [i]
                if random.random() < tasa_mutacion:
                    if gen == "0":
                        HijoMutado[i]= "1"
                    else: 
                        HijoMutado[i]= "0"
                    break
            HijoMutadoN =''.join(HijoMutado)
            return HijoMutadoN
#  -----------Ant Colony Algorithm -----------
    class AntColony:
        def __init__(self, num_ants, num_iteraciones, tasa_evaporacion_feromona, alpha, beta, graph,funcion_objetivo):
            self.num_ants = num_ants
            self.num_iteraciones = num_iteraciones
            self.tasa_evaporacion_feromona = tasa_evaporacion_feromona
            self.alpha = alpha
            self.beta = beta
            self.graph = graph
            self.num_ciudades = len(graph)
            self.matriz_feromonas = np.ones((self.num_ciudades, self.num_ciudades))
            self.funcion_objetivo = funcion_objetivo

        def run(self):
            mejor_viaje = None
            mejor_distancia = float('inf')

            for iteration in range(self.num_iteraciones):
                ant_tours = []

                for ant in range(self.num_ants):
                    tour = self.generar_ant_ruta()
                    ant_tours.append((tour, self.funcion_objetivo.calcular_distancia_recorrido(tour)))

                    if ant_tours[-1][1] < mejor_distancia:
                        mejor_viaje = ant_tours[-1][0]
                        mejor_distancia = ant_tours[-1][1]

                self.actualizacion_feromona(ant_tours)
                print(f"Iteracion {iteration}: Mejor distancia = {mejor_distancia}, Mejor viaje = {mejor_viaje}")
    
            return mejor_viaje, mejor_distancia

        def generar_ant_ruta(self):
            tour = [random.randint(0, self.num_ciudades - 1)]
            ciudad_sinvisitar = set(range(self.num_ciudades))

            while ciudad_sinvisitar:
                next_city = self.elegir_siguiente_ciudad(tour[-1], ciudad_sinvisitar)
                tour.append(next_city)
                ciudad_sinvisitar.remove(next_city)

            return tour

        def elegir_siguiente_ciudad(self, ciudad_actual, ciudad_sinvisitar):
            probabilidades = []

            for city in ciudad_sinvisitar:
                pheromone = self.matriz_feromonas[ciudad_actual][city]
                distance = self.graph[ciudad_actual][city]

               
                if distance == 0:
                    probability = 0
                else:
                    probability = (pheromone ** self.alpha) * ((1 / distance) ** self.beta)
                
                probabilidades.append(probability)

            total_probability = sum(probabilidades)
            normalized_probabilidades = [p / total_probability for p in probabilidades]
            ciudad_elegida = np.random.choice(list(ciudad_sinvisitar), p=normalized_probabilidades)

            return ciudad_elegida
        
        def actualizacion_feromona(self, ant_tours):
            self.matriz_feromonas *= (1 - self.tasa_evaporacion_feromona)

            for tour, tour_distance in ant_tours:
                for i in range(len(tour) - 1):
                    from_city = tour[i]
                    to_city = tour[i + 1]
                    self.matriz_feromonas[from_city][to_city] += 1 / tour_distance
                    self.matriz_feromonas[to_city][from_city] += 1 / tour_distance
#  -----------Simulated Annealing Algorithm -----------
    class RecocidoSimulado:
        def __init__(self, ciudades, temperatura_inicial, factor_enfriamiento, iteraciones,funcion_objetivo):
            self.ciudades = ciudades
            self.temperatura_inicial = temperatura_inicial
            self.factor_enfriamiento = factor_enfriamiento
            self.iteraciones = iteraciones
            self.funcion_objetivo = funcion_objetivo

        def recocido_simulado(self):
            n = len(self.ciudades)
            mejor_solucion = list(range(n))  
            mejor_costo = self.funcion_objetivo.costo_total(mejor_solucion)
            temperatura_actual = self.temperatura_inicial

            for i in range(self.iteraciones):
               
                solucion_vecina = mejor_solucion.copy()
                j, k = random.sample(range(n), 2)
                solucion_vecina[j], solucion_vecina[k] = solucion_vecina[k], solucion_vecina[j]

                costo_vecino = self.funcion_objetivo.costo_total(solucion_vecina)

                
                if costo_vecino < mejor_costo or random.random() < math.exp((mejor_costo - costo_vecino) / temperatura_actual):
                    mejor_solucion = solucion_vecina
                    mejor_costo = costo_vecino

               
                temperatura_actual *= self.factor_enfriamiento

            return mejor_solucion, mejor_costo
#  -----------Immune System Algorithm -----------
    class SistemaInmunologico:
        def __init__(self, num_anticuerpos, longitud_anticuerpo,functObj,antigeno,probabilidad_mutacion,iteraciones):
            self.num_anticuerpos = num_anticuerpos
            self.longitud_anticuerpo = longitud_anticuerpo
            self.anticuerpos = self.generar_anticuerpos()
            self.functObj = functObj
            self.antigeno = antigeno
            self.probabilidad_mutacion = probabilidad_mutacion
            self.iteraciones = iteraciones

        def generar_anticuerpos(self):
            anticuerpos = []
            for _ in range(self.num_anticuerpos):
                anticuerpo = [ random.randint(0, 1) for _ in range(self.longitud_anticuerpo)]
                anticuerpos.append(anticuerpo)
            return anticuerpos
        
        def seleccionar_anticuerpos(self, num_seleccionados):
            afinidades = self.functObj.calcular_afinidad(self.antigeno,self.anticuerpos,self.longitud_anticuerpo)
            mejores_indices = sorted(range(len(afinidades)), key=lambda i: afinidades[i], reverse=True)
            seleccionados = [self.anticuerpos[i] for i in mejores_indices[:num_seleccionados]]
            return seleccionados

        def cruzar(self):
            nueva_generacion =[]
          
            for x in range(0,int(len(self.anticuerpos)/2)):
                IndRand1 = random.randint(0,self.num_anticuerpos-1)
                IndRand2 = random.randint(0,self.num_anticuerpos-1)
                PuntoCruzaR = random.randint(0,self.longitud_anticuerpo-1)
                Padre1 = self.anticuerpos[IndRand1]
                Padre2 =  self.anticuerpos[IndRand2]

                Hijo1 = Padre1[:PuntoCruzaR] + Padre2[PuntoCruzaR:]
                Hijo2 = Padre2[:PuntoCruzaR] + Padre1[PuntoCruzaR:]

                nueva_generacion.append(Hijo1)
                nueva_generacion.append(Hijo2)

        def mutar_anticuerpos(self):
            for i in range(self.num_anticuerpos):
                for j in range(self.longitud_anticuerpo):
                    if random.random() < self.probabilidad_mutacion:
                        self.anticuerpos[i][j] = 1 - self.anticuerpos[i][j]
        
        def run(self):
            self.cruzar()
            print(f"Antigeno : {self.antigeno}")
            print("Anticuerpos generados de inicio: ")
            for anticuerpo in self.anticuerpos:
                print(anticuerpo)
            for i in range(self.iteraciones):
                print(f"-------Iteracion {i} -------")
                print("Anticuerpos con mas afinidad: ")
                seleccionados = self.seleccionar_anticuerpos(self.num_anticuerpos // 2)
                for anticuerpo in seleccionados:
                    print(anticuerpo)
                
                self.cruzar()
                print("\nAnticuerpos después de la cruza:")
                for anticuerpo in self.anticuerpos:
                    print(anticuerpo)

                self.mutar_anticuerpos()
                print("\nAnticuerpos después de la mutación:")
                for anticuerpo in self.anticuerpos:
                    print(anticuerpo)
#  -----------Neural Network Algorithm  -----------
    class RedNeuronal:
        def __init__(self,numeroNeuronas,tazaAprendizaje,numCapas):
            self.numeroNeuronas = numeroNeuronas
            self.tazaAprendizaje = tazaAprendizaje
            self.numCapas = numCapas
        
        def confCapa(self):
            self.modelo =  tf.keras.Sequential([
                tf.keras.layers.Dense(units=self.numeroNeuronas,input_shape=[1],name="Capa_entrada")
                ])
            for i in range(0,self.numCapas):
                self.modelo.add(tf.keras.layers.Dense(units=self.numeroNeuronas,name="Capa_oculta"+str(i)))
           
            self.modelo.add(tf.keras.layers.Dense(units=1,name="Capa_salida"))
            


        def confCompile(self):
            self.modelo.compile(
                optimizer=tf.keras.optimizers.Adam(self.tazaAprendizaje),
                loss='mean_squared_error')
            
        def getModelo(self):
            self.confCapa()
            self.confCompile()
            return self.modelo

            



        


            
        



        
 
                
    