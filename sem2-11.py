try:
    kat1 = float(input('Введите катет 1 \n'))
    kat2 = float(input('Введите катет 1 \n'))
except ValueError:
    print("Нужно вводить только числа")
else:
    s = kat1 * kat2 / 2
    print(f'Площадь треугольника равна {s} кв.см')