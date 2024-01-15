# operadores identidade
# São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.


# Exemplo
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# operador identidade é IS que compara os objetos
curso is nome_curso
# >>> True

curso is not nome_curso
# >>> False

saldo is limite
# >>> True


# Aula
saldo = 1000
limite = 1000

print(saldo is limite)
# >>> True

print(saldo is not limite)
# >>> False