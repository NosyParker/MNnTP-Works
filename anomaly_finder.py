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
