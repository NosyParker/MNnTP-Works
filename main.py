import os
import re
from clear_csv_maker import make_csv_from_original_data, replace_spaces_with_semicolon

new_path = "./out_csv/"
counter = 0
for file in os.listdir("data"):
    if file.endswith(".min"):
        out_csv_file = new_path + file + ".csv"
        print ("Обрабатывается - ".format(file))
        make_csv_from_original_data("./data/" + file, out_csv_file)
        replace_spaces_with_semicolon(out_csv_file)
        counter+=1

print ("Обработано файлов - {}".format(counter))

