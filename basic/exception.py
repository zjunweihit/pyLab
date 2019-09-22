
class CustomException(Exception):
    def __init__(self, name):
        Exception.__init__(self)
        self.name = name


addressBook = {
    'Tom': 'Road T No. 126',
    'Jim': 'Road J No. 223',
    'Alex': 'Road A No. 991'
}

#input_name = 'Lucy'
#
#if input_name not in addressBook:
#    raise ValueError("Not find the name: {}".format(input_name))
#    # later code will not be processed

try:
    input_name = input("Enter a name:")
    if input_name not in addressBook:
        raise CustomException(name=input_name)
except EOFError:
    print("EOF error")
except CustomException as ex:
    print("CustomException: name '{}' is not found".format(ex.name))
# no except path
else:
    print("{}: {}".format(input_name, addressBook[input_name]))

# NOTE:
#
# try...finally
#
# if you want a code to run regardless of exception is raised, like when close a file after it's opened.
# use "finally", which cannot be used with "else" together.
#try:
#    f = open("poem.txt")
#except IOError:
#    print("IO Error")
#finally:
#    if f:
#        f.close()
#    print("clean up: closing the file")

# NOTE:
#
# with
#
# 将 with 语句和 open 函数一起使用 —— 我们让 with open 自动完成文件关闭。
#   with 语句隐藏地使用了一个规则。它获取了 open 语句返回的对象，这里我们称之为 "thefile" 。
#   开始它下面的这个代码块前 总是 调用 thefile.__enter__ 函数，在离开这个代码块后 总是 调用 thefile.__exit__
#   被我们写入 finally 语句块的代码会被 __exit__ 方法自动完成
#
#with open("poem.txt") as f:
#    for line in f:
#        print(line, end='')
