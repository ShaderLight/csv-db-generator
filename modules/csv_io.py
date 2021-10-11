import csv

def csv_to_list(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        output = []
        for row in csv_reader:
            output.append(row)
    return output


def list_to_csv(filename, input_list, fieldnames):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')

        csv_writer.writeheader()

        for row in input_list:
            csv_writer.writerow(row)

    return 0