import math


class calculadora:
    def __init__(self):
        pass
    
    def somar(self, num1,num2):
        return float(num1) + float(num2)

    def subtrair(self, num1, num2):
        return float(num1) - float(num2)

    def multiplicar(self, num1, num2):
       return float(num1) * float(num2)

    def dividir(self, num2):
       if float (num2) == 0:
           return "Impossivel dividir por zero!!!"
       else:
           return float (num2)

    def potencia(self, base, expoente):
        if float (expoente) == 0:
            return float (1)
        elif float (expoente) == 1:
            return float (base)
        else:
            return math.pow(base, expoente)

    def raiz(self, num):
        if float (num) < 0:
            return float ("Impossivel calcular")
        else:
            return math.sqrt(float (num))

    def tabuada(self, num):
        for i in range(11):
            resultado = resultado + "\n{} * {} = {}".format (float(num)), i, int (float (num)*i)
        return resultado