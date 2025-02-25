from math import pi

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.c + self.b

    def area(self):
        p = (self.a + self.c + self.b)/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return self.a * self.h

    def perimeter(self):
        return 2 * (self.a + self.b)

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2 * pi * self.r

if __name__ == "__main__":
    P = Parallelogram(2, 5 , 3)
    print(f"Area: {P.area()} Perimeter: {P.perimeter()}")

    C = Circle(5)
    print(f"Area: {C.area()} Perimeter: {C.perimeter()}")

    TEST_FILES = ["input01.txt", "input02.txt", "input03.txt"]
    figures_area = []
    figures_perimeter = []
    for test_file in TEST_FILES:
        with open(test_file, "r") as f:
            for line in f.readlines():
                try:
                    tmp = line.split()
                    if tmp[0] == "Rectangle":
                        pass
                    elif tmp[0] == "Circle":
                        pass
                    elif tmp[0] == "Parallelogram":
                        pass
                    elif tmp[0] == "Triangle":
                        pass
                    elif tmp[0] == "Trapeze":
                        pass
                except Exception as e:
                    continue

    for f in figures_area:


    if solutions1:
        x1 = min(solutions1)
        x2 = max(solutions1)
        print(f"Min one root: {x1}")
        print(f"Max one root: {x2}")
