class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
    
    def getNome(self) -> str:
        return self.__nome
    
    def getIdade(self) -> int:
        return self.__idade

    def __str__(self):
        return f"{self.__nome}:{self.__idade}"
    
class Moto:
    def __init__(self, potencia_inicial: int = 1):
        self.__potencia = potencia_inicial
        self.__minutos = 0
        self.__pessoa: Pessoa | None = None

    def getPotencia(self) -> int:
        return self.__potencia
    
    def getMinutos(self) -> int:
        return self.__minutos
    
    def getPessoa(self) -> Pessoa | None:
        return self.__pessoa

    def inserirPessoa(self, pessoa: Pessoa) -> bool: 
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
            return False 
        
        self.__pessoa = pessoa
        return True 

    def removerPessoa(self) -> Pessoa | None:
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return None
        pessoa_removida = self.__pessoa
        self.__pessoa = None
        print(pessoa_removida)
        return pessoa_removida
    
    def dirigir(self, dirigirTempo: int) -> bool:
        if self.__minutos == 0:
            print("fail: buy time first")
            return False
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return False
        if self.__pessoa.getIdade() > 10: 
            print("fail: too old to drive")
            return False
        
        if self.__minutos >= dirigirTempo:
            self.__minutos -= dirigirTempo
            return True
        else:
            tempo_dirigido = self.__minutos
            self.__minutos = 0
            print(f"fail: time finished after {tempo_dirigido} minutes")
            return False
    
    def comprarTempo(self, minutos: int):
        if minutos > 0:
            self.__minutos += minutos
    
    def buzina(self) -> str:
        return f"P{'e' * self.__potencia}m"

    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        pessoa_obj = self.getPessoa()
        if pessoa_obj is None:
            pessoa_str = "(empty)"
        else:
            pessoa_str = f"({pessoa_obj})"
        return f"power:{self.getPotencia()}, time:{self.getMinutos()}, person:{pessoa_str}"
def main():
    moto = Moto()
    
    while True:
        try:
            line = input()
        except EOFError:
            break
        except Exception:
            break
        print("$" + line)
        args = line.split(" ")
        if not args or args[0] == "":
            continue
        if args[0] == "end":
            break
        
        elif args[0]== "enter":
            nome = str (args[1])
            idade = int(args[2])
            if idade > 0:
                pessoa = Pessoa(nome, idade)
                moto.inserirPessoa(pessoa)
        elif args[0] == "init":
            potencia = int(args[1])
            if potencia < 1:
                potencia = 1
            moto = Moto(potencia)
        elif args[0] == "show":
            print(moto)
        elif args[0] == "leave":
            moto.removerPessoa() 
        elif args[0] == "buy":
            minutos = int(args[1])
            moto.comprarTempo(minutos)
        elif args[0] == "drive":
            dirigirTempo= int(args[1])
            moto.dirigir(dirigirTempo)        
        elif args[0] == "honk":
            print(moto.buzina())

main()


#     def __main__(self):
#         moto = Moto()
#         while True:
#             line = input()
#             print("$" + line)
#             args = line.split(" ")

#             if args[0] == "end":
#                 break
#             elif args[0] == "init":
#                 moto = Moto()
#             elif args[0] == "enter":
#                 relogio = Watch()
#                 horinha = int(args[1])
#                 minutinho = int(args[2])
#                 segundinho = int(args[3])
#                 relogio.setHora(horinha)
#                 relogio.setMinuto(minutinho)
#                 relogio.setSegundo(segundinho)
#             elif args[0] == "show":
#                 print(moto)
# def __main__(self):
#         moto = Moto()
#         while True:
#             line = input()
#             print("$" + line)
#             args = line.split(" ")

#             if args[0] == "end":
#                 break
#             elif args[0] == "init":
#                 pessoa = bool(args[1])
#                 potencia = int(args[2])
#                 minutos = int(args[3])
#                 relogio.(horinha)
#                 relogio.setMinuto(minutinho)
#                 relogio.setSegundo(segundinho)
#             elif args[0] == "drive":
#                 relogio = Watch()
#                 horinha = int(args[1])
#                 minutinho = int(args[2])
#                 segundinho = int(args[3])
#                 relogio.setHora(horinha)
#                 relogio.setMinuto(minutinho)
#                 relogio.setSegundo(segundinho)
#             elif args[0] == "show":
#                 print(moto)
#             elif args[0] == "leave":
#                 relogio.nextSecond()
#             elif args[0] == "buy":
#                 relogio.nextSecond()
#             elif args[0] == "honk":
#                 relogio.nextSecond()


main()