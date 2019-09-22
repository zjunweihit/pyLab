str = "this is a book"

print(str)

if str.startswith("this"):
    print("the string start with 'this'")

if 'a' in str:
    print("the string contains the 'a'")

if str.find("book"):
    print("the string includes 'book'")

delimiter = "_#_"
mylist = ['Chian', 'Japan', 'Russia']
print(delimiter.join(mylist))