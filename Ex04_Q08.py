# 08. Criar um algoritmo que calcule a soma dos números pares entre 25 e 200.

def ePar(n):
    return n % 2 == 0

def SomaPares(inicio, final):
    if not ePar(inicio):
        inicio += 1
    soma = 0        
    for i in range(inicio, final + 1, 2):
        soma += i
    return soma

a = int(input("Início: "))
b = int(input("Final: "))

print("Soma dos pares entre %d e %d: %d" % (a, b, SomaPares(a, b)))

