# Introdução
# A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
# Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.


# Maiúscula, minúscula e título
curso = "pYtHon"

print(curso.upper())
# >>> PYTHON

print(curso.lower())
# >>> python

print(curso.title())
# >>> Python

# Eliminando espaços em branco
curso = "   Python"

print(curso.strip())
# >>> "Python"

print(curso.lstrip())
# >>> "Python "

print(curso.rstrip())
# >>> "   Python"

# Junções e centralização
curso = "Python"

print(curso.center(10, "#"))
# >>> "##Python##"

print(".".join(curso))
# >>> "P.y.t.h.o.n"



# AULA


nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")

for letra in menu:
    print(letra, end="-")
print()
print("-".join(menu))

print("-".join(menu))
