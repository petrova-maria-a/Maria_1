max_number = None

print("Вводите целые числа. Чтобы закончить, введите 'стоп'.")

while True:
    user_input = input("Введите число: ")
    
    if user_input.lower() == 'стоп':
        break
    
    try:
        number = int(user_input)
        
        # Если это первое число ИЛИ оно больше текущего максимума — обновляем максимум
        if max_number is None or number > max_number:
            max_number = number
            
    except ValueError:
        print("Ошибка! Введите целое число или 'стоп'.")

if max_number is not None:
    print(f"Самое большое число: {max_number}")
else:
    print("Вы не ввели ни одного числа.")