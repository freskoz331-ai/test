# from math import *

# # # Задание 1
# p = [0.7, 0.1, 0.1, 0.1]
# h = -sum(pi * log2(pi) for pi in p)
# print(h)
# # 1.3567796494470397
# # так как вероятности сильно отличаются, энтропия меньше, чем при равновероятных


# # # Задание 2
# message = "АААВАСАА"

# # фиксированный код:
# code_fixed = {'А': '00', 'В': '01', 'С': '10'}
# encode_fixed = ''.join(code_fixed[x] for x in message)
# print(len(encode_fixed))

# # переменный код:
# code_var = {'А': '0', 'В': '10', 'С': '11'}
# encode_var = ''.join(code_var[x] for x in message)
# print(len(encode_var))

# # экономия
# print(len(encode_fixed) - len(encode_var))
# # 16
# # 10
# # 8
# # экономия битов при использовании переменного кода составляет 8 битов


# # Задание 3
# def encode(data_bits):
#     d1, d2, d3, d4 = (int(x) for x in data_bits)
#     p1 = d1 ^ d2 ^ d4
#     p2 = d1 ^ d3 ^ d4
#     p4 = d2 ^ d3 ^ d4
#     code = [p1, p2, d1, p4, d2, d3, d4]
#     return ''.join(str(x) for x in code)

# def syndrome(code_bits):
#     b = [int(x) for x in code_bits]
#     s1 = b[0] ^ b[2] ^ b[4] ^ b[6]
#     s2 = b[1] ^ b[2] ^ b[5] ^ b[6]
#     s4 = b[3] ^ b[4] ^ b[5] ^ b[6]
#     return s1 * 1 + s2 * 2 + s4 * 4

# def correct(code_bits):
#     b = [int(x) for x in code_bits]
#     pos = syndrome(code_bits)
#     if pos != 0:
#         b[pos - 1] ^= 1
#     return ''.join(str(x) for x in b)

# data = "0110"
# code = encode(data)

# broken = list(code)
# # меняем 7-й бит (индекс 6)
# if broken[6] == '1':
#     broken[6] = '0'
# else:
#     broken[6] = '1'
# broken = ''.join(broken)

# syn = syndrome(broken)
# fixed = correct(broken)
# extracted = fixed[2] + fixed[4] + fixed[5] + fixed[6]

# print(data)
# print(code)
# print(broken)
# print(syn)
# print(fixed)
# print(extracted)
# # 0110
# # 1100110
# # 1100111
# # 7
# # 1100110
# # 0110


# # # Задание 4
# num = -45
# bits = 8

# # прямой код
# dv = format(abs(num), f"0{bits-1}b")
# dv_1 = "1" + dv
# print(dv_1)

# # обратный код
# direct = dv_1
# inv = "".join(str(int(not int(b))) for b in direct)
# inv = '1' + inv[1:]
# print(inv)

# # дополнительный код
# twos = format(int(inv, 2) + 1, "08b")
# print(twos)

# # обратное восстановление из прямого кода
# mag_val = int(dv, 2)
# val_dir = mag_val * -1
# print("восстановление из прямого:", val_dir)

# # обратное восстановление из обратного кода
# inv_magnitude_str = "".join(str(int(not int(b))) for b in inv[1:])
# inv_mag_val = int(inv_magnitude_str, 2)
# val_inv = inv_mag_val * -1
# print("восстановление из обратного:", val_inv)

# # обратное восстановление из дополнительного кода
# raw_twos_val = int(twos, 2)
# if twos[0] == '1':
#     val_twos = raw_twos_val - (1 << bits)
# else:
#     val_twos = raw_twos_val
# print("восстановление из дополнительного:", val_twos)
# # 10101101
# # 11010010
# # 11010011
# # восстановление из прямого: -45
# # восстановление из обратного: -45
# # восстановление из дополнительного: -45


# # # Задание 5
# import math

# numbers = [12.75, 10.5, 3.625, 0.375]
# for x in numbers:
#     # 1. Твой вариант ручного перевода (целая и дробная части)
#     whole = int(x)
#     frac = x - whole
#     bin_whole = bin(whole)[2:]
#     bin_frac = ""
#     f = frac
#     for _ in range(8):
#         f *= 2
#         bit = int(f)
#         bin_frac += str(bit)
#         f -= bit
#     full_bin = f"{bin_whole}.{bin_frac}"
    
#     # Ручной порядок (сдвиг запятой до вида 1.xxxxx)
#     if whole > 0:
#         manual_exponent = len(bin_whole) - 1 
#     else:
#         manual_exponent = -bin_frac.find('1') - 1
#     print("число:", x)

#     print("ручной двоичный перевод:", full_bin)
#     print("ручной порядок:", manual_exponent)
    
#     # 2. Результаты math.frexp()
#     mantissa, exponent = math.frexp(x)
#     print("math.frexp -> мантисса:", mantissa)
#     print("math.frexp -> порядок:", exponent)
    
#     restored = mantissa * (2 ** exponent)
#     print("восстановленное через frexp:", restored)
    
#     print()
# # число: 12.75
# # ручной двоичный перевод: 1100.11000000
# # ручной порядок: 3
# # math.frexp -> мантисса: 0.796875
# # math.frexp -> порядок: 4
# # восстановленное через frexp: 12.75

# # число: 10.5
# # ручной двоичный перевод: 1010.10000000
# # ручной порядок: 3
# # math.frexp -> мантисса: 0.65625
# # math.frexp -> порядок: 4
# # восстановленное через frexp: 10.5

# # число: 3.625
# # ручной двоичный перевод: 11.10100000
# # ручной порядок: 1
# # math.frexp -> мантисса: 0.90625
# # math.frexp -> порядок: 2
# # восстановленное через frexp: 3.625

# # число: 0.375
# # ручной двоичный перевод: 0.01100000
# # ручной порядок: -2
# # math.frexp -> мантисса: 0.75
# # math.frexp -> порядок: -1
# # восстановленное через frexp: 0.375
