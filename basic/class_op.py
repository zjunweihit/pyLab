#
# NOTE:
# self is always set as the first parameter for a func in a class
# 假设你有一个类叫做 MyClass 以及这个类的一个对象叫做 myobject 。
# 当你需要这样调用这个对象的方法的时候：myobject.method(arg1, arg2) ，
# 这个语句会被 Python 自动的转换成 MyClass.method(myobject, arg1, arg2)

class Person:
    # calculate the number of Person
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.counter += 1

    def SayHi(self):
        print("Hello, my name is {}".format(self.name))

    def Remove(self):
        print("{}: I'm going to leave".format(self.name))
        Person.counter -= 1

    def Tell(self):
        print("Name: {}, Age: {}".format(self.name, self.age), end=" ")

    # method of the class, not for an object.
    # have to define the counter in class.
    # it's a decorator
    # e.g. HowMany = classmethod(HowMany)
    @classmethod
    def HowMany(cls):
        print("Now we have {} person{}".format(cls.counter, 's' if cls.counter > 1 else ''))


class Teacher(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary
    def tell(self):
        Person.Tell(self)
        print("Salary: {}".format(self.salary))


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score
    def tell(self):
        Person.Tell(self)
        print("Score: {}".format(self.score))


p1 = Person("Lee", 16)
p1.SayHi()

p2 = Person("John", 18)
p2.SayHi()

p2.Remove()

Person.HowMany()

print("==========================================")

t1 = Teacher("Tom", 33, 5000)
t2 = Teacher("Lucy", 43, 15000)

s1 = Student("Jim", 16, 90)
s2 = Student("Alex", 15, 80)

members = [t1, t2, s1, s2]

for i in members:
    i.tell()

