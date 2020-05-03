def square(x):
    return x * x


def cube(x):
    return x * x * x


def my_map(func, args_list):
    result = [func(i) for i in args_list]
    return result


print(my_map(cube, [1, 2, 3, 4, 5]))
print(my_map(square, [1, 2, 3, 4, 5]))


#returning functions and using it

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1=html_tag('h1')
print_h1("Test Headline")

print_p=html_tag('p')
print_p("Test Paragraph")