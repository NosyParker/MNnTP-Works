from itertools import count
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import collections


def calc_moving_average(data, window_size):
    """ Функция для расчета "скользящего среднего".

    """
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(data, window, 'same')


def explain_anomalies_rolling_std(y, window_size, sigma=1.0):
    """ Функция для расчета стандартного отклонения.

        Возвращает хэш, содержащий информацию об аномалиях (индекс, значение) и значениях стандартного отклонения.
    """
    avg = calc_moving_average(y, window_size)
    avg_list = avg.tolist()
    residual = y - avg

    testing_std = pd.rolling_std(residual, window_size)
    testing_std_as_df = pd.DataFrame(testing_std)
    rolling_std = testing_std_as_df.replace(np.nan,
                                  testing_std_as_df.ix[window_size - 1]).round(3).iloc[:,0].tolist()
    std = np.std(residual)
    return {'stationary standard_deviation': round(std, 3),
            'anomalies_dict': collections.OrderedDict([(index, y_i)
                                                       for index, y_i, avg_i, rs_i in zip(count(),
                                                                                           y, avg_list, rolling_std)
              if (y_i > avg_i + (sigma * rs_i)) | (y_i < avg_i - (sigma * rs_i))])}


def plot_results(x, y, window_size, sigma_value=1,
                 text_xlabel="Минуты *какого-то дня*", text_ylabel="Значение *характеристики*"):
    """ 
    Генерирует график и отмечает звездочками на нем аномалии.

    """
    plt.figure(figsize=(15, 8))
    plt.plot(x, y, "k.", markersize=16)
    y_av = calc_moving_average(y, window_size)
    plt.plot(x, y_av, color='green')
    plt.xlabel(text_xlabel)
    plt.ylabel(text_ylabel)

    events = {}
    events = explain_anomalies_rolling_std(y, window_size=window_size, sigma=sigma_value)


    x_anomaly = [x for x in events["anomalies_dict"].keys()]
    y_anomaly = [y for y in events["anomalies_dict"].values()]
    print(x_anomaly, "Минуты")
    print(y_anomaly, "Значения")
    plt.plot(x_anomaly, y_anomaly, "r*", markersize=12)

    plt.grid(True)
    plt.show()


def anomaly_to_nan(data, column, indexes_of_events, output_csv):
    """ 
    Заменяет аномальные значения в датасете (data) для указанной характеристики (параметр column) на NaN,
    используя индексы аномалий (indexes_of_events), и записывает датасет в выходной CSV (output_csv).

    """
    for row, value in enumerate(data[column]):
        for index, val in enumerate(indexes_of_events):
            if row == val:
                data[column][row] = None

    data.to_csv(output_csv, index = False, na_rep = "NaN", sep=";")