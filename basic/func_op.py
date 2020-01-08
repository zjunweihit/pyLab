
def SayHello():
    print("Hello there!")

def SayHelloWithName(name):
    print("Hello {}".format(name))

x = 10
def LocalVar(x):
    # NOTE:
    # cannot define that
    #   SyntaxError: name 'x' is parameter and global
    #global x
    print("input x: {}".format(x))
    x = 3
    print("local x: {}".format(x))

# NOTE:
# *param and later become a tuple
# **param and later become a dictionary
def total(a=5, *numbers, **ages):
    print("a", a)

    # iterate all tuple
    for item in numbers:
        print("No.{}".format(item))
    # iterate all dictionary
    for name, age in ages.items():
        print(name, age)

# NOTE:
# DocStrings 的书写惯例是：首行首字母大写，结尾有句号；第二行为空行；第三行以后为详细的描述
def print_max(x, y):
    '''
    Get the max value of two numbers.

    The numbers must be integer.
    '''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


SayHello()
SayHelloWithName("boy")
LocalVar(5)

total(10, 1, 2, 3, Jack=20, Tom=22, Jenny=19)

print_max(3, 6)
print(print_max.__doc__)
