def type_logger(func):
    def tag_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'\tcall {func.__name__} - ({type(args)})')
        return result

    return tag_wrapper


@type_logger
def calc_cube(x):
   return x ** 3


#a = calc_cube(5)
print(type(calc_cube(5)))