# Нахождение + и - чисел в последовательности


kolvo_polos = 0
kolvo_otr = 0
x = int(input("Вводите числа, в конце последовательности введите 0: "))
while x != 0:
    if x > 0:  
        kolvo_polos += 1
    else:
        kolvo_otr += 1
    x = int(input("Вводите числа, в конце последовательности  введите 0: "))
    
print( "Положительных: ", kolvo_polos )
print( "Отрицательных: ", kolvo_otr )
