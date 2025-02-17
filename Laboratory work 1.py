import random
import numpy as np
from scipy.stats import kstest

def randomValueGenerator():
    while True:
        value = random.uniform(0, 1)

        if value != 0.0 and value != 1.0:
            return value
        else:
            return randomValueGenerator()

# Проверка работы генератора
#print(randomValueGenerator())

def sequenceGenerator(size):
    return np.asarray([randomValueGenerator() for _ in range(size)])

def kolmogorovSmirnovTest(sequence, alpha):
    result = kstest(sequence, 'uniform', args = (0, 1))

    print(f"Уровень значимости: {alpha}")
    print(f"Статистика-критерия: {result.statistic}")
    print(f"P-значение: {result.pvalue}")

    if result.pvalue < alpha:
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
        kolmogorovSmirnovTest(sequence, alpha)
