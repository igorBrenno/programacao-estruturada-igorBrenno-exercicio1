def q1():
    """
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.
    """
    numero = int(input(""))

    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")


def q2():
    """
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def'
    Para 'texto', imprima 'to'

    """
    
    texto = input("")

    metade = int(len(texto) / 2)

    if metade % 2 == 0:
        metade = metade + 1
        
    else:
        metade = metade
    
    saida = texto[metade:]
    print(saida)

def q3():
    """
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha
    """
    numero = int(input(""))
    lista = ""
    for i in range(1,11):

        lista = lista + str(numero * i) + " "
    print(lista, end="")

def q4():
    """
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
    """
    nome = input("")

    x = nome.split()
    tamanho = len(x)
    saida = ""
    for i in range(tamanho):
        if x[i] == x[0] or x[i] == x[tamanho - 1]:
            if i < tamanho - 1:
                saida = saida + x[i][0].upper() + x[i][1:] + " "
            else:
                saida = saida + x[i][0].upper() + x[i][1:]
        else:
            if i < tamanho - 1:
                saida = saida + x[i][0] + x[i][1:] + " "
            else:
                saida = saida + x[i][0] + x[i][1:]

    print(saida)


def q5():
    """
    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno
    """
    lado = input("")
    saida = ""
    if lado[0] == lado[1] and lado[0] == lado[2]:
        saida = "equilátero"
    elif lado[0] == lado[1] or lado[0] == lado[2] or lado[1] == lado[2]:
        saida = "isósceles"
    else:
        saida = "escaleno"
    print(saida)