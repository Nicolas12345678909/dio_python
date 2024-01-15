# Estruturas condicionais ternaria
# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

# If
# Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if. O comando
# irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.

# Exemplo
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo <= saque:
    print("Saldo insuficiente!")

#     If/else
# Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a
# expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código
# 'do else será executado.

# Exemplo
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

# If/elif/else
# Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por
# uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um 
# número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade
# do código.


# Exemplo
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))
#...
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    # certo -> Sys
    SystemExit.exit("Opção inválida")

# AULA

maior_idade = 18
idade_especial = 17

idade = int(input("Informe sua idade: "))
if idade >= maior_idade:
    print("Maior de idade, pode tirar a CHN.")

if idade < maior_idade:
    print("Ainda não pode tirar a CNH.")

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CHN.")

else:
    print("Ainda não pode tirar a CNH.")

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CHN.")

elif idade == idade_especial:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")

else:
    print("Ainda não pode tirar a CNH.")



# If aninhado
# Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de
# estruturas if/elif/else.


# AULA aninhada

conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")


# AULA ternaria

# If ternário
# O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão
# retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.


saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

