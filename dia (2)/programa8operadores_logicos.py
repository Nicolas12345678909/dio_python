# Operadores Lógicos
# São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um
# operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os
# operadores lógicos, exemplo:op_comparacao + op_logico + op_comparacao... N...


# Exemplo
saldo = 1000
saque = 200
limite = 100

saldo >= saque
# >>> True
saque <= limite
# >>> False

# Operador E
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
# >>> False


# Operador OU
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
# >>> True


# Operador Negação
# seria como virce-verça
contatos_emergencia = []

not 1000 > 1500
# >>> True
not contatos_emergencia
# >>> True
not "saque 1500;"
# >>> False
not ""
# >>> True


# Parênteses
saldo = 1000
saque = 250
limite = 200

conta_especial = True

# difícil
saldo >= saque and saque <= limite or conta_especial and saldo >= saque
# >>> True

# prático
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
# >>> True


# Aula


# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True and True)
# >>> true

print(True and False and True)
# >>> false

print(False and False and False)
# >>> false

print(True or True or True)
# >>> true

print(True or False or False)
# >>> true

print(False or False or False)
# >>> false

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)
# >>> true

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)
# >>> true

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
# >>> true