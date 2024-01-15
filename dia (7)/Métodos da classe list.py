# Métodos da classe list

# [].append

lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]


# [].clear

lista = [1, "Python", [40, 30, 20]]

print(lista) [1, "Python", [40, 30, 20]]

lista.clear()

print(lista) # []

# [].copy

lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista) # [1, "Python", [40, 30, 20]]

# aula

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()
print(lista)

print(id(l2), id(lista)) # [1, "Python", [40, 30, 20]]

l2[0] = 2

print(l2)
print(lista)


# [].count
cores = ["vermelho", "azul", "verde", "azul"]
cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1


# [].extend
linguagens = ["python","js", "c"]
print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])
print(linguagens) # ["python", "js", "c", "java", "csharp"]


# [].index
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java") # 3
linguagens.index("python") # 0



# [].pop
linguagens = ["python","js", "c", "java", "csharp"]

linguagens.pop() # csharp
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python


# [].reverse
linguagens = [ "python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens) # ["csharp", "java", "c", "js", "python"]




# [].sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"]

linguagens = ["python","js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]

linguagens = ["python","js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]


# len
linguagens = ["python", "js", "c", "java", "csharp"]

len(linguagens) # 5



# sorted
linguagens = ["python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]


# Aula

# linguagens = ["python", "js", "c", "java", "csharp"]
# # isso para procura a variáveis do comando
# print(sorted (linguagens, key-lambda x: len(x))) # ["c", "js", "java", "python", "csharp"]
# print(sorted(linguagens, key-lambda x: len(x), reverse True)) # ["python", "csharp", "java", "js", "c"]

# print(sorted (linguagens))