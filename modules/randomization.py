from datetime import date, timedelta
from random import randint, randrange


# Selects a random element from a list and returns it
def random_select(input_list):
    i = randint(0, len(input_list)-1)
    
    return input_list[i]


# Picks a random date between dates specified in params
def random_date(fromd, fromm, fromy, tod, tom, toy):
    start_date = date(fromy, fromm, fromd)
    end_date = date(toy, tom, tod)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    random_number_of_days = randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    return random_date