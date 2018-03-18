import os
import time

from .clear_csv_maker import make_csv_from_original_data
from .clear_csv_maker import replace_spaces_with_semicolon


def folder_processing(original_path_or_dir: str, out_path_or_dir: str, comments_end = 24) -> None:
    """
        Функция для трансформации наборов исходных IAGA-2002 файлов, хранящихся в 
        :original_path_or_dir директории, и получении выходных csv-файлов в
        :out_path_or_dir директорию.
    """
    counter = 0
    start_time = time.time()
    for file in os.listdir(original_path_or_dir):
        if file.endswith(".min"):
            out_csv = out_path_or_dir + file + ".csv"
            print (f"Processing --- {file}")
            make_csv_from_original_data(original_path_or_dir + file, out_csv, comments_end=comments_end)
            replace_spaces_with_semicolon(out_csv)
            counter += 1
    print (f"Processing is over.\nThere were processed {counter} files with {(time.time() - start_time)} seconds.")