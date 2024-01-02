# for loop
name = "David"
for l in name:
    print(l)

# while loop
i = 1
while i < 6:
    print(i)
    i += 1
print("You have reached the end of the list")

# list    
members = ["David", "John", "Ann", "Peter", "Jane"]
for x in members:
    print(x) 

# break
people = ["David", "John", "Ann", "Peter", "Jane"]
for x in people:
    print(x) 
    if x == "Peter":
        break
print("You have reached the end of the list")

# continue
word_list = ["David", "John", "Ann", "Peter", "Jane"]
for name in word_list:
    if name == "Peter":
        continue
    print(name)
print("You have reached the end of the list")

# countdown
number = int(input())
while number >= 0:
    print(number)
    number -= 1