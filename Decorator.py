def decorator_function(original_func):
    def wrapper_function(*args,**kwargs):
        print('Wrapper executed this before : {}'.format(original_func.__name__))
        return original_func(*args,**kwargs)

    return wrapper_function


@decorator_function
def display():
    print('display function ran')

display()

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name,age))


display_info('Ajay', 26)

