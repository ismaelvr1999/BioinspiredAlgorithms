#Villalpando Rivera Ismael
#Cutonala. ALgoritmos Bioinspirados. 2023-B
from PSLib import AlgBio
import random
class ParamLib:
    def __init__(self) -> None:
        pass

    class ParamAlg:
        MasApt = ()
        Individuos = []
        Nueva_Generacion = []
        tasa_mutacion = 0.1

        def __init__(self,Algoritmo) -> None:
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

        def producir(self):
            print("Primera generacion")
            self.Individuos = self.AlgoritmoGen.GenerarInd()
            print(self.Individuos)
            self.funObj(self.Individuos)
            print("------------Cruza---------------")
            self.Nueva_Generacion = self.AlgoritmoGen.Cruza(self.Individuos,self.tasa_mutacion)
            print("--------------Nueva generacion-------------")
            print(self.Nueva_Generacion)
            self.funObj(self.Nueva_Generacion)


        
        
AlgGen = AlgBio.AlgGen()
obj = ParamLib.ParamAlg(AlgGen)
obj.producir()




