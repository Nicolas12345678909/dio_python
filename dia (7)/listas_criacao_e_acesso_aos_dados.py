# Entender o funcionamento da estrutura de dados lista.

# Criando listas
# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

# Exemplo
frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)


# Acesso direto
# A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos sequência a partir do zero.

# Exemplo
frutas = ["maçã", "laranja", "uva", "pera"]

frutas[0] #maçã

frutas[2] # uva


# Índices negativos
# Sequências suportam indexação negativa. A contagem começa em -1.

# Exemplo
frutas = ["maçã", "laranja", "uva", "pera"]

frutas[-1] # pera

frutas[-3] # laranja

# Listas aninhadas
# Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

# Exemplo
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]

matriz[0][0] # 1

matriz[0][-1] #2

matriz[-1][-1] # "c"

# Fatiamento
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

# Exemplo
lista = ["p","y","t","h", "o","n"]

lista[2:] # ["t","h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y","t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y","t","h", "o", "n"]
lista[::-1] # ["n", "o","h", "t", "y", "p"]


# Iterar listas
# A forma mais comum para percorrer os dados de uma lista é utilizando o comando for.


# Exemplo
carros = ["gol", "celta", "palio"]

for carro in carros:
     print(carro)

# Função enumerate
# Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.


# Exemplo
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate (carros):
     print(f"{indice}: {carro}")


# Compreensão de listas
# A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.
     
    #  Filtro versão 1
     
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)


        # Filtro versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]


    # Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
     quadrado.append(numero ** 2)


    #  Modificando valores versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]