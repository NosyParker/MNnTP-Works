## Anomaly detection of geomagnetic station`s time series
***
## Выявление выбросов в рядах данных геомагнитных станций
***
## HowTo:
1. Convert **IAGA-2002**-files into standard **CSV** for Pandas processing:
    1.1 Use **make_csv_from_original_data** and **replace_spaces_with_semicolon**  from **clear_csv_maker** module.
    1.2 Loop data folder with that one`s.
    1.3 See **main.py** for example.

***
## Использование:
1. Конвертируйте **IAGA-2002**-файлы в обычный **CSV** -формат для дальнейшей обработки с Pandas:
    1.1 Используйте **clear_csv_maker** модуль для выполнения конвертации, а именно: функции **make_csv_from_original_data** и **replace_spaces_with_semicolon**.
    1.2 Примените их в цикле для своего набора данных.
    1.3 Пример показан в **main.py**.

***    
#TBD ... 
#Репозиторий и README постепенно обновляются
