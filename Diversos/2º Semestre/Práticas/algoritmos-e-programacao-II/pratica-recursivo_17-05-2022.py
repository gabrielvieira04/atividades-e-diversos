#Pratica realizada no dia 17-05-2022
#Primeira solução, utilizando estrutura de repetição
print("\x1b[2J\x1b[1;1H")
n = int(input("Digite o número que deseja calcular o fatorial.\n"))

def factorial(n):
    print("\x1b[2J\x1b[1;1H")
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i 
    print(f"O fatorial de", n,  "é", factorial)

#Segunda solução, utilizado recursividade.
def factorial_second(n):
    print("Segunda solução: \n")    
    if(n==0):
        return 1
    else:
        print(f"O fatorial de", n, "é igual a: ",n * factorial(n-1))

factorial(n)
factorial_second(n)

