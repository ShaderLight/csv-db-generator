from random import randint

from .randomization import random_date, random_select
from .csv_io import csv_to_list

class csv_field:
    def __init__(self, names, input_filename, input_fieldnames=None):
        self.input_filename = input_filename
        
        if type(names) != list:
            self.names = [names]
        else:
            self.names = names

        if input_fieldnames == None:
            self.input_fieldnames = self.names
        elif type(input_fieldnames) != list:
            self.input_fieldnames = [input_fieldnames]
        else:
            self.input_fieldnames = input_fieldnames

    def generate(self, n):
        output = []
        data = csv_to_list(self.input_filename)

        for i in range(n):
            temp_dict = {}
            for k in range(len(self.input_fieldnames)):
                selected = random_select(data)
                temp_dict[self.names[k]] = selected[self.input_fieldnames[k]]
            output.append(temp_dict)
        
        return output

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
            output.append({self.name : rng_date})

        return output


class randint_field:
    def __init__(self, name, a, b, unique=False):
        self.name = name
        self.a = a
        self.b = b
        self.unique = unique
    

    def generate(self, n):
        used_numbers = []
        output = []
        for i in range(n):
            rint = randint(self.a, self.b)
            if self.unique:
                if rint in used_numbers:
                    continue
            output.append({self.name : randint(self.a, self.b)})
            used_numbers.append(used_numbers)

        return output


class id_field:
    def __init__(self, name='id'):
        self.name = name
    
    def generate(self, n):
        output = []
        for i in range(n):
            output.append({self.name : i+1})

        return output