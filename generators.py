'''
Generators are special kind of iterators
'''


#  A generator function is a function that contains a yield statement
def gen():
    print('hello')
    yield
    print('how are you?')
    yield


g1 = gen()  # the generator function gets initialized
next(g1)  # the generator object gets called first time and returns whenever a yield statement is reached
next(g1)
# next(g1)  # uncomment to see the exception


#  1 1 2 3 5 8 13 21 ...
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


f = fib()
for _ in range(10):
    print(next(f))

pairs = (x*2 for x in range(10))  # gen comprehension expression
print(pairs)
for pair in pairs:
    print(pair)



