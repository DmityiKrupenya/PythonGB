n = int(input('Введите трехзначное число; '))
while n // 1000 > 0:
    if n // 1000 > 0:
        print('Число не трехзначное')
        n = int(input('Введите трехзначное число; '))

sum = 0
while n / 10 > 0:
    sum = sum + n % 10
    n = n // 10
print(f'Сумма трехзначного числа: {sum}')