import random
# random.seed(45)
i = random.randint (1,100)
p = 0
counter = 0
while p != i:
    p = int(input('Введи число!'))
    if p > i: 
        print('-')
    else:
        print('+')
    counter += 1
print('Молодец, угадал! Количество попыток', counter)
print(i)