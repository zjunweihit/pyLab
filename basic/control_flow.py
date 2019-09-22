
num = 23

#guess = int(input('Enter an integer: '))
guess = 8

if guess == num:
    print("You got it!")
elif guess < num:
    print("No, it's less than that")
else:
    print("No, it's more than that")

print("Done")

# ------------------------------------------------------------
cnt = 0

while cnt < 3:
    print ("count : {}".format(cnt))
    cnt += 1

print("Done")

# ------------------------------------------------------------

print("count in range (1, 5):")
for i in range(1, 5):
    print(i)
print("Done")
