import random
import numpy as np

# Генератор базовой случайной величины (БСВ)
def randomValueGenerator():
    while True:
        value = random.uniform(0, 1)
        if value != 0.0 and value != 1.0:
            return value

# Генератор выборки заданного размера
def sequenceGenerator(size):
    return np.asarray([randomValueGenerator() for _ in range(size)])

# Реализация критерия согласия Колмогорова-Смирнова
def kolmogorovSmirnovTestManual(sequence, alpha):
    # Сортировка выборки
    sequence_sorted = np.sort(sequence)

    # Размер выборки
    n = len(sequence)

    # Вычисление эмпирической функции распределения (ЭФР)
    # Создаём массив от 1 до n - размера выборки, и каждый элемент делим на n, чтобы получить доли
    # Каждый элемент показывает, какая доля выборки меньше или равна соответствующему элементу в отсортированной выборке
    # Например, если первый элемен равен 0.1, то ecdf[0] будет равен 1 / n, что соответствует доле выборки, которая меньше или равна 0.1
    ecdf = np.arange(1, n + 1) / n

    # Вычисление теоретической функции распределения (ТФР)
    # (для равномерного распределения совпадает с отсортированной выборкой)
    cdf = sequence_sorted

    # Вычисление максимального отклонения
    d_plus = np.max(np.abs(ecdf - cdf))                                 # Вычисление разницы между ЭФР и ТФР для каждого элемента выборки
    d_minus = np.max(np.abs(ecdf - np.concatenate(([0], cdf[:-1]))))    # Вычисление разницы между ЭФР и ТФР для каждого элемента выборки, но уже с учётом сдвига, чтобы учесть возможные отколенния на концах распределения
    d = max(d_plus, d_minus)                                            # Выбираем максимальное значение из найденных разниц

    # Критическое значение для уровня значимости alpha
    critical_value = np.sqrt(-0.5 * np.log(alpha / 2)) / np.sqrt(n)

    print(f"Уровень значимости: {alpha}")
    print(f"Статистика критерия: {d}")
    print(f"Критическое значение: {critical_value}")

    if d > critical_value:
        print("Гипотеза отвергается - выборка не согласуется с равномерным распределением")
    else:
        print("Гипотеза не отвергается - выборка согласуется с равномерным распределением")
    print()

# Размеры выборок
sequenceSizes = [30, 100, 1000]

# Уровни значимости
alphas = [0.1, 0.05, 0.01]

for size in sequenceSizes:
    sequence = sequenceGenerator(size)
    print(f"Размер выборки: {size}")

    for alpha in alphas:
        kolmogorovSmirnovTestManual(sequence, alpha)
