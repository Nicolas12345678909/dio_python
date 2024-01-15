while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)


# Estruturas de Repetição

# O que são estruturas de repetição?
# São estruturas utilizadas para repetir um trecho de código um
# determinado número de vezes. Esse número pode ser
# conhecido previamente ou determinado através de uma
# expressão lógica.


# Exemplo sem repetição
# Receba um número do teclado e exiba os 2 números seguintes
a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)



# Exemplo com repetição
# Receba um número do teclado e exiba os 2 números seguintes
a = int(input("Informe um número inteiro: "))
print(a)

# repita 2 vezes:
a += 1
print(a)



# Comando for
# O comando for é usado para percorrer um objeto iterável. Faz sentido
# usar for quando sabemos o número exato de vezes que nosso bloco de código
# deve ser executado, ou quando queremos percorrer um objeto iterável.


# for

texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print()
# adiciona uma quebra de linha



# for/else
# Exemplo utilizando um iterável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()
    print("Executar no final do laço")
# adiciona uma quebra de linha



# Função range
# Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio
#  (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido:
# i, i+1, +2, +3, ..., j-1.
# Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.

# range
# range(stop) -> range object
# range(start, stop[, step]) -> range object
list(range(4))
# >>> [0, 1, 2, 3]



# Utilizando range com for
# Exemplo utilizando a função built-in range
for numero in range(0, 11):
    print(numero, end=" ")

# >>> 0 1 2 3 4 5 6 7 8  9 10


# exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

# >>> 0 5 10 15 20 25 30 35 40 45 50



# Comando while
# O comando while é usado para repetir um bloco de código várias vezes.
#  Faz sentido usar while quando não sabemos o número exato de
#  vezes que nosso bloco de código deve ser executado.


# while
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")

    elif opcao == 2:
        print("Exibindo o extrato... ")
        
# while/else
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

if opcao == 1:
    print("Sacando...")

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    print("Obrigado por usar nosso sistema bancário, até logo!")



# BREAK
# a instrução break oferece a possibilidade de sair de um loop quando uma condição externa é acionada. A instrução break será colocada
#  dentro do bloco de código abaixo da sua instrução de loop, geralmente após uma instrução condicional if . Neste pequeno programa,
#  o number da variável é inicializado em 0.

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

# /////////////////////////////////CORRECT//////////////////////////////////////////////////

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)

# /////////////////////////////////ERRO//////////////////////////////////////////////////

while True:
    numero = int(input("Informe um número: "))

    if numero % 2 == 0:
        continue

    if numero == 10:
        break

    print(numero)


# CONTINUE
# continue dá a opção de ignorar a parte de um loop onde uma condição externa é acionada, mas continuar e completar o resto do loop.
#  Ou seja, a iteração atual do loop será interrompida, mas o programa retornará ao topo do loop.


for numero in range(100):

     if numero % 2 == 0:
         continue

     print(numero, end=" ")