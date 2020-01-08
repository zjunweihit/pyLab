import functools

def trace(func):
    def wappter(*args, **kwargs):
        print("call func: {}".format(func.__name__))
        return func(*args, **kwargs)
    return wappter

@trace
def myFunc(input):
    print("this is my function: input {}".format(input))


def trace2(func):
    @functools.wraps(func)
    def wappter(*args, **kwargs):
        print("call func: {}".format(func.__name__))
        return func(*args, **kwargs)
    return wappter
@trace2
def myFuncWithMyName(input):
    print("this is my function: input {}".format(input))


def traceFile(fileName):
    def trace(func):
        def wappter(*args, **kwargs):
            print("call func: {} to file {}".format(func.__name__, fileName))
            return func(*args, **kwargs)
        return wappter
    return trace

@traceFile("log.txt")
def myFuncFile(input):
    print("this is my file function: input {}".format(input))


myFunc("test")
myFuncFile("test2")

print("myFunc name : {}".format(myFunc.__name__))
print("myFuncWithMyName name : {}".format(myFuncWithMyName.__name__))
