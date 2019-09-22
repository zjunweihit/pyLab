# List, tuple, dictionary and set

# list [] 是一种保存有序项集合的数据结构。 项目列表应该使用方括号扩起来.
# start from 0

# tuple ()元组用于将多个对象组合在一起。可以将它们近似看作列表，但是没有列表类提供的许多功能。
# 元组的一个重要特征是，它们和字符串一样是 **不可变的 **，即你不能修改元组。

# dictionary {} 字典就像是一个地址簿，只要知道一个人的名字，你就可以找到他 / 她的地址或联系方式，
# 即，我们将键 （名字）与 值 （详细信息）相关联。
# 注意，
#   1. key is unquie
#   2. key must be const object, like string
#   3. dictionary is out of order

# set([]) 集合（set）是简单对象的 无序的 集合（collection）。
# 当对象在集合中的存在比对象在集合中的顺序或者出现的次数更为重要时，我们就会用到set。
# 可以使用集合（set）来测试成员资格，看看它是否是另一个集合（set）的子集，找到两个集合之间的交集

shoplist = ['apple', 'mango', 'carrot', 'banana']

print("I have {} items to purchase.".format(len(shoplist)))
print("They are:", end=' ')
for i in shoplist:
    print(i, end=' ')

print("\n\nOh, I also need to buy rice.")
shoplist.append('rice')
print("Now my shop list is {}".format(shoplist))

print("\n\nLet's sort the list.")
shoplist.sort()
print("Now my sorted shop list is {}".format(shoplist))

print("\n\n(10 minutes later) I have brought the apple.")
del shoplist[0]
print("Now my sorted shop list is {}".format(shoplist))

print ("====================================================\n\n")

zoo = ('python', 'elephant', 'penguin')
print("number of animals in the zoo is", len(zoo))

# we can re-define the tuple
zoo = ('tiger', 'hippo', 'shark')
# but we cannot change the item of the tuple
#zoo[1] = 'dog'

new_zoo = ('monkey', 'camel', zoo)
print("number of cages in new zoo", len(new_zoo))
print("all animals in new zoo are", new_zoo)
print("all animals from the old zoo is", new_zoo[2])
print("last animal from the old zoo is", new_zoo[2][2])

print ("====================================================\n\n")

addressBook = {
    'Tom': 'Road T No. 126',
    'Jim': 'Road J No. 223',
    'Alex': 'Road A No. 991'
}

print("Alex's address is", addressBook['Alex'])

# add a key-value pair
addressBook['Tony'] = "Road T No. 588"

if 'Tony' in addressBook:
    print("Tony's address is", addressBook['Tony'])

# iterate the dictionary
print("There are {} contacts in address book:".format(len(addressBook)))
for name, address in addressBook.items():
    print("  {} is at {}".format(name, address))

print ("====================================================\n\n")
print("slice of list, tuple")

# index
name = "Alex"

print(shoplist)
print(name)
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# slice
# NOTE:
# **NOT** include the end of range
# same operation as string name

print(shoplist)
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# NOTE:
# 提供第三个参数 步长，默认的步长为 1
print('Item end to start is', shoplist[::-1])
print('Item even index from start to end', shoplist[1::2])

print ("====================================================\n\n")

bri = set(['brazil', 'russia', 'india'])
print("india in bri: {}".format('india' in bri))
print("USA in bri: {}".format('USA' in bri))

bric = bri.copy()
bric.add("China")

print("bri", bri)
print("bric", bric)
print("bric is supuperset of bri : {}".format(bric.issuperset(bri)))

bri.remove('russia')
print("bri", bri)
print("bric", bric)
print("bric & bri : {}".format(bri & bric))

print ("====================================================\n\n")
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
print(shoplist)

# NOTE: **reference**
# mylist 只是指向同一个对象的另一个别名！
mylist = shoplist

# 我买下了第一件商品，所以把它从列表中移除
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到 shoplist 和 mylist 产生了同样的输出
# 输出的都是没有 'apple' 的相同列表
# 这验证了它们都指向着同一个对象

print('Copy by making a full slice')

# NOTE:
# copy list by the entire of slice
# 通过全切片来获得一个副本
mylist = shoplist[:]
# 移除第一个元素
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
