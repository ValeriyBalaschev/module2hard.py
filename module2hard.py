# module2hard.py Дополнительное практическое задание по модулю: "Основные операторы"
code_1 = int(input('Введите целое число в диапазоне от 3 до 20: '))
result = ''
for part_1 in range(1, code_1+1):
      for part_2 in range(part_1 + 1, code_1 + 1):
           if code_1 % (part_1 + part_2) == 0:
            result = result + str(part_1 ) + str(part_2)

print('Пароль: ', result)
