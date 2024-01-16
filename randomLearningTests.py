# # for loop
# name = "David"
# for l in name:
#     print(l)

# # while loop
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# print("You have reached the end of the list")

# # list    
# members = ["David", "John", "Ann", "Peter", "Jane"]
# for x in members:
#     print(x) 

# # break
# people = ["David", "John", "Ann", "Peter", "Jane"]
# for x in people:
#     print(x) 
#     if x == "Peter":
#         break
# print("You have reached the end of the list")

# # continue
# word_list = ["David", "John", "Ann", "Peter", "Jane"]
# for name in word_list:
#     if name == "Peter":
#         continue
#     print(name)
# print("You have reached the end of the list")

# # countdown
# number = int(input())
# while number >= 0:
#     print(number)
#     number -= 1
    
# def fib(x):
#   if x == 0 or x == 1:
#     return 1
#   else:
#     return fib(x-1) + fib(x-2)
# print(fib(4))

# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))

# def power(x, y):
#   if y == 0:
#     return 1
#   else:
#     return x * power(x, y-1)

# print(power(2, 3))

try:
   num1 = 7
   num2 = 0
   print(num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")