"""
iterables are objects which we can iterate over,
like: lists, tuples, dict
"""
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)

print(l)

"""
an iterator is an object which is used to iterate 
over an iterable
"""
iter1 = iter(l)
print(iter1)
# An iterator can be iterated within a for loop
for item in iter1:
    print(item)
# An iterator can be iterated using next() method and a StopIteration exception must be handled
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
try:
    print(next(iter1))
except StopIteration:
    print('no more elements')
