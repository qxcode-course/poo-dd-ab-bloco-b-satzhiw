class Chinela:
    def __init__(self, tamanho: int):
        self.__tamanho = tamanho

    def setTamanho(self, pe: int):
        if (pe <= 20 or pe >= 50) and pe % 2 != 0:
            print("fail: ou vc tem pezao ou vc n tem pe")
            return False
        else:
            self.__tamanho = pe
            return True
        
    def getTamanho(self) -> int:
        return self.__tamanho 

    def __str__(self) -> str:
        return f"sua chinela é do tamanho {self.getTamanho()}"
    

def main():
    chinela = None
    while True:
        try:
            line: str = input()
        except EOFError:
            break
        args: list[str] = line.split(" ")
        print("$" + line)
        if not args[0]:
            continue
        if args[0] == "end":
            break
        elif args[0] == "init":
            tamanho = args[1]
            chinela = Chinela(tamanho)
            print(f"chinela criada no tamanho {chinela.getTamanho()}") 
            
        elif args[0] == "show":
            if chinela is not None: 
                print(chinela)
        else:
            print("fail: comando desconhecido")

main()


havaiana = Chinela()
havaiana.setTamanho(44)
print(havaiana)



