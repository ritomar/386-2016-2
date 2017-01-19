"""
    Isso é uma DOCSTRING
    e ela
    pode ter
    várias linhas.

    DOCSTRING não é
    comentário
    
"""

# Comentários são sempre de uma única linha
# e são criados com o caracter # 


# Comando de saída de dados
print("print() é o comando de saída de dados")
print("Pode receber vários", "parâmetros separados por", "vírgula.")

# Imprimir linha em branco:
print('\n') # ou print("")

# Criação de variáveis
# Segue o padrão: identificador = valor
# Exemplo:

a = 10 # Cria uma variável inteira com identificador "a" e atribui o valor "10"
nome = "João" # Cria uma variável do tipo String
tem_filho = False # Cria uma variável Booleana
x = 2.54321 # Cria uma variável real

print('\n')

# Imprime o conteúdo das variáveis

print("Variável inteira:", a)
print("Variável string:", nome)
print("Variável boolean:", tem_filho)
print("Variável real:", x)

print('\n')

# É possível formatar a saída valores reais, por exemplo:
print("Valor 2.54321 formatado com duas casas: %.2f" % x)

print('\n')

# Comando de Entrada de Dados
nome = input("Digite seu nome: ")
print("Olá,", nome)

# A função type retorna o tipo da variável
print(type(nome)) # <class 'str'>

print('\n')

# Força a conversão do input para inteiro
idade = int(input("Digite a sua idade: "))
print(type(idade)) # <class 'int'>

print('\n')

# Força a conversão do input para float
peso = float(input("Digite seu peso: "))
print(type(peso)) # <class 'float'>

print('\n')

# Operadores Aritméticos
a = 5
b = 2
c = 6

print("a =", a)
print("b =", b)
print("c =", c)

print("Soma: a + b = ", a + b)
print("Subtração: a - b = ", a - b)
print("Multiplicação: a * b = ", a * b)
print("Divisão real: a / b = ", a / b)
print("Divisão inteira: a // b = ", a // b)
print("Módulo(resto): a % b = ", a % b)

print('\n')

# Operadores Relacionais
print("Igualdade: a == b = ", a == b)
print("Diferente: a != b = ", a != b)
print("Maior: a > b = ", a > b)
print("Menor: a < b = ", a < b)
print("Maior ou igual: a >= b = ", a >= b)
print("Menor ou igual: a <= b = ", a <= b)

print('\n')

# Operadores Lógicos
print("and: (a == b) and (b == c) =", (a == b) and (b == c))
print("or:  (a == b) or  (b == c) =", (a == b) or (b == c))
print("not: not (a == b) =", not (a == b))

