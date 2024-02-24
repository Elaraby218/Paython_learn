#string format = optional method that gives uesr more control when output string s
# its like string interpolation in c++

animal = "cow"
plant = "moon"

print("The {} jumped int the {}".format(animal,plant))

text = "The {} jumped into the {} "
print(text.format(animal,plant))

name = "mohamed"

print("Hello {:10}.Nice to meet you".format(name))
# 10 spaces including the word
# in default the badding is after the word
# to make it before the word use >
print("Hello {:>10}.Nice to meet you".format(name))
# to centerlize the valur use ^
print("Hello {:^10}.Nice to meet you".format(name))






