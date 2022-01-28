def findSmallest(arr):  # Способ 1
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


@profile
def sort1(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


@profile
def sort2(arr):  # Способ 2
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort2(less) + equal + sort2(greater)
    else:
        return arr


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


@profile
def sort3(arr, begin=0, end=None):  # Способ 3
    if end is None:
        end = len(arr) - 1

    def _quicksort(arr, begin, end):
        if begin >= end:
            return
        pivot = partition(arr, begin, end)
        _quicksort(arr, begin, pivot - 1)
        _quicksort(arr, pivot + 1, end)

    return _quicksort(arr, begin, end)


if __name__ == "__main__":
    sort1([5, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10])  # Способ 1
    sort2([5, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10])  # Способ 2
    sort3([5, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10])  # Способ 3

# При проверке файла  kernprof -l -v task3.py
# Если мы разберем данные три способа сортировки, то можно отметить что наименьшее время выполнение функции у третьего
# способа, но если рассмотреть с точки зрения работы каждой функции можно обратить внимание что среднее время выполнения
# каждой строки у способа номер  два будет ниже.

