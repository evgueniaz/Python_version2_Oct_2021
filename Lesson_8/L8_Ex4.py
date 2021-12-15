
def val_checker(func):
    def wrapper(*args):
        arg = float(*args)
        if arg >= 0:
            return func(*args)
        else:
            raise ValueError(f"Wrong argument value {arg}")

    return wrapper


@val_checker
def sqr_root(x):
    return x ** 0.5

a = sqr_root(25)
print(a)