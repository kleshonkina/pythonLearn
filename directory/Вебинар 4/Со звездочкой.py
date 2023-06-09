# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974
def get_digits(num):
    digits = [int(digit) for digit in str(num)]
    return list(digits)


def get_num(digits):
    r = ''
    for digit in digits:
        r += str(digit)
    return int(r)


def max_division_by_3(num):
    digits = get_digits(num)
    s = sum(digits)
    dx = 3 - s % 3
    changed = False
    for j in range(len(digits)):
        if digits[j] + dx <= 9:
            changed = True
            digits[j] += dx
            digits[j] += (9 - digits[j]) // 3 * 3
            break
    if not changed:
        for j in range(len(digits) - 1, -1, -1):
            if digits[j] - dx >= 0:
                digits[j] -= dx
                break
    new_num = get_num(digits)
    return new_num


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]
test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]
for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
