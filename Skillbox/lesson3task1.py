print('Таблица умножения')
b = 1
while b <= 9:
  for a in range(1, 10):
    print(a, '*', b, '=', a * b)
  print('\t')
  b += 1