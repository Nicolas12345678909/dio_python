# number = 0

# range é qunatas vezes devem ser digitado

# for number in range():
#     number = int(input("digite "))
#     if number == 5:
#         break    # break here

#     print('Number is ' + str(number))

# print('Out of loop')

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     number = int(input("digite "))
#     if num == 3:
#         continue
#     print(num)

# Usando o loop while para repetir um bloco de código
# i = 0
# while i < 12:
#     i = int(input("digite "))
#     print(i)

# Usando a instrução break para sair de um loop prematuramente
# while True:
#     for num in numbers:
#         numbers = [1, 2, 3, 4, 5]
#         number = int(input("digite "))
#     if num < 12:
#         break
#     print(num)


A = "January"
B = "February"
C = "March"
D = "April"
E = "May"
F = "June"
G = "July"
H = "August"
I = "September"
J = "October"
K = "November"
L = "December"

while True:
    try:
        month_number = int(input("Digite o número do mês (1-12): "))
        if month_number < 1 or month_number > 12:
            # não é necessario colocar ''raise'', só alerta o poblem, como opcional pode substituir o ''print'' para fluir o programa.
            raise ValueError("O número do mês deve estar entre 1 e 12.")
        month_name = [A, B, C, D, E, F, G, H, I, J, K, L][month_number - 1]
        # o ''month_name'' é necessario para ter a noção para selecionar o variavel, o ''- 1'' é certeza da seleção pernamente e o mesmo.
        print(f"O mês correspondente ao número {month_number} é {month_name}.")
        break
    except ValueError as e:
        print(f"digite novamente: {e}")

# A = "january"
# B = "february"
# C = "march"
# D = "april"
# E = "may"
# F = "june"
# G = "juny"
# H = "august"
# I = "september"
# J = "october"
# K = "november"
# L = "december"

# while True:
#     try:
#         calender = input("Digite o mês em inglês, deve ser chamado pelo abecedário maiúsculo dos meses... ")
#         month = {A: "January", B: "February", C: "March", D: "April", E: "May", F: "June", G: "Juny", H: "August", I: "September", J: "October", K: "November", L: "December"}
#         print(month[calender])
#     except KeyError:
#         print("O mês deve ser chamado pelo abecedário maiúsculo dos meses.")

# try:
#     price = int(price)
# except ValueError as e:
#     print ('', e)

# while True:
#     price = raw_input('Please enter your marks for Maths:')
#     try:
#         price = int(price)
#         if price < 0 or price > 100:
#             raise ValueError
#         break
#     except ValueError:
#         print ()"Please enter a whole number from 0 to 100")

# print ("The mark entered was", price)