import time

def timer(func):
    def wrapper(*args,**kwargs):
       t1 = time.time()
       func(*args,**kwargs)
       t2 = time.time()
       print("time taken by the func to execute is : {}".format(t2-t1))

    return wrapper

@timer
def bigfunc():
    for i in range(1000000):
        i*5



bigfunc()