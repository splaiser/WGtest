import time


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


@profile
def sort3(arr):  # Способ 3
    def _quicksort(arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            _quicksort(arr, low, p)
            _quicksort(arr, p + 1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        while True:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low >= high:
                return high
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    _quicksort(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    # Не упорядоченный список
    print(sort1([5, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10]))  # Способ 1
    print(sort2([5, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10]))  # Способ 2
    print(sort3([5, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10, 3, 6, 2, 10]))  # Способ 3
    # Упорядоченный список
    print(
        sort1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))  # Способ 1
    print(
        sort2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))  # Способ 2
    print(
        sort3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))  # Способ 3

# При проверке файла  kernprof -l -v task3.py
# Если мы разберем данные три способа сортировки, то можно отметить, что время выполнение функции у второго способа на порядок выше,
# тем временем у первого и второго незначительно отличаются.
