import re

# line = "'Bart', 'Lisa & Maggie'"
# line = re.sub('[\']', '', line)
# print(line)
# list1 = [0,1,2,6,3,4,5]


# def increment_string(strng):
#     digit = -999
#     digit_str = "-999"
#     last_digit = -999
#     count = 0
#     if strng == "":
#         return str(1)
#     elif strng[-1].isalpha():
#         return strng + str(1)
#     else:
#         for i in range(len(strng) - 1, -1, -1):
#             if strng[i].isdigit():
#                 print("Yes")
#                 count += 1
#                 print(count)
#                 if len(strng) == count:
#                     digit_str = strng
#                     digit = int(digit_str)
#                 continue
#             else:
#                 last_digit = i
#                 digit_str = strng[last_digit + 1:]
#                 digit = int(digit_str)
#                 break
#
#         digit += 1
#         if len(str(digit)) != digit_str:
#             dif = len(digit_str) - len(str(digit))
#             strng = strng[:last_digit + 1] + str(0) * dif + str(digit)
#         else:
#             strng = strng[:last_digit + 1] + str(digit)
#         return strng
#
#
# print(increment_string("00799"))
#

# import requests
# # from random import choice
# # import pyfiglet
# # from termcolor import colored
# #
# #
# # header = pyfiglet.figlet_format("DAD JOKES 3000")
# # header = colored(header, color="green")
# # print(header)
# # request = input("Let me tell you a joke! Give me a topic: ")
# # url = "https://icanhazdadjoke.com/search"
# # req = requests.get(url, headers={"Accept": "application/json"},
# #                    params={"term": request})
# # data = req.json()
# # no_of_jokes = data['total_jokes']
# print(no_of_jokes)
# print("No. of jokes" + str(no_of_jokes))

# print(data)
# print(data.keys())
# if no_of_jokes > 20:
#     random_num = 20
#
# if no_of_jokes == 0:
#     print(f"Sorry, I don't have jokes about {request}! Please try again.")
# elif no_of_jokes == 1:
#     print(f"I've got one joke about {request}. Here it is: ")
#     print(data['results'][0])
#
# else:
#     print(f"I have got {no_of_jokes} jokes about {request}! Here is one:")
#     print(choice(data['results'])['joke'])
#
#
# def permutations(string):
#   rest = permutations(string[1:])
#   print(rest)
#
# permutations("he")

# def same_structure_as(original, other):
#     for i in original:
#         for j in other:
#             if type(i) != type(j):
#                 return False
#     return True

# a = 4 ** 3
# b = pow(4, 3)
# print(type(a), type(b))
