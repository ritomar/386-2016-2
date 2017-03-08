def SerieH(N):
    soma = 0.0
    for i in range(1, N + 1):
        soma += 1/i
    return soma

n = int(input("Digite o N: "))

print("H =", SerieH(n))

