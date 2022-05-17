import numpy as np

def menu_1():
    print("-----Menu de opções------")
    print("(1)Mostre a matriz Original")
    print("(2)Mostre a matriz transposta")
    print("(3)Mostre a soma da diagonal principal da matriz")
    print("(4)Mostre os números pares da matriz")
    print("(5)Mostre os números impares da matriz")
    print("(0)Sair do sistema")
    print("-------------------------")

def option_read(m):
    print (m)

def option_t(m):
    m_t = np.array(m).T
    print(m_t)
    
def option_sum(m):
    diagonal_sum = np.trace(m)
    print(diagonal_sum)

def option_pair_numbers(m):
    pair_counter_1 = len(m)
    for i in range(pair_counter_1):
        pair_counter_2 = len(m[0])
        for j in range (pair_counter_2):
            if (m[i][j] % 2 == 0):
                print(m[i][j])

def option_odd_numbers(m):
    odd_counter_1 = len(m)
    for i in range(odd_counter_1):
        odd_counter_2 = len(m[0])
        for j in range (odd_counter_2):
            if (m[i][j] % 2 == 1):
                print(m[i][j])


#Main
#Matriz principal
m_mc = np.array([[9, 7, 4 ,2],
                 [10, 13, 18, 21],
                 [33, 5, 7, 90], 
                 [23, 31, 51, 60]]) 
menu_option = 1
while (menu_option!=0):
    menu_1()
    menu_option = int(input("Selecione a opção desejada: "))
    if menu_option == 1:
        print("Segue a matriz original. ")
        option_read(m_mc)

    if menu_option == 2:
        print("Segue a matriz tranposta. ")
        option_t(m_mc)

    if menu_option == 3:
        option_sum(m_mc)
        print("Segue a soma da diagonal principal da matriz")

    if menu_option == 4:
        print("Os números pares contidos na matriz são: ")
        option_pair_numbers(m_mc)

    if menu_option == 5:
        print("Segue os números impares contidos na matriz: ")
        option_odd_numbers(m_mc)

    if menu_option == 0:
        print("Programa finalizado: ")
        exit()


    