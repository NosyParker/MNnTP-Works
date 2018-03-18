import os,sys
import re
import math
import time 

import pandas 
import numpy


def calc_IRTF(csv_file, sep=";"):
    df = pandas.read_csv(csv_file, sep=sep)
    IRTX = pandas.to_numeric(df["IRTX"])
    IRTY = pandas.to_numeric(df["IRTY"])
    IRTZ = pandas.to_numeric(df["IRTZ"])

    df["IRTF"] = IRTX**2 + IRTY**2 + IRTZ**2
    df["IRTF"] = df["IRTF"].pow(1./2).round(3)

    df.to_csv(csv_file, index = False, na_rep = "NaN", sep=sep)


def calc_schedule_meanIRTF(csv_file, sep=";"):
    sum_IRTF = 0
    counter =0
    df = pandas.read_csv(csv_file, sep=sep)
    for minute in range(1440):
        if (0<=minute<=179) or (720<=minute<=899):
            counter += 1
            sum_IRTF += df["IRTF"][minute]
    
    return sum_IRTF/counter


def calc_allday_meanIRTF(csv_file, sep=";"):
    df = pandas.read_csv(csv_file, sep=sep)
    return df["IRTF"].mean()


def calc_year_changes(first_day_csv, last_day_csv, sep=";"):
    first_day_df = pandas.read_csv(first_day_csv, sep=sep)
    last_day_df = pandas.read_csv(last_day_csv, sep=sep)

    return last_day_df["IRTF"][1439] - first_day_df["IRTF"][0]


def main_work(path_to_data):
    start_time = time.time()
    sum_schedule_meanIRTF = 0
    sum_allday_meanIRTF = 0
    for file in os.listdir(path_to_data):
        print (f"Обрабатывается файл - {file} в директории - {path_to_data}")
        calc_IRTF(path_to_data+file)
        sum_schedule_meanIRTF += calc_schedule_meanIRTF(path_to_data+file)
        sum_allday_meanIRTF += calc_allday_meanIRTF(path_to_data+file)

        if "0101" in file or "1231" in file:
            if "0101" in file:
                first_day_csv = file
            else:
                last_day_csv = file
            
    print(f"Изменение вектора за год: {calc_year_changes(path_to_data + first_day_csv, path_to_data+last_day_csv)}")
    print (f"Среднее значение за год в период с 00.00 - 03.00 и с 12.00 - 15.00: {sum_schedule_meanIRTF/365}")
    print (f"Среднее значение за год:  {sum_allday_meanIRTF/365}")
    print (f"Время на всё выполнение заняло - {time.time() - start_time} секунд")


if __name__ == "__main__":
    main_work(sys.argv[1])
