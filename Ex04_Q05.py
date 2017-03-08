# 05. Imprimir o quadrado dos números de 1 a 20.


def potencia(b, n):
    p = 1
    for i in range(n):
        p *= b
    return p


for i in range(1, 21):
    print("%4d" % potencia(i, 2))
