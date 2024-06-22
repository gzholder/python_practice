animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse', 'dog']
# First way
sorted_animals = sorted(animals)
print('Annimal list unsorted:    {}'.format(animals))
print('Sorted animals list: {}'.format(sorted_animals))

# Second way
animals.sort()
print('Animals after sort method: {}' .format(animals))

# Range
for number in range(2 ,10):
    print(number)
# Every second number
for number in range(2, 10, 2):
    print(number)

for number in range(0, len(animals), 2):
    print(animals[number])