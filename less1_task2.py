n = int(input('Введите число от 1 до 9: '))

n_str = str(n)
two_n = n_str + n_str
three_n = n_str + n_str + n_str

print(two_n)
n_sum = n + int(two_n) + int(three_n)

print(n_sum)