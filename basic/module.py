# NOTE:
# 导入模块是一个相对而言开销较大的操作，因此，Python 试用了一些手段来使得导入模块的操作更加快速。
# 其中一个方法，就是创建以 .pyc 为扩展名的 字节码 文件，它是一种中间形式，
# Python 会把程序代码转换成这样的形式。当你下一次想要在另外一个程序代码中导入模块的时候，
# 这个 .pyc 文件就导入操作会很快完成，这是因为导入模块所必须的一部分操作已经被事先完成了。
# 此外，这些字节码文件都是平台无关的。
#
# 注意：这些 .pyc 文件一般会被创建在与它对应的 .py 文件相同的文件目录下。
# 如果 Python 没有在该文件夹下写文件的权限，那么 .pyc 文件将不会被创建。
import sys

# NOTE:
# from...import we can use argv in later code directly.
# but suggest to use import, so that we can see the function from which module clearly
#
#from sys import argv

print("the command arguments:")

# NOTE:
# sys.argv[0] the python program's name
# sys.argv[1] the input argument
for i in sys.argv:
    print("  - {}".format(i))

# NOTE:
# 如果module不是一个编译模块（即用 Python 编写的模块），那么 Python 解释器会在它的 sys.path 变量中列出来的目录中寻找它
print("\n PYTHONPATH is{}".format(sys.path))

# NOTE:
# 每一个模块都有一个名称，在模块中我们可以通过判断语句来确定模块的名称。
# **当模块第一次被导入的时候，模块的代码将被执行。**
if __name__ == "__main__":
    print("This program is being executed by itself")
else:
    print("I'm being imported from another module")

# no arguments when it's imported
#
# >>> import module
# the command arguments:
#   -
#
#  PYTHONPATH is['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/home/zjunwei/.local/lib/python3.6/site-packages', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']
# I'm being imported from another module
# >>>

# NOTE:
# MyModule ONLY can be found in
# 1. the same path as the current program
# 2. sys.path
from MyModule import SayHi, __version__

SayHi()
print("MyModule Version: ",  __version__)

# NOTE:
# dir() lists properties of a module or current module if no input

print(dir(sys))
# current modules
print(dir())

# NOTE:
# 程序包就是一个装满模块的文件夹，它有一个特殊的 __init__.py 文件，
# 这个文件告诉 Python 这个文件夹是特别的，因为它装着 Python 的模块。
#
# 让我们假设你想创建一个叫做 world 的程序包，它有很多子程序包 asia、africa 等。
# 这些子程序包依次包含 india、madagascar 等模块。
#
# - <some folder present in the sys.path>/
#     - world/
#         - __init__.py
#         - asia/
#             - __init__.py
#             - india/
#                 - __init__.py
#                 - foo.py
#         - africa/
#             - __init__.py
#             - madagascar/
#                 - __init__.py
#                 - bar.py
