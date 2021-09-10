def calculate(first_num, second_num, action):
  if action == '+':
    print(first_num, '+', second_num, '=', first_num + second_num)
  elif action == '-':
    print(first_num, '-', second_num, '=', first_num - second_num)
  elif action == '*':
    print(first_num, '*', second_num, '=', first_num * second_num)
  elif action == '/':
    print(first_num, '/', second_num, '=', first_num / second_num)


action = str(input('Выберите операцию: \n"+" - сложение, "-" - вычитание, "*" - умножение, "/" - деление\n'))

while True:
  if (action != '+') and (action != '-') and (action != '*') and (action != '/'):
    action = str(input('Ошибка. Такой операции не существует. Попробуйте еще раз. '))
  else:
    break

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

calculate(first_num, second_num, action)