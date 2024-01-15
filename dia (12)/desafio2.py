T = int(input())

for i in range(T):
   # A função "range" é uma função incorporada na linguagem de programação Python que é usada para gerar uma sequência de números. Ela é comumente usada em loops e iterações, onde precisamos executar um bloco de código várias vezes.

   i = input()

   i = i.split()

   

   N = int(i[0])

   K = int(i[1])

   

   garrafas_cheias = N // K

   garrafas_vazias = N % K

   

   total = garrafas_vazias + garrafas_cheias

   print(total)