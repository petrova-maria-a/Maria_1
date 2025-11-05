print('Введите число с кесколькими знаками после точки')
number = float(input())
number1 = number*100
number2 = int(number1)
number3 = number2%100
print(number3)