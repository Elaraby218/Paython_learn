# break    : used to terminate the loop entirely
# continue : skips to the next iteration of the loop
# pass     : does nothing, acts as a placeholder

print("Test Break")
while True:
    name = input("Please insert your name")
    if name!="":
        break

print("")

print("Test continue")
Phone_number = "123-3434-353"
for i in Phone_number:
    if i=='-':
        continue
    else:
        print(i , end="")

print("")
print("")
print("Test Pass")
for i in range(20):
    if i%2==0:
        pass
    else:
        print(i)


# https://youtu.be/XKHEtdqhLK8?t=4861