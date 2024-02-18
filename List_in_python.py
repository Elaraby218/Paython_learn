# list = used to store multiple items in a single variable

food = ["Pizza" , "hamburger" , "hotdog" , "spaghetti" , "pudding"]
food[0] = "sushi"

print(food)

food.append("ice cream") # add element to the list at the end
food.remove("hotdog")
food.pop() # remove the last element
food.insert(0,"cake") #insert item at specefic position
food.sort()
food.clear() # remove all elements in the list
for i in food:
    print(i)