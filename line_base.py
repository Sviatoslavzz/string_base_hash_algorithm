option = int(input("Введите 1 для ввода строки из консоли / введите 2 для загрузки строки из файла\n"))
if option == 1:
    s = input("Введите строку: ")
else:
    path = input("Введите путь к файлу: ")
    with open(path, "r") as file:
        s = file.read()

x = 257
p = 10 ** 9 + 7
h = [0]
x_list = [0]
res = 0
mul_x = 1
n = len(s)
for i in range(n):
    res = ((res * x) + ord(s[i])) % p
    h.append(res)
    mul_x = (mul_x * x) % p
    x_list.append(mul_x)


def string_compare(len_sub, start_1, start_2):
    return (h[start_1 + len_sub] + h[start_2] * x_list[len_sub]) % p == (
            h[start_2 + len_sub] + h[start_1] * x_list[len_sub]) % p


i = 0
k = 1
equal_arr = []
while k != n:  # or k <= n // 2 + 1
    if string_compare(1, i, k) and not string_compare(1, i, k - 1):
        equal_arr.append(k)
    if string_compare(1, i, k) and k == n - 1:
        equal_arr.append(k)
    k += 1

sym_count = len(equal_arr)

if sym_count == 0 or sym_count == 1:
    if string_compare(1, i, n - 1):
        print(1)
    else:
        print(n)
else:
    equal_arr.insert(0, 0)
    part_len = n - equal_arr[-1]
    result = n
    i = 0
    is_equal = False
    while len(equal_arr) != 1:
        k = equal_arr[-1]
        if string_compare(part_len, i, k):
            is_equal = True

        equal_arr = equal_arr[:-1]

        if is_equal:
            result = k  # at least

        part_len += k - equal_arr[-1]
        is_equal = False

    print(f"Минимальная возможная длина исходной строки = {result}")