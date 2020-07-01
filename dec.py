def params(odlFunc):
    def inside(*args, **kwargs):
        print(args, kwargs)
        return odlFunc(*args, **kwargs)
    return inside


@params
def mult(x, y):
    print(x * y)


if __name__ == '__main__':
    mult(4, 4)
