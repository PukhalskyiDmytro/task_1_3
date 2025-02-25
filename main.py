from math import pi

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
    figures = []
    for test_file in TEST_FILES:
        with open(test_file, "r") as f:
            for line in f.readlines():
                try:
                    tmp = line.split()
                    if tmp[0] == "Rectangle":
                        a, b = map(float, tmp[1:])
                        r = Rectangle(a, b)
                        figures.append(r)
                    elif tmp[0] == "Circle":
                        r = float(tmp[1])
                        c = Circle(r)
                        figures.append(c)
                    elif tmp[0] == "Parallelogram":
                        a, b, h = map(float, tmp[1:])
                        p = Parallelogram(a, b, h)
                        figures.append(p)
                    elif tmp[0] == "Triangle":
                        a, b, c = map(float, tmp[1:])
                        t = Triangle(a, b, c)
                        figures.append(t)
                    elif tmp[0] == "Trapeze":
                        a, b, c, d = map(float, tmp[1:])
                        p = Trapeze(a, b, c, d)
                        figures.append(p)
                except Exception as e:
                    continue

    max_area = figures[0].area()
    max_perimeter = figures[0].perimeter()
    for f in figures[1:]:
        area = f.area()
        if area > max_area:
            max_area = area

        perimeter = f.perimeter()
        if perimeter > max_perimeter:
            max_perimeter = perimeter

    print(f"Max area: {max_area}, max perimeter: {max_perimeter}")