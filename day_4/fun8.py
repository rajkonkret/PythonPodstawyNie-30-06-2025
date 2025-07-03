def all_params(a, b, /, c=42, d=256):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_params(1, 2)  # a=1, b=2
all_params(1, 2, 3, 4)
# a=1, b=2
# c=3, d=4
# / oddziela argumenty posycyjne(postional-only) od pozostałych
# all_params(a=5,b=9,c=8,d=10)
# a, b muszą byc przekazane pozycyjnie
all_params(1, 3, c=9, d=10)

print(50 * "-")


def all_params2(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")
    print(f"{args=}")
    print(f"{kwargs=}")


all_params2(1, 2)
all_params2(1, 2, 3)  # c=3, d=256
all_params2(1, 2, c=45)
all_params2(1, 2, 3, 4)  # c=3, d=4
all_params2(1, 2, 3, 4, 5, 6, 7, )  # c=3, d=4
all_params2(1, 2, 3, 4)  # c=3, d=4
# args=(4, 5, 6, 7)
# kwargs={}
# a=1, b=2
# args=(4,)
# kwargs={}
# d bo jest po args musi byc po nazwie
all_params2(1, 2, 3, 4, 5, 6, 7, d=89)
# a=1, b=2
# c=3, d=89
# args=(4, 5, 6, 7)
# kwargs={}
all_params2(1, 2, 3, 4, 5, 6, 7, d=89, name="Radek")
# kwargs={'name': 'Radek'}
all_params2(1, 2, 3, 4, 5, 6, 7, d=89, name="Radek", a=100)
# kwargs={'name': 'Radek', 'a': 100}
