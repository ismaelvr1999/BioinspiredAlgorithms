#Villalpando Rivera Ismael
#Cutonala. ALgoritmos Bioinspirados. 2023-B
import random
import math
class AlgBio:

    def __init__(self) -> None:
        pass

    class AlgGen:
        Individuos = []
        def __init__(self) -> None:
            pass

        def GenerarInd(self):
            self.Individuos = [random.randint(0,15) for x in range(0,30)]
            print(self.Individuos)
            return self.Individuos






# gen = AlgBio.AlgGen()

# gen.GenerarInd()
# gen.CalcApt()

                
                
    