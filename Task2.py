# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# 7 -> "нельзя определить"

all = int(input("Введите общее число журавликов -> "))
if all % 2 == 0:
    Katya = all // 2
    Sergey = Katya // 2
    Petr = Sergey
    print(f'Катя = {Katya}; Серёжа = {Sergey}; Петя = {Petr}')
elif all % 2 != 0:
    print('Нельзя определить!')