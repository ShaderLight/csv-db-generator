class csv_field:
    def __init__(self, input_filename, fieldname):
        self.input_filename = input_filename
        self.fieldname = fieldname
    
    def generate(self, n):
        pass
    

class date_field:
    def __init__(self, from_d, from_m, from_y, to_d, to_m, to_y):
        self.from_d = from_d
        self.from_m = from_m
        self.from_y = from_y
        self.to_d = to_d
        self.to_m = to_m
        self.to_y = to_y

    def generate(self, n):
        pass


class randint_field:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def generate(self, n):
        pass


class id_field:
    def __init__(self):
        pass
    
    def generate(n):
        pass