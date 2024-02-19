# Dictionary = A changeable , unordered collection of unique Key:value pairs
#              fast because they use hashing, allow us to access a value quickly


capitals = {'USA':'washington DX',
            'India':'New dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

#print(capitals['gfhj']) # Error
print(capitals.get('sadf'))  # return none

# print only the keys useing keys method
print(capitals.keys())

#print only values using capitals method
print(capitals.values())

#print everything using items methods
print(capitals.items())

# add new items into the dicitionary using update method , it can also
# update the value if the key is exist in the dictionary already
capitals.update({'Egypt':'asyut'})
capitals.update({'Egypt':'Cairo'})

# to remove item form dictionary use pop and insert the key
capitals.pop('USA')

#print items in the dictionary using for loop
for key,value in capitals.items():
    print(key, " , " ,value)