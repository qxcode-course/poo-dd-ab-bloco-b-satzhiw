class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.__calibre = calibre
        self.__dureza = dureza
        self.__tamanho = tamanho
    
    def get_calibre(self) -> float:
        return self.__calibre
    def get_dureza(self) -> str:
        return self.__dureza
    def get_tamanho(self) -> int:
        return self.__tamanho
    
    def set_tamanho(self, novo_tamanho: int):
        self.__tamanho = novo_tamanho

    def usagePerSheet(self) -> int:
        if self.__dureza == 'HB':
            return 1
        elif self.__dureza == '2B':
            return 2
        elif self.__dureza == '4B':
            return 4
        elif self.__dureza == '6B':
            return 6
        return 0 #pq nao sabe a dureza consequentemnte n sabe o gasto
    
    def __str__(self) -> str:
        """Formato: [calibre:dureza:tamanho]"""
        return f"[{self.__calibre}:{self.__dureza}:{self.__tamanho}]"

class Lapiseira: 
    def __init__(self, calibre: float):
        self.__calibre = calibre
        self.__ponta: Grafite | None = None
    
    def hasGrafite(self) -> bool:
        return self.__ponta is not None
    
    def insert(self, grafite: Grafite) -> bool:
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return False
        if self.__calibre != grafite.get_calibre():
            print("fail: calibre incompativel")
            return False
        self.__ponta = grafite
        return True

    def __str__(self) -> str:
        grafite_str = str(self.__ponta) if self.hasGrafite() else "null"
        return f"calibre: {self.__calibre}, grafite: {grafite_str}"

def main():
    lapiseira: Lapiseira | None = None
    
    while True:
        try:
            line = input()
        except EOFError:
            break
        except Exception:
            break
            
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
                calibre = float(args[1])
                lapiseira = Lapiseira(calibre)        
        elif args[0] == "show":
            if lapiseira:
                print(lapiseira)
            else:
                print("fail: lapiseira nao inicializada")

        elif args[0] == "insert":
                calibre = float(args[1])
                dureza = str(args[2])
                tamanho = int(args[3])
                grafite = Grafite(calibre, dureza, tamanho)
                
                if lapiseira:
                    lapiseira.insert(grafite)
                else:
                    print("fail: lapiseira nao inicializada")
                
        elif args[0] == "remove":
            if lapiseira:
                lapiseira.remove()
            else:
                print("fail: lapiseira nao inicializada")

        elif args[0] == "write":
            if lapiseira:
                lapiseira.writePage()
            else:
                print("fail: lapiseira nao inicializada")


main()