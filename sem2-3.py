inp = input('Введите что-нибудь \n')
try:
    i = float(inp)
    j = i + 1
    print(j)
except ValueError:
    print(f'{inp} не число')

