# 01. Imprimir todos os números de 1 a 100.

def ImprimirNumeros(inicio, final):
    for i in range(inicio, final + 1):
        print("%3d" % i, end=' ')
        if i % 10 == 0:
            print("")

ImprimirNumeros(1, 100)
