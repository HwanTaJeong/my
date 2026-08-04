class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

class Line:

    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.startX = s.x
        self.startY = s.y
        self.endX = e.x
        self.endY = e.y
        self.deltaX = self.startX - self.endX
        self.deltaY = self.startY - self.endY

    def __repr__(self):
        return "Line({} -> {})".format(self.start, self.end)

    def length(self):
        return (self.deltaX ** 2 + self.deltaY ** 2) ** 0.5

class Triangle:
    
    def __init__(self, a, b, c, checkValid = True):
        self.pointA = a
        self.pointB = b
        self.pointC = c
        self.AB = Line(a, b)
        self.BC = Line(b, c)
        self.CA = Line(c, a)

        if checkValid and not self.isValid():
            raise ValueError("Three points are on a line.")

    def __repr__(self):
        return "Triangle({}, {}, {})".format(self.pointA, self.pointB, self.pointC)

    def getCentroid(self):
        return Point((self.pointA.x + self.pointB.x + self.pointC.x)/3, (self.pointA.y + self.pointB.y + self.pointC.y)/3)

    def getPerimeter(self):
        return self.AB.length() + self.BC.length() + self.CA.length()

    def getArea(self):
        ax, ay = self.pointA.x, self.pointA.y
        bx, by = self.pointB.x, self.pointB.y
        cx, cy = self.pointC.x, self.pointC.y
        return abs((ax*(by - cy) + bx*(cy - ay) + cx*(ay - by)) / 2)

    def getCircumcenter(self):
        ax, ay = self.pointA.x, self.pointA.y
        bx, by = self.pointB.x, self.pointB.y
        cx, cy = self.pointC.x, self.pointC.y

        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))

        ux = ((ax**2 + ay**2) * (by - cy) +
              (bx**2 + by**2) * (cy - ay) +
              (cx**2 + cy**2) * (ay - by)) / d
        uy = ((ax**2 + ay**2) * (cx - bx) +
              (bx**2 + by**2) * (ax - cx) +
              (cx**2 + cy**2) * (bx - ax)) / d

        return Point(ux, uy)

    def getOrthocenter(self):
        o = self.getCircumcenter()
        return Point(
            self.pointA.x + self.pointB.x + self.pointC.x - 2 * o.x,
            self.pointA.y + self.pointB.y + self.pointC.y - 2 * o.y
        )

    def isValid(self, eps=1e-9):
        return self.getArea() > eps

def isOnALine(a, b, c):
    return not Triangle(a, b, c, checkValid = False).isValid()

a = Point(0, 0)
b = Point(3, 4)
c = Point(6, 2)

AB = Line(a, b)

abc = Triangle(a, b, c)
DEF = Triangle(a, b, Point(6, 8), checkValid = False)

print(a)
print(AB)
print(abc)
print(abc.getCentroid())
print(abc.getPerimeter())
print(abc.getArea())
print(abc.isValid())
print(DEF.isValid())
print(abc.getCircumcenter())
print(abc.getOrthocenter())
print(isOnALine(abc.getCircumcenter(), abc.getOrthocenter(), abc.getCentroid()))