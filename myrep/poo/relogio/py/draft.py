class Watch:
    def __init__(self):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
    
    def getHora(self):
        return self.__hora
    def getMinuto(self): 
        return self.__minuto
    def getSegundo(self):
        return self.__segundo 

    def setHora(self, horinha: int ):
        if 0 <= horinha <= 23:
            self.__hora = horinha
        else:
            print("fail: hora invalida")
    
    def setMinuto(self, minutinho: int ):
        if 0 <= minutinho <= 59:
            self.__minuto = minutinho
        else:
            print("fail: minuto invalido")
    
    def setSegundo(self, segundinho: int ):
        if 0 <= segundinho <= 59:
            self.__segundo = segundinho
        else:
            print("fail: segundo invalido")    

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo == 60:
            self.__segundo= 0 
            self.__minuto += 1
        if self.__minuto == 60:
            self.__minuto = 0 
            self.__hora += 1
        if self.__hora == 24:
            self.__hora = 0

    def show(self) -> None:
        print(self)
    
    def __str__(self):
        return (f"{self.getHora():02d}:{self.getMinuto():02d}:{self.getSegundo():02d}")

def main():
    relogio = Watch()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "set":
             horinha = int(args[1])
             minutinho = int(args[2])
             segundinho = int(args[3])
             relogio.setHora(horinha)
             relogio.setMinuto(minutinho)
             relogio.setSegundo(segundinho)
        elif args[0] == "init":
             relogio = Watch()
             horinha = int(args[1])
             minutinho = int(args[2])
             segundinho = int(args[3])
             relogio.setHora(horinha)
             relogio.setMinuto(minutinho)
             relogio.setSegundo(segundinho)
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "next":
            relogio.nextSecond()

main()