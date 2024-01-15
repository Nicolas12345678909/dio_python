# Criando dicionários
# Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas

# Exemplo
pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3333-1234" # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(pessoa)

# exemplo prof

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234" # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

pessoa ["nome"] = "Maria"
print(pessoa)



# Acesso aos dados
# Os dados são acessados e modificados através da chave.

# Exemplo
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados ["nome"] # "Guilherme"
dados["idade"] # 28
dados["telefone"] # "3333-1234"

dados ["nome"] = "Maria"
dados ["idade"] = 18
dados ["telefone"] = "9988-1781"

print(dados) # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}



# Dicionários aninhados
# Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strings e números).

# Exemplo
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"] # "3443-2121"
print(telefone)

# Exemplo prof
contatos1 = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}

telefone1 = contatos1["giovanna@gmail.com"]["telefone"] # "3443-2121"
print(telefone1)

extra = contatos1["melaine@gmail.com"]["extra"]["a"]
print(extra)



# Iterar dicionários
# A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for.

# Exemplo
for chave in contatos:
     print(chave, contatos [chave])
for chave, valor in contatos.items():
     print(chave, valor)

# guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'} #giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
#chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
#melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766'}
     
for chave in contatos:
     print(chave, contatos [chave])

print("=" * 100)

for chave, valor in contatos.items():
     print(chave, valor)