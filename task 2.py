import collections


class FirstExampleBuffer:  # Данный класс при использовании библиотеки collections позволят указать
    # максимальное количество символов в буфере тем самым,
    # если количество символов меньше указанного нами новый символ будет добавлен и ничего не удалится,
    # что и подразумивает циклический буфер.
    # Плюсы - удобство, компактный код
    # Минусы -  привлечение стороенней библиотеки
    def __init__(self, len):
        self.deque = collections.deque(maxlen=len)
        self.list = []

    def add(self, numb):
        self.deque.extend(self.list)
        self.deque.append(numb)

    def get(self):
        if self.deque:
            return self.deque.pop()
        else:
            return "Очередь пуста"


class SecondExampleBuffer:  # Данный метод при использовании if\else позволят указать максимальное количество символов
    # в буфере, тем самым,если количество символов меньше указанного нами
    # максимального колчичества новый символ будет добавлен и ничего не удалится,
    # что и подразумевает циклический буфер.
    # Плюсы - Не использует сторонние библиотеки
    # Минусы - Данный способ занимает больше строк кода при одинаковой скорости выполнения.
    def __init__(self, len):
        self.len = len
        self.list = []

    def add(self, numb):
        list_len = len(self.list)
        if list_len >= self.len:
            self.list.pop(0)
            self.list.append(numb)
        else:
            self.list.append(numb)

        return self.list

    def get(self):
        if len(self.list) > 0:
            return self.list.pop(-1)
        else:
            return "Очередь пуста"


if __name__ == '__main__':
    pass
