"""Функция для сортировки"""
def positive_sort(a):
    """Функция для сортировки"""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return " ".join(map(str, a))

if __name__ == "__main__":
    input_list = list(map(int, input("Введите числа через пробел").split()))
    print(positive_sort(input_list))
