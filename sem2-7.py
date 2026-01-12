n = float(input('Вводите числа \n'))
sum = 0
count = 0
while n != 0:
    sum = sum + n
    count = count + 1
    n = float(input())
if sum !=0:
    print(sum / count)
