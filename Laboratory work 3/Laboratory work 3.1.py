import numpy as np

# Функция плотности вероятности
def probabilityDensity(x):
    return (7 * (x + 1)**(3/4)) / (4 * (2**(7/4) - 1))

# Функция распределения
def distributionFunction(x):
    return ((x + 1)**(7/4) - 1) / (2**(7/4) - 1)

# Обратная функция распределения
def inverseDistributionFunction(y):
    return (y * (2**(7/4) - 1) + 1)**(4/7) - 1

# Генерация случайной величины методом обратной функции
def generateRandomVariable(size = 1):
    u = np.random.uniform(0, 1, size)
    return inverseDistributionFunction(u)

# Вычисление математического ожидания
def expectedValue():
    return (7 / (4 * (2**(7/4) - 1))) * (
        (4 / 11) * (2**(11/4) - 1) - (4 / 7) * (2**(7/4) - 1)
    )

# Вычисление дисперсии
def variance():
    expValue = expectedValue()
    secondPoint = (7 / (4 * (2**(7/4) - 1))) * (
        (4 / 15) * (2**(15/4) - 1) - (8 / 11) * (2**(11/4) - 1) + (4 / 7) * (2**(7/4) - 1)
    )
    return secondPoint - expValue**2

# Массив размеров выборки
sampleSizes = [10, 100, 1000, 10000, 100000, 1000000]

# Теоретические значения
theoreticalExpectedValue = expectedValue()
theoreticalVariance = variance()

# Вычисление для каждого размера выборки
for sampleSize in sampleSizes:
    randomValues = generateRandomVariable(sampleSize)
    
    # Выборочное среднее
    sampleAverage = np.mean(randomValues)
    
    # Выборочная дисперсия
    sampleVariance = np.var(randomValues, ddof=1)
    
    print(f"\nРазмер выборки: {sampleSize}")
    print(f"Теоретическое матожидание: {theoreticalExpectedValue:.6f}")
    print(f"Выборочное среднее: {sampleAverage:.6f}")
    print(f"Теоретическая дисперсия: {theoreticalVariance:.6f}")
    print(f"Выборочная дисперсия: {sampleVariance:.6f}")

