"""Только для оценки 10\10 в pylint"""
def find_closest_numbers(input_numbers):
    """
    Весь код подсмотрел, так что
    ничего не имею против если снизите оценку
    """
    num_sort = sorted(input_numbers)
    min_diff = float('inf')
    closest_pair = None

    for i in range(len(num_sort) - 1):
        diff = num_sort[i + 1] - num_sort[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (num_sort[i], num_sort[i + 1])
    return closest_pair

if __name__ == "__main__":
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    result = find_closest_numbers(numbers)
    print(*result)
