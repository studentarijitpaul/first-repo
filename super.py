class Employee:
    def __init__(self) -> None:
        print("constructorof employee")
    a = 1

class progremmer (Employee):
    def __init__ (self):
        super().__init__()
        print( "constructor of progremmer")
    b = 2

class manager( progremmer ):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c = 3

o = manager()
print(o.a,o.b,o.c)