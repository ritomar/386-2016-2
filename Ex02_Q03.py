'''
  Faça uma função que recebe dois números por parâmetro e retorna o maior.
'''


def maior(primeiro, segundo):
    '''
        função que retorna o maior entre dois números
    '''
    # return primeiro if primeiro > segundo else segundo
    if primeiro > segundo:
        return primeiro
    else:
        return segundo

print(maior(4, 3))

