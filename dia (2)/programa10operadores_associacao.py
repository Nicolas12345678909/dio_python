# Operadores de associação
# São operadores utilizados para verificar se um objeto está presente em uma sequência.

# Exemplo
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

# IN é uma lista de presença da variavel

"Python" in curso
# >>> True

"maçã" not in frutas
# >>> True

200 in saques
# >>> False


# Aula
frutas = ["limao", "uva"]
curso = "Curso de python"

print("laranja" not in frutas)
# >>> True

print("limao" in frutas)
# >>> True

print("Python" in curso)
# >>> False