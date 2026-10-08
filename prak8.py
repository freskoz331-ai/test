#1
# bits = int(input('разрядность '))
# p = int(input('первое '))
# v = int(input('второе '))
# def to_twos_complement(x, bits):
#     if x >= 0:
#         return x
#     return (1 << bits) + x

# def add_twos_complement(a, b, bits):
#     mask = (1 << bits) - 1
#     result = (a + b) & mask
#     return result


# a = to_twos_complement(p, bits)
# b = to_twos_complement(v, bits)

# result = add_twos_complement(a, b, bits)
# signed_result = result if result < (1 << (bits - 1)) else result - (1 << bits)

# print(signed_result)
# # первое 23
# # второе -9
# # 14

#2
# def to_twos_complement(x, bits):
#     if x >= 0:
#         return x
#     return (1 << bits) + x

# def add_twos_complement(a, b, bits):
#     mask = (1 << bits) - 1
#     result = (a + b) & mask
#     return result

# # Входные данные
# bits = 8
# num1 = 50
# num2 = 20

# # Вычитание num1 - num2 эквивалентно сложению num1 + (-num2)
# a = to_twos_complement(num1, bits)
# b = to_twos_complement(-num2, bits)

# result = add_twos_complement(a, b, bits)
# signed_result = result if result < (1 << (bits - 1)) else result - (1 << bits)

# print(signed_result)
# # 30

#3
# def to_twos_complement(x, bits):
#     if x >= 0:
#         return x
#     return (1 << bits) + x

# def add_twos_complement(a, b, bits):
#     mask = (1 << bits) - 1
#     result = (a + b) & mask
#     return result

# bits = 8
# num1 = 100
# num2 = 50

# a = to_twos_complement(num1, bits)
# b = to_twos_complement(num2, bits)

# result = add_twos_complement(a, b, bits)
# signed_result = result if result < (1 << (bits - 1)) else result - (1 << bits)

# # Границы разрядности
# min_val = -(1 << (bits - 1))
# max_val = (1 << (bits - 1)) - 1
# math_sum = num1 + num2

# print('Полученный  результат:', signed_result)

# # Проверка на переполнение
# if math_sum < min_val or math_sum > max_val:
#     print('Переполнение!')
# else:
#     print("Переполнения нет")

# # Полученный  результат: -106
# # Переполнение!

#4

# # 4 бита
# bits = 4
# min_val = -(1 << (bits - 1))
# max_val = (1 << (bits - 1)) - 1
# print("4 бита:  от", min_val, "до", max_val)

# # 8 бит
# bits = 8
# min_val = -(1 << (bits - 1))
# max_val = (1 << (bits - 1)) - 1
# print("8 бит:   от", min_val, "до", max_val)

# # 16 бит
# bits = 16
# min_val = -(1 << (bits - 1))
# max_val = (1 << (bits - 1)) - 1
# print("16 бит:  от", min_val, "до", max_val)

# # 32 бита
# bits = 32
# min_val = -(1 << (bits - 1))
# max_val = (1 << (bits - 1)) - 1
# print("32 бита: от", min_val, "до", max_val)
# # 4 бита:  от -8 до 7
# # 8 бит:   от -128 до 127
# # 16 бит:  от -32768 до 32767
# # 32 бита: от -2147483648 до 2147483647

#5
# import math

# x = float(input())
# mantissa, exponent = math.frexp(x)

# print(mantissa, exponent)
# # 12.75
# # 0.796875 4

#6

# import math

# x = float(input("Введите число: "))

# mantissa, exponent = math.frexp(x)

# print("Мантисса:", mantissa)
# print("Порядок:", exponent)
# # 12.67
# # 0.791875 

#7
# x = 0.1
# y = sum([0.1 for _ in range(10)])

# print("Сумма:", y)
# print("Точно равно 1.0?:", y == 1.0)

#8
# a = 0.1 + 0.2
# b = 0.3

# print("Результат 0.1 + 0.2:", a)
# print("Число 0.3:", b)

# # Прямое сравнение
# print("Прямое сравнение (a == b):", a == b)

# # Правильное сравнение с погрешностью
# eps = 0.000001
# print("Сравнение с погрешностью:", abs(a - b) < eps)