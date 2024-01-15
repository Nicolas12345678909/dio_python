# N = int(input())

# i = 0

# while i < N:

#    v = input().split()

#    a = v[0]

#    b = v[1]

#    if len(b) > len(a):

#        print("nao encaixa")

#    elif a.endswith(b):

#        print("encaixa")

#    else:
#        print("nao encaixa")
# i += 1



# N = int(input("Digite a quantidade de casos de teste: "))

# i = 0

# while i < N:
#     v = input().split()

#     a = v[0]
#     b = v[1]

#     if len(b) > len(a):
#         print("nao encaixa")
#     elif a[-len(b):] == b:
#         print("encaixa")
#     else:
#         print("nao encaixa")

#     i += 1


  # Dicionário com a relação entre números e meses
meses = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

# Leitura da entrada
month = int(input("Digite um valor entre 1 e 12: "))

# Verifica se o número está dentro do intervalo permitido
if 1 <= numero_mes <= 12:
    # Obtém o nome do mês correspondente
    nome_mes = meses[numero_mes]

    # Imprime o resultado com a primeira letra maiúscula
    print(nome_mes.capitalize())
else:
    print("Número inválido. Por favor, digite um valor entre 1 e 12.")