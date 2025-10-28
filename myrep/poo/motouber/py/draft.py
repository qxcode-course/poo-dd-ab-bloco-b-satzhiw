class Pessoa:
    def __init__(self, nome: str, dinheiro: float):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def get_nome(self) -> str:
        return self.__nome

    def get_dinheiro(self) -> float:
        return self.__dinheiro

    def pagar(self, valor: float) -> float:
        if valor < 0:
            return 0.0
            
        if self.__dinheiro >= valor:
            self.__dinheiro -= valor
            return valor
        else:
            valor_pago = self.__dinheiro
            self.__dinheiro = 0.0
            return valor_pago

    def receber(self, valor: float):
        if valor > 0:
            self.__dinheiro += valor

    def __str__(self) -> str:
        if self.__dinheiro == int(self.__dinheiro):
            return f"{self.__nome}:{int(self.__dinheiro)}"
        return f"{self.__nome}:{self.__dinheiro:.2f}"

class Moto:
    def __init__(self):
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None
        self.__custo: float = 0.0

    def get_motorista(self) -> Pessoa | None:
        return self.__motorista
    def get_passageiro(self) -> Pessoa | None:
        return self.__passageiro
    def get_custo(self) -> float:
        return self.__custo

    def _iniciar_corrida(self):
        self.__custo = 0.0
    def _adicionar_custo(self, valor: float):
        if valor > 0:
            self.__custo += valor

    def setDriver(self, motorista: Pessoa) -> bool:
        if self.__motorista is not None:
            print(f"fail: Ja existe um motorista.")
            return False
        if self.__passageiro is not None:
            print("fail: Nao pode trocar de motorista durante uma corrida.")
            return False
        self.__motorista = motorista
        return True

    def setPass(self, passageiro: Pessoa) -> bool:
        if self.__motorista is None:
            print("fail: Impossivel subir, moto sem motorista.")
            return False
        if self.__passageiro is not None:
            print(f"fail: Moto ja esta com passageiro.")
            return False
        self.__passageiro = passageiro
        self._iniciar_corrida()
        return True

    def drive(self, km: float):

        if self.__motorista is None or self.__passageiro is None:
            print("fail: Corrida nao pode ser iniciada.")
            return
        custo_trecho = km * 1.0 
        self._adicionar_custo(custo_trecho)

    def leavePass(self):
        if self.__passageiro is None:
            print("fail: Nao ha passageiro para desembarcar.") 
            return
        if self.__motorista is None:
            print("fail: Nao ha motorista") 
            return
        custo_final = self.get_custo()
        valor_pago = self.__passageiro.pagar(custo_final)
        if valor_pago < custo_final:
            print("fail: Passenger does not have enough money")

        self.__motorista.receber(custo_final)
        
        print(f"{self.__passageiro} left")
        
        self.__passageiro = None
        self._iniciar_corrida()

    def __str__(self) -> str:
        motorista_str = str(self.__motorista) if self.__motorista else "None"
        passageiro_str = str(self.__passageiro) if self.__passageiro else "None"
        
        custo_str = ""
        if self.__custo == int(self.__custo):
            custo_str = str(int(self.__custo))
        else:
            custo_str = f"{self.__custo:.2f}"
            
        return f"Cost: {custo_str}, Driver: {motorista_str}, Passenger: {passageiro_str}"

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
        elif args[0] == "setDriver":
                nome = str(args[1])
                dinheiro = float(args[2])
                pessoa = Pessoa(nome, dinheiro)
                moto.setDriver(pessoa)
        elif args[0] == "setPass":
                nome = str(args[1])
                dinheiro = float(args[2])
                pessoa = Pessoa(nome, dinheiro)
                moto.setPass(pessoa)
        elif args[0] == "show":
            print(moto)
        elif args[0] == "leavePass":
            moto.leavePass()
        elif args[0] == "drive":
            km = float(args[1])
            moto.drive(km)

main()