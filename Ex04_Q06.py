# 06. Criar um algoritmo que calcule e imprima o valor de bn.
# O valor de n deverá ser maior que 1 e inteiro e o valor de
# b maior ou igual a 2 e inteiro.


def potencia(b, n):
    p = 1
    for i in range(n):
        p *= b
    return p

b = int(input("Digite a base: "))
n = int(input("Digite o expoente: "))

if n > 1 and b >= 2:
    print("Potencia = ", potencia(2, 3))
else:
    print("Valores inválidos.")
