import numpy as np
import matplotlib.pyplot as plt

# Функция для генерации нормальной случайной величины методом суммирования
def generateNormalRandomVariable(a, sigma, n=12):
    # Генерация нормальной случайной величины методом суммирования

    # Параметры:
    # a (float): математическое ожидание
    # sigma (float): среднеквадратическое отклонение
    # n (int): количество суммируемых случайных величин (по умолчанию 12)

    # Возвращает:
    # float: нормально распределённая случайная величина

    # Суммируем n равномерно распределённых случайных величин
    sumUniform = sum(np.random.uniform(0, 1, n))

    # Преобразуем сумму в нормально распределённую величину
    z = (sumUniform - n / 2) / np.sqrt(n / 12)

    # Масштабируем и сдвигаем величину
    return a + sigma * z


# Функция для генерации выборки нормальных случайных величин
def generateNormalVariableSample(a, sigma, size=1000):
    # Генерация выборки нормальных случайных величин

    # Параметры:
    # a (float): математическое ожидание
    # sigma (float): среднеквадратическое отклонение
    # size (int): размер выборки

    # Возвращает:
    # list: выборка нормальных случайных величин

    return [generateNormalRandomVariable(a, sigma) for _ in range(size)]


# Функция для построения гистограммы
def buildHistogram(sample, h, a, sigma, sample_size):
    # Построение гистограммы для выборки

    # Параметры:
    # sample (list): выборка нормальных случайных величин
    # h (float): шаг гистограммы
    # a (float): математическое ожидание
    # sigma (float): среднеквадратическое отклонение
    # sample_size (int): размер выборки (для заголовка графика)

    # Определяем границы гистограммы
    bins = np.arange(min(sample), max(sample) + h, h)

    # Строим гистограмму
    plt.hist(sample, bins=bins, density=True, alpha=0.6, color='g', label='Экспериментальная плотность')

    # Добавляем теоретическую плотность нормального распределения
    x = np.linspace(a - 4 * sigma, a + 4 * sigma, 1000)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - a) / sigma) ** 2)
    plt.plot(x, y, 'r-', label='Теоретическая плотность')

    # Настройки графика
    plt.title(f'Гистограмма выборки (размер = {sample_size})')
    plt.xlabel('Значение')
    plt.ylabel('Плотность вероятности')
    plt.legend()
    plt.grid(True)
    plt.show()


# Функция для проверки закона "трёх сигм"
def checkThreeSigmaRule(sample, a, sigma):
    # Проверка выполнения закона "трёх сигм"

    # Параметры:
    # sample (list): выборка нормальных случайных величин
    # a (float): математическое ожидание
    # sigma (float): среднеквадратическое отклонение

    # Вычисляем количество элементов в интервалах
    withinSigma1 = sum(a - sigma <= x <= a + sigma for x in sample)
    withinSigma2 = sum(a - 2 * sigma <= x <= a + 2 * sigma for x in sample)
    withinSigma3 = sum(a - 3 * sigma <= x <= a + 3 * sigma for x in sample)

    # Вычисляем доли элементов в интервалах
    proportionSigma1 = withinSigma1 / len(sample)
    proportionSigma2 = withinSigma2 / len(sample)
    proportionSigma3 = withinSigma3 / len(sample)

    # Выводим результаты
    print(f"Доля элементов в пределах 1 сигмы: {proportionSigma1:.4f} (ожидается ~0.6827)")
    print(f"Доля элементов в пределах 2 сигм: {proportionSigma2:.4f} (ожидается ~0.9545)")
    print(f"Доля элементов в пределах 3 сигм: {proportionSigma3:.4f} (ожидается ~0.9973)")


# Параметры распределения
a = 5  # Математическое ожидание
sigma = 2  # Среднеквадратическое отклонение
h = 0.5  # Шаг гистограммы

# Массив размеров выборок
sampleSizes = [10, 100, 1000, 10000, 100000, 1000000]

# Генерация выборок, построение гистограмм и проверка закона "трёх сигм"
for size in sampleSizes:
    print(f"\nРазмер выборки: {size}")
    # Генерация выборки
    sample = generateNormalVariableSample(a, sigma, size)
    # Построение гистограммы
    buildHistogram(sample, h, a, sigma, size)
    # Проверка закона "трёх сигм"
    checkThreeSigmaRule(sample, a, sigma)
