import collections
import time
from datetime import datetime

start_time = time.time()


class FirstExampleBuffer:  # Данный метод при использовании библиотеки collections позволят указать
    # максимальное количество символов в буфере тем самым,
    # если количество символов меньше указанного нами новый символ будет добавлен и ничего не удалится,
    # что и подразумивает циклический буфер.
    def __init__(self, len, numb, list):
        self.len = len
        self.numb = numb
        self.list = list

    def example(self):
        result = collections.deque(maxlen=self.len)
        result.extend(self.list)
        result.append(self.numb)
        print(result)
        print(time.time() - start_time)


start_time = time.time()


class SecondExampleBuffer:  # Данный метод при использовании if\else позволят указать максимальное количество символов
    # в буфере, тем самым,если количество символов меньше указанного нами
    # максимального колчичества новый символ будет добавлен и ничего не удалится,
    # что и подразумевает циклический буфер. Данный способ занимает больше
    # строк кода при одинаковой скорости выполнения.
    def __init__(self, len, numb, list):
        self.numb = numb
        self.len = len
        self.list = list

    def example(self):
        list_len = len(self.list)
        if list_len == self.len:
            self.list.append(self.numb)
            self.list.pop(0)
        else:
            self.list.append(self.numb)

        print(self.list)
        print(time.time() - start_time)


first = FirstExampleBuffer(7, 145,
                           [25, 4, 5, 123, 9, 33, 4, 5, 123, 9, 33, 4, 5, 123, 9, 33, 4, 5, 123, 9, 33, 4, 5, 123, 9,
                            33, 4, 5, 123, 9, 33, 4, 5, 123, 9, 33])
second = SecondExampleBuffer(100, 12,
                             [12, 2, 7, 8, 16, 4, 5, 123, 9, 33, 4, 5, 123, 9, 33, 4, 5, 123, 9, 33, 4, 5, 123, 9, 33,
                              4, 5, 123, 9, 33, 4, 5, 123, 9, 33])
first.example()
second.example()
