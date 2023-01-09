def title_decorator(print_name_function):
    def wrapper():#function within funtion which decorates and add another thing
        print('Mr')
        print_name_function()#calling the arguement of the function
    return wrapper()

def print_my_name():
    print('Savvas')

decorator_function = title_decorator(print_my_name)#adding as parameter another function
decorator_function

#with decorator we place the function that we will use the other function as decorator
def title_decorator(print_name_function):
    def wrapper():#function within funtion which decorates and add another thing
        print('Mr')
        print_name_function()#calling the arguement of the function
    return wrapper()

@title_decorator #that is the decorator where you place
def print_my_name():
    print('Savvas')

print_my_name