# Introdução
# Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a
#  atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.

# Strings triplas
nome = "Guilherme"

mensagem = f""" Olá meu nome é {nome}, Eu estou aprendendo Python """

# >>> 
# 
# Olá meu nome é Guilherme, Eu estou aprendendo Python
# 



# Strings triplas
nome = "Guilherme"

mensagem = f'''
    Olá meu nome é {nome},
Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
'''
# >>>
# 
#   Olá meu nome é Guilherme,
# Eu estou aprendendo Python.
#    Essa mensagem tem diferentes recuos.
# 



# AULA

nome = "Guilherme"

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)


print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)

menu = "============= MENU =============\n"
menu += "\n"
menu += "1 - Depositar\n"

print(menu)