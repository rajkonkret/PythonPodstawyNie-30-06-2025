def connect(**opcje):  # argumenty nazwane, słownikowe **kwargs
    print(opcje)


# argument przekazywany po nazwie
connect(a=100)  # {'a': 100}
connect()  # {}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3, 4, 5, 6, 7)  # (1, 2, 3, 4, 5, 6, 7) {}
all_args(a=10, b=34, c=98, name="Radek")  # () {'a': 10, 'b': 34, 'c': 98, 'name': 'Radek'}
all_args(1, 2, 3, a=10, b=90)  # (1, 2, 3) {'a': 10, 'b': 90}
