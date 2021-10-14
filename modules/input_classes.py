from .randomization import random_date
import random

class csv_field:
    def __init__(self, name, input_filename, input_fieldnames):
        self.name = name
        self.input_filename = input_filename
        self.input_fieldnames = input_fieldnames
        self.name = name
    
    def generate(self, n):
        pass


class date_field:
    def __init__(self, name, from_d, from_m, from_y, to_d, to_m, to_y):
        self.name = name
        self.from_d = from_d
        self.from_m = from_m
        self.from_y = from_y
        self.to_d = to_d
        self.to_m = to_m
        self.to_y = to_y

    def generate(self, n):
        output = []
        for i in range(n):
            rng_date = random_date(self.from_d, self.from_m, self.from_y, self.to_d, self.to_m, self.to_y)
            output.append(rng_date)

        return output


class randint_field:
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b
    
    def generate(self, n):
        output = []
        for i in range(n):
            output.append(random.randint(self.a, self.b))

        return output


class id_field:
    def __init__(self, name='id'):
        self.name = name
    
    def generate(n):
        output = []
        for i in range(n):
            output.append(i+1)

        return output