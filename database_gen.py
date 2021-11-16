from modules.csv_io import list_to_csv
from modules.input_classes import*


def generate_db(output_filename, n, *args):
    output = []
    fieldnames = []

    for field_class in args:
        try:
            fieldnames.append(field_class.name)
        except AttributeError:
            fieldnames.extend(field_class.names)
    
    temp_val = []
    for i in range(len(args)):
        if i == 0:
            output.extend(args[0].generate(n))
            continue
        temp_val = args[i].generate(n)

        for k in range(n):
            output[k].update(temp_val[k])

    return list_to_csv(output_filename, output, fieldnames)

generate_db('output.csv', 4, date_field('d', 1, 1, 2000, 10, 10, 2000))