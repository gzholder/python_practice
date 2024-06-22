# import sys
#
# cur = ''
# cnt = 0
#
# for x in input():
#     if x != cur:
#         if cnt > 0:
#             sys.stdout.write('({}, {}) '.format(cnt, cur))
#         cur = x
#         cnt = 1
#     else:
#         cnt += 1
#
# if cnt > 0:
#     sys.stdout.write('({}, {}) '.format(cnt, cur))

# print("100200".split("00"))

import operator

def person_lister(f):
    def inner(people):
        age = people[3]
        print(age)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# Sort by N character in list
import operator

def person_lister(f):
    def inner(people):
        sorted_people = sorted(people, key=lambda x: int(x[2]))
        return [f(person) for person in sorted_people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')