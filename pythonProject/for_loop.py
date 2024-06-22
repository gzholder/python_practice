# animals = ['man', 'bear', 'pig', 'cat', 'dog', 'horse']
# for animals in animals:
#     print(animals.upper())
#
# index = 3
# # While loop
# while index < len(animals):
#     print(animals)
#     index += 1
#
# i = 5
# while True:
#     print(i)
#     if i >= 5:
#         break

min_length = 3
name = input("Enter your name: ")
while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Enter your name: ")
    print('Hello, {0}'.format(name))
