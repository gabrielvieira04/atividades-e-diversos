#Pratica realizada no dia 17-05-2022
#Primeira solução, utilizando estrutura de repetição
print("\x1b[2J\x1b[1;1H")
n = int(input("Digite o número que deseja calcular o fatorial."))

def n_fatorial(n):
    print("\x1b[2J\x1b[1;1H")
    fatorial = 1
    for i in range(1,n+1):
        fatorial = fatorial * i 
    print(f"O fatorial de", n,  "é", fatorial)

n_fatorial(n)

#Segunda solução, utilizado recursividade.
