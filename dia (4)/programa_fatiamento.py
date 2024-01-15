# Introdução
# Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), informando inicio
#  (start), fim (stop) e passo (step): [start: stop[, step]].

# Fatiamento
nome = "Guilherme Arthur de Carvalho"

nome [0]
# >>> "G"

nome[:9]
# >>> "Guilherme"

nome [10:]
# >>> "Arthur de Carvalho"

# início <- : -> fim

nome [10:16]
# >>> "Arthur"

# :início:final:estepe
# estepe/step -> passo

nome [10:16:2]
# >>> "Atu"
nome[:]
# >>>>> "Guilherme Arthur de Carvalho"


# espelhar a string
# invertimento

nome [::-1]
# >>>> "ohlavrac ed ruhtrA emrehliuG"


# AULA

nome = "Guilherme Arthur de Carvalho"

print(nome[0])
print(nome[-2])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])