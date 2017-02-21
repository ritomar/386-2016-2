'''
  17. A partir de dois números fornecidos pelo usuário,
      escreva uma das seguintes mensagens:
       - Os dois são pares
       - Os dois são impares
       - O primeiro é par e o segundo é ímpar
       - O primeiro é ímpar e o segundo é par
'''


def ePar(valor):
    return valor % 2 == 0

def eImpar(valor):
    return not ePar(valor)

def mensagem(primeiro, segundo):
    if ePar(primeiro) and ePar(segundo):
        return "Os dois são pares"
    elif eImpar(primeiro) and eImpar(segundo):
        return "Os dois são impares"
    elif ePar(primeiro) and eImpar(segundo):
        return "O primeiro é par e o segundo é ímpar"
    elif eImpar(primeiro) and ePar(segundo):
        return "O primeiro é ímpar e o segundo é par"


# primeiro = int(input("Digite o primeiro número: "))
# segundo = int(input("Digite o segundo número: "))

print(mensagem(2, 8))
print(mensagem(7, 9))
print(mensagem(4, 7))
print(mensagem(3, 6))









    
    
