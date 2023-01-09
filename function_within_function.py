def add_five(num):
    def add_two(num1):
        return num1+2

    num_plus_two = add_two(num)
    print(num_plus_two +3)

add_five(10)

def get_math_function(operation):
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2

    if operation == "+":
        return add
    elif operation == '-':
        return sub


add_function = get_math_function('+')
print(add_function(2,5))
