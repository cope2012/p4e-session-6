def verify_grater_than_20(func):
    # print('outer function body')
    def wrapper(*args, **kwargs):
        # print('wrapper function body')
        return func(*args, **kwargs) > 20
    return wrapper


def verify_grater_than(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) > num
        return wrapper
    return decorator


@verify_grater_than(30)
def magic_sum(x, y):
    return x+y


print(magic_sum(10, 21))
