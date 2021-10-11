import random
import datetime


def random_select(input_list):
    i = random.randint(0, len(input_list)-1)
    
    return input_list[i]


def random_date(fromy, fromm, fromd, toy, tom, tod):
    start_date = datetime.date(fromy, fromm, fromd)
    end_date = datetime.date(toy, tom, tod)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date