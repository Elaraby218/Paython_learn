# set = collection which is unordered , unindexed. no duplicate values
# set in c++ has a different concept : its ordered
# to create list we use [ ] , to create set we use { } so be careful


## methods of set

utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl" , "plate" , "cup"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# it will add all objects of dishes to utensils (update())
# utensils.update(dishes)
# dishes.update(utensils)

dinner_table = utensils.union(dishes)

for i in utensils:
    print(i)
print("--------")
for i in dishes:
    print(i)
print("--------")
for i in dinner_table:
    print(i)

print("--------")
# difference method
print(utensils.difference(dishes))
print("--------")
# difference method
print(dishes.difference(utensils))
print("--------")
# intersection method
print(utensils.intersection(dishes))
print("--------")
# intersection method
print(utensils.intersection(dinner_table))