print("Вводите целые числа. Чтобы закончить, введите 'стоп'.")
max = None
while True:
    inp = input("Введите число \n")
    if inp == 'стоп':
        break    
    try:  
        num = int(inp)      
        if max is None or num > max:
            max = num                     
    except ValueError:
        print("Ошибка! Введите целое число или 'стоп'.")
if max is not None:
    print(f'Самое большое число: {max}')
else:
    print("Вы не ввели ни одного числа.")