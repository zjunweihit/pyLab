
# '\' will avoie to add an empty line at the first line of the file
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''
fileName = 'poem.txt'
# write a file
f = open(fileName, 'w')
f.write(poem)
f.close()

# read a file
# by default it uses "read" mode
f = open(fileName)
while True:
    # read each line
    line = f.readline()

    # read all lines in a list
    #line = f.readlines()

    # empty line means EOF
    if len(line) == 0:
        break

    # '\n' is appended in each line
    print(line, end='')

f.close()

print("===============================================")

import pickle
shopListFile = "shoplist.data"
shopList = ['apple', 'banana', 'orange']

print("shop list: ", shopList)

print("save the shop list in a picked file")
f = open(shopListFile, 'wb')
# save the object to the file
pickle.dump(shopList, f)
f.close()

print("delete the shop list")
del shopList

f = open(shopListFile, 'rb')
storedList = pickle.load(f)
print("read from pickled file:", storedList)

