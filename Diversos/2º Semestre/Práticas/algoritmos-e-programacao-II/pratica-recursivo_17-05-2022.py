#Pratica realizada no dia 17-05-2022
#O código deve retornar o valor de um número fatorial, primeiro utilizando repetição 
#e depois utilizado recursividade.

#Primeira solução, utilizando estrutura de repetição
print("\x1b[2J\x1b[1;1H")
n = int(input("Digite o número que deseja calcular o fatorial.\n"))

def factorial(n):
    print("\x1b[2J\x1b[1;1H")
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i 
    print(f"O fatorial de", n,  "é", factorial)
factorial(n)
