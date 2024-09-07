class Triangle:
    def __init__(self, level):
        self.__level = level

    def show(self):
        for i in range(self.__level):
            for j in range(i + 1):
                print('*', end='')
            print()

class RTriangle:
    def __init__(self, level):
        self.__level = level

    def show(self):
        for i in range(0, -self.__level, -1):
            for j in range(self.__level + i):
                print('*', end='')
            print()


class Rectangle:
    def __init__(self, level):
        self.__level = level
    
    def show(self):
        for i in range(self.__level):
            for j in range(self.__level):
                print('*', end='')
            print()


class Line:
    def __init__(self, level):
        self.__level = level

    def show(self):
        for i in range(self.__level):
            print('**')

# r = Triangle(5)
# r.show()
# r2 = Rectangle(5)
# r2.show()
# r1 = RTriangle(5)
# r1.show()
# line = Line(3)
# line.show()

graph = []
graph.append(Triangle(5))
graph.append(Rectangle(5))
graph.append(RTriangle(5))
graph.append(Line(3))
             
for i in graph:
    i.show()