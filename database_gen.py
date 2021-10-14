from modules.input_classes import*
from modules.csv_io import list_to_csv


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