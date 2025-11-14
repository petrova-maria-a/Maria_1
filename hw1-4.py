print("Введите целое неотрцательное число")
num = int(input())
a = 0
b = 1
if num == 0:
    print('Число Фибоначчи = 0')
elif num == 1:
    print('Число Фибоначчи = 1')
else:
    num = (num-1)+(num-2)
    print(num)
