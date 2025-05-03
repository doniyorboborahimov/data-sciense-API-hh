def data_types():
    a = 1               # int
    b = "hello"         # str
    c = 3.14            # float
    d = True            # bool
    e = [1, 2, 3]       # list
    f = {"a": 1}        # dict
    g = (1, 2)          # tuple
    h = {1, 2, 3}       # set

    types = [type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h)]
    type_names = [t.__name__ for t in types]
    print(f"[{', '.join(type_names)}]")


if __name__ == '__main__':
    data_types()
