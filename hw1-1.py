print('Введите трехзначное число')
num = int(input())
summa = 0
while num > 0:
    summa = summa + num%10
    num = num//10
print(summa)