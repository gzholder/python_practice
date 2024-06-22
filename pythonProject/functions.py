# Example 1
def say_hi (first, last):
    # Curly braces is a placeholder for .format method
    print ('Hi {}!'. format(first, last))

say_hi('Sundae', 'Holder')
# # Example
def odd_or_even(number):
    if number %2 == 0:
        return 'Even'
    else:
        return 'Odd'

odd_or_even_string = odd_or_even(8)
print (odd_or_even_string)

def get_name():
    name = input('What is your name? ')
    return name

def say_name(name):
    print ('Your name is {}'.format(name))

def get_and_say_name():
    name = get_name()
    say_name(name)
get_and_say_name()

def new_func(a, b):
    return a * b
thing = new_func(5, 2)
print(thing)