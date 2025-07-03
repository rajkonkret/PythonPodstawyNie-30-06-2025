# funkcja wewnętrzna, zagnieżdżona
# funkcja zagnieżdzona uzywana jest w dekoratorach

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy adres funkcji


fun1()
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x10261b600>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2, uruchomienie funkcji zawartej w zmiennej xFun

# To jest fun1
# <function fun1.<locals>.fun2 at 0x10063b600>
# <class 'function'>
# To jest fun2
