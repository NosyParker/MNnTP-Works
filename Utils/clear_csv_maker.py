import re

def make_csv_from_original_data(original_filename, output_csv):
    original_file = open(original_filename, "r")

    lines = original_file.readlines()
    original_file.close()

    output_csv = open(output_csv, "w")

    for line in lines[28:]:
        output_csv.write(line)

    output_csv.close()


def replace_spaces_with_semicolon(raw_csv):
    correct_lines = []

    with open(raw_csv, "r") as input_file:
        for line in input_file:
            line = re.sub(r"\s+", ";", line)
            line = line[:-1]
            line = line + "\n"
            correct_lines.append(line)

    correct_lines[0] = re.sub(r";\|","",correct_lines[0])

    with open(raw_csv, "w") as output_file:
        for correct_line in correct_lines:
            output_file.write(correct_line)

            