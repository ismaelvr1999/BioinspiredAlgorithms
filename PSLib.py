#Villalpando Rivera Ismael
#Cutonala. ALgoritmos Bioinspirados. 2023-B
import random
import math
class AlgBio:

    def __init__(self) -> None:
        pass

    class AlgGen:

        def __init__(self) -> None:
            pass
        def GenerarInd(self):
            Individuos = [random.randint(0,15) for x in range(0,30)]

            return Individuos
        
        def Cruza(self,Individuos,tasa_mutacion):
            nuevaGeneracion = [] 
            for x in range(0,15):
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

                print(f"Punto de Cruze: {str(PuntoCruzaR)} Padre 1: {BinPadr1} Padre 2: {BinPadr2}")
                print(f"Hijo 1: {Hijo1} Hijo 2: {Hijo2}")

                MutacionH1 = self.Mutacion(Hijo1,tasa_mutacion)
                MutacionH2 = self.Mutacion(Hijo2,tasa_mutacion)
                print(f"Mutacion Hijo 1: { MutacionH1} MutacionHijo 2: { MutacionH2}")

                nuevaGeneracion.append(int(MutacionH1,2))
                nuevaGeneracion.append(int(MutacionH2,2))
                
            return nuevaGeneracion

        def Mutacion(self,Hijo,tasa_mutacion):
            HijoMutado = ""
            for i in range(len(Hijo)):
                gen = Hijo[i]
                if random.random() < tasa_mutacion:
                    if gen == "0":
                        HijoMutado += "1"
                    else: HijoMutado += "0"
                else: HijoMutado +=gen
            return HijoMutado
 
                
    