

def sum (number1: int, number2: int) -> int:
    if number2 == 0:
        return number1
    return 1 + sum(number1, number2-1)
numbers1 = int(input('Введите число1: '))
numbers2 = int(input('Введите число2: '))
print(sum(numbers1, numbers2))