def iseven2(even):
    return print(True if int(even) & 1 else False)


# Ипользуем побитовый оператор AND(&). Сравниваем, побитно первое число четных чисел всегда 1 а нечетных 0 т.е.
# 1 = 001, 2 = 010, 3 = 011 сраваниваем первое число двоичной системе и получаем что у четных чисел будет False и будет
# возвращаться "Чет" в термиле а у нечетных True и будет возвращаться "Нечет"
# Приемуществом данного метода является тем, что в оперативной памяти хранятся не числа а флажки True\False, что
# позволяет более рационально занимать оперативную память оперативную память.


def iseven1(value):
    return print(value % 2 == 0)


# В данной функции мы делим получаемое число на 2 тем самым определяя её четность.Так же данная функция выполняется
# быстрее.



