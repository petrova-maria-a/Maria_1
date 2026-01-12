print('Введите сумму вклада - рубли')
rub = int(input())
print('ВВедите сумму вклада - копейки')
kop = int(input())
print('Введите процентную ставку')
perc = float(input())
vklad = rub*100+kop
itog = vklad+(vklad/100)*perc
rub = itog//100
kop = itog%100
print(rub, 'руб.', kop, 'коп.')
