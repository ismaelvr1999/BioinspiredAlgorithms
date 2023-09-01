#Villalpando Rivera Ismael
#Cutonala. ALgoritmos Bioinspirados. 2023-B
from PSLib import AlgBio
import random
class ParamLib:
    def __init__(self) -> None:
        pass

    class ParamAlg:
        Aptitud = {}
        MasApt = {}
        Individuos = []
        Nueva_Generacion = []
        tasa_mutacion = 0.1

        def __init__(self,Ind) -> None:
            self.Individuos = Ind

        def funObj(self):
            for x in range(0,30):
                eval = pow(self.Individuos[x],2)+2
                self.Aptitud[ eval ] = self.Individuos[x]

            mayor =max(self.Aptitud)
            self.MasApt[self.Aptitud[mayor]] = mayor
            print(self.Aptitud)
            print("Mas apto = Evaluacion: "+str(mayor)+" Genotipo: "+str(self.Aptitud[mayor]))

        
        def Cruza(self):
            for x in range(0,15):
                IndRand1 = random.randint(0,29)
                IndRand2 = random.randint(0,29)
                PuntoCruzaR = random.randint(0,3)
                
                Padre1 = self.Individuos[IndRand1]
                Padre2 = self.Individuos[IndRand2]
                
                BinPadr1 = str(bin(Padre1))[2:]
                BinPadr2 = str(bin(Padre2))[2:]
                
                BinPadr1 = BinPadr1.zfill(4)
                BinPadr2 = BinPadr2.zfill(4)

                Hijo1 = BinPadr2[:PuntoCruzaR] + BinPadr1[PuntoCruzaR:]
                Hijo2 = BinPadr1[:PuntoCruzaR] +BinPadr2[PuntoCruzaR:]

                print(f"Punto de Cruze: {str(PuntoCruzaR)} Padre 1: {BinPadr1} Padre 2: {BinPadr2}")
                print(f"Hijo 1: {Hijo1} Hijo 2: {Hijo2}")

                MutacionH1 = self.Mutacion(Hijo1)
                MutacionH2 = self.Mutacion(Hijo2)
                print(f"Mutacion Hijo 1: { MutacionH1} MutacionHijo 2: { MutacionH2}")

                # self.Individuos[IndRand1] = int(Hijo1,2)
                # self.Individuos[IndRand2] = int(Hijo2,2)

                self.Nueva_Generacion.append(int(Hijo1,2))
                self.Nueva_Generacion.append(int(Hijo2,2))

            print("Nueva generacion")
            print(self.Nueva_Generacion)

        def Mutacion(self, Hijo):
            HijoMutado = ""
            for i in range(len(Hijo)):
                gen = Hijo[i]
                if random.random() < self.tasa_mutacion:
                    if gen == "0":
                        HijoMutado += "1"
                    else: HijoMutado += "0"
                else: HijoMutado +=gen

            return HijoMutado
                    











        
        
gen = AlgBio.AlgGen()
ind = gen.GenerarInd()
obj = ParamLib.ParamAlg(ind)
obj.funObj()

obj.Cruza()

# BinPadr = str(bin(dec))[2:]

# print(BinPadr)


