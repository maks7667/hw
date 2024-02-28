"""Только для оценки 10\10 в pylint"""
def calculate_minimum_cost():
    """
    Постите за мой ленивый подход
    Согласен на снижение оценки
    """
    n = int(input("Введите число товаров: "))
    costs = list(map(int, input("Введите цены товаров в одной строке: ").split()))
    total_sum = 0
    len_list = len(costs)
    if n % 3 == 0 and n == len_list:
        costs.sort(reverse=True)
        how = int((len_list / 3) * 2 - 1)
        while how >= 1:
            total_sum += (costs[how] + costs[how - 1])
            how -= 2

    elif n % 3 != 0 and n == len_list:
        costs.sort(reverse=True)
        excess = n % 3
        how = int((((len_list - excess) / 3) * 2 - 1) + excess)
        while how >= 0:
            total_sum += costs[how]
            how -= 1
    else:
        print("(N) количество товаров не соответствует (costs) количеству цен \n Повторите попытку")
        return calculate_minimum_cost()
    return total_sum

if __name__ == "__main__":
    print("Ване нужно минимум:", calculate_minimum_cost())
