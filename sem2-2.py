k1 = int(input('Сколько учеников в классе 1? \n'))
k2 = int(input('Сколько учеников в классе 2? \n'))
k3 = int(input('Сколько учеников в классе 3? \n'))
if k1 % 2 == 0:
    part1 = k1 / 2
else:
    part1 = k1 // 2 + 1
if k2 % 2 == 0:
    part2 = k2 / 2
else:
    part2 = k2 // 2 + 1
if k3 % 2 == 0:
    part3 = k3 / 2
else:
    part3 = k3 // 2 + 1
print(f'Общее количество парт - {part1 + part2 + part3}')