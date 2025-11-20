print("Введите 'стоп' для завершения или что угодно для продолжения")
while input() != "стоп":
    print('Введите число от 1 до 999')
    num = int(input())
    if num / 100 >= 1:
        if num % 3 == 0:
            num = num ** 2
        elif:
            num = num // 5
    if num / 100 < 1:
        num = (num * 8) % 6
    print(num)
