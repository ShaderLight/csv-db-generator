from csv import DictReader, DictWriter

def csv_to_list(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        csv_reader = DictReader(f, delimiter=';')
        output = []
        for row in csv_reader:
            output.append(row)
    return output


def list_to_csv(filename, input_list, fieldnames):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        csv_writer = DictWriter(f, fieldnames=fieldnames, delimiter=';')

        csv_writer.writeheader()

        print(fieldnames)
        print(input_list)
        for row in input_list:
            print(row)
            csv_writer.writerow(row)

    return 0