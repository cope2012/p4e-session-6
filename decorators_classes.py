class RegisterClass:
    def __call__(self, *args, **kwargs):
        self.registry[args[0].__name__] = args[0]

    def __init__(self):
        self.registry = {}


collector = RegisterClass()


@collector
def dummy1():
    print('dummy1 output')


@collector
def dummy2():
    print('dummy2 output')


@collector
def dummy3():
    print('dummy3 output')


input1 = input()
collector.registry[input1]()
