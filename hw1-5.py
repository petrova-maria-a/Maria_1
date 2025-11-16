print('Введите число секунд')
sec = int(input())
sec1 = sec % 60
min = sec // 60
hours = min // 60
min1 = min % 60
print(f'{hours}:{min1}:{sec1}')