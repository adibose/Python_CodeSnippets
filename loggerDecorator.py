from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args : {} and kwargs : {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        orig_func(*args, **kwargs)
        t2 = time.time()-t1
        print('{} ran in {} secs'.format(orig_func.__name__, t2))

    return wrapper



# @my_logger
# def display_info(name, age):
#     print('display_info ran with arguments {},{}'.format(name, age))
#
#
# display_info('Jane',29)

@my_logger
@my_timer
def random_record(number):
    import random
    names = ["Aditya", "Arif", "Arnab", "Arko", "Riddhi", "Pallabi", "Sunny", "Pamela", "Monica"]
    majors = ["Maths", "English", "Computer Science", "History"]
    for i in range(number):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        print(person)

random_record(1000000)
