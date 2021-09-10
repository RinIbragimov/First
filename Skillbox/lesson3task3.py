action = str(input('Выберите операцию: \n"+" - сложение, "-" - вычитание, "*" - умножение, "/" - деление\n'))

while True:
  if (action != '+') and (action != '-') and (action != '*') and (action != '/'):
    action = str(input('Ошибка. Такой операции не существует. Попробуйте еще раз. '))
  else:
    break

operand = int(input('Сколько операндов? '))

print('Введите операнд 1 : ', end = '')
result = int(input())
answer = str(result) + ' ' + action + ' '

for num in range(2, operand + 1):
  print('Введите операнд', num, ': ', end = '')
  number = int(input())

  if action == '+':
    result += number
    number = str(number)
    answer += number + ' + '
  elif action == '-':
    result -= number
    number = str(number)
    answer += number + ' - '
  elif action == '*':
    result *= number
    number = str(number)
    answer += number + ' * '
  elif action == '/':
    result /= number
    number = str(number)
    answer += number + ' / '

print(answer.strip(action + ' '), ' =', result)

