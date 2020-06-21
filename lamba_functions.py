#  map, filter, reduce
from functools import reduce


people = [
    {
        'name': 'Jhon',
        'age': 20,
        'height': 1.74
    },
    {
        'name': 'Jane',
        'age': 25,
        'height': 1.69
    },
    {
        'name': 'Carol',
        'age': 15,
        'height': 1.66
    }
]

older_ones = list(filter(lambda x: x['age'] >= 20, people))
# print(older_ones)


def add_to_age(x):
    x['age'] += 5
    return x


altered_age = list(map(add_to_age, people))  # map operates in the same iterable, it does not create a new one
print(altered_age)

#  list comprehension
l = [person['age'] for person in people]
print(l)


sum_of_ages = reduce(lambda x, y: x + y, [person['age'] for person in people])
print(sum_of_ages)

