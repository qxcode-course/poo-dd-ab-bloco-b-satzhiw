class Camisa:
    def __init__(self):
        self.__tamanho: str = ""
    
    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, numeracao: str):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if numeracao not in tamanhos_validos:
            print(f"fail: tamanho não encontrado. tamanhos permitidos: {tamanhos_validos}")
        else:
            self.__tamanho = numeracao

    def show(self) -> None:
        print(self)
    
    def __str__(self):
        # CORREÇÃO: O método é getTamanho, não getTam
        return (f"minha camisa é {self.getTamanho()}")

def main():
    camisa = Camisa()

    while True:
        print("Digite um comando (ex: init M, show, end):")
        
        try:
            line = input()
        except EOFError:
            break

        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            if len(args) > 1:
                numeracao = args[1]
                camisa.setTamanho(numeracao)
            else:
                print("fail: comando init precisa de um tamanho (ex: init M)")
        elif args[0] == "show":
            print(camisa)
        else:
            print("fail: comando desconhecido")

main()

polo = Camisa()
polo.setTamanho("M")
print(polo)
