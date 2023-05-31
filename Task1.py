# Задача 22:
# Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# n=int(input("Input number N "))
# m=int(input("Input number M"))
set_n=set()
set_m=set()
resultSet=set()
n=5
m=8
count=0
for i in range(n): 
    set_n.add(int(input("Input numbers in set n ")))
for j in range(m): 
    set_m.add(int(input("Input numbers in set m ")))
for i in set_n:
    for j in set_m:
        if i==j:
            resultSet.add(i)
            count+=1 
if count==0:
    print("There are no duplicate numbers")  
else:          
    print(*sorted(resultSet))