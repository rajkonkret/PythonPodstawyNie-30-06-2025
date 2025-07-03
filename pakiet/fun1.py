def powitanie():
    print("Witaj!!!")


def info():
    print("Jestem pakietem")


print(__name__)  # __main__
# przy imporcie pakiet.fun1
if __name__ == '__main__':
    powitanie()
