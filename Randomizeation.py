#Random numbers

import random
x = random.randint(1,6)
y = random.random()
print(y)
print(x)

list = ["r","p","s"]
y = random.choice(list);
print(y)

list = ['a',3,4,5,6,7,65,5,'b',4,65]
random.shuffle(list)
print(list)