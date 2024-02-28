"""Описание функций"""
def negative_sort(a):
    """Описание функций"""
    n = len(a)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return " ".join(map(str, a))

if __name__ == "__main__":
    input_list = list(map(int, input("Введите числа через пробел").split()))
    print(negative_sort(input_list))
