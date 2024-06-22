animals =['man', 'bear', 'pig']
print(animals[0])
# change first index to cat
animals[0] = 'cat'
print(animals[0])
# negative works from last index all the way down
print(animals[-1])

#use append to ADD to index
animals.append('dog')
# Use extend to ADD multiple indexes to list
animals.extend(['shark', 'whale'])
print(animals)

more_animals = ['horse', 'monkey']
animals.extend(more_animals)
print(animals)

# Print starting from second index up to the fourth but not including the 4th
some_animals = animals[:2]
print('Some animals:      {}'.format(some_animals))

# Combine lists use + sign
more_animals = ['fish]', 'jellyfish', 'octopus']
all_animals = animals + more_animals
print('Combined list ', all_animals)

print('The length of all_animals is ', len(all_animals), 'and the length for more_animals is', len(animals))

# Tuples:
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday')
weekend = list(days_of_week)
for day in weekend:
    print(day)