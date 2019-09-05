#  File: Geom.py

#  Description: Assignment 3 - Take the input and gives the output using geometric values with classes of Point, Circle
#  and Rectangle.

#  Student Name: Woongchan Lee

#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim

#  Partner UT EID: DK25659

#  Course Name: CS 313E

#  Unique Number: 85575

#  Date Created: 06/15/2019

#  Date Last Modified: 06/17/2019

#  Extra Credit: using internal methods starting from underscore(_) to indicate that method is used by the class

import math


class Point(object):
    # constructor
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # test for the equality of two Point objects
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    def __init__(self, radius=1.0, x=0.0, y=0.0):
        self.radius = float(radius)
        self.center = Point(x, y)

    # compute the circumference of the circle
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute the area of the circle
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if a Point is strictly inside the circle
    def point_inside(self, p):
        return self.center.dist(p) < self.radius

    # determine if a Circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # neither is completely inside the circle
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap(self, c):
        distance = self.center.dist(c.center)
        return distance < (self.radius + c.radius)

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribe(self, r):
        self.center = Point((r.ul.x + Rectangle._length(r) / 2), (r.lr.y + Rectangle._width(r)) / 2)
        self.radius = Point.dist(r.ul, self.center)
        return self

    # string representation of a Circle object
    def __str__(self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.radius - other.radius) < tol) and (abs(self.center.x - other.center.x) < tol) and (
                abs(self.center.y - other.center.y) < tol))


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0.0, ul_y=1.0, lr_x=1.0, lr_y=0.0):
        if (ul_x < lr_x) and (ul_y > lr_y):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def _length(self):
        return float(self.lr.x - self.ul.x)

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def _width(self):
        return float(self.ul.y - self.lr.y)

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return float(2 * (self._length() + self._width()))

    # determine the area of rectangle
    def area(self):
        return self._length() * self._width()

    # determine if a point is strictly inside the rectangle
    def _point_inside(self, p):
        return (self.ul.x < p.x < self.lr.x) and (self.ul.y > p.y > self.lr.y)

    # determine if a rectangle r is strictly inside this rectangle
    def rectangle_inside(self, r):
        return self._point_inside(r.ul) and self._point_inside(r.lr)

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap(self, r):
        # if ul and lr points are in the self, or the range is in the self
        return not self.rectangle_inside(r) and not (self.ul.x > r.lr.x or self.ul.y < r.lr.y or self.lr.x < r.ul.x\
            or self.lr.y > r.ul.y)

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rectangle_circumscribe(self, c):

        self.ul = Point((c.center.x - c.radius), (c.center.y + c.radius))
        self.lr = Point((c.center.x + c.radius), (c.center.y - c.radius))
        return self

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__(self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self._length() - other._length()) < tol) and (abs(self._width() - other._width()) < tol))


def main():
    # open the file geom.txt
    inf = open("geom.txt", "r")
    lines = inf.readlines()
    lst = []
    for line in lines:
        for item in line.split():
            if '.' in item:
                flt = float(item)
                lst.append(flt)
            else:
                pass

    # display outputs

    # create point P and Q
    P = Point(lst[0], lst[1])
    Q = Point(lst[2], lst[3])

    # print the coordinates of the points P and Q
    print("Coordinates of P: " + str(P))
    print("Coordinates of Q: " + str(Q))

    # find the distance between the points P and Q
    print("Distance between P and Q: " + str(Point.dist(P, Q)))

    # create circle C and D
    C = Circle(lst[4], lst[5], lst[6])
    D = Circle(lst[7], lst[8], lst[9])

    # print C and D
    print("Circle C: " + str(C))
    print("Circle D: " + str(D))

    # compute the circumference of C
    print("Circumference of C: " + str(Circle.circumference(C)))

    # compute the area of D
    print("Area of D: " + str(Circle.area(D)))

    # determine if P is strictly inside C
    if Circle.point_inside(C, P):
        print("P is inside C")
    else:
        print("P is not inside C")

    # determine if C is strictly inside D
    if Circle.circle_inside(D, C):
        print("C is inside D")
    else:
        print("C is not inside D")

    # determine if C and D intersect (non zero area of intersection)
    if Circle.circle_overlap(D, C):
        print("C does intersect D")
    else:
        print("C does not intersect D")

    # determine if C and D are equal (have the same radius)
    if C == D:
        print("C is equal to D")
    else:
        print("C is not equal to D")

    # create two rectangle objects G and H
    G = Rectangle(lst[10], lst[11], lst[12], lst[13])
    H = Rectangle(lst[14], lst[15], lst[16], lst[17])

    # print the two rectangles G and H
    print("Rectangle G: " + str(G))
    print("Rectangle H: " + str(H))

    # determine the length of G (distance along x axis)
    print("Length of G: " + str(Rectangle._length(G)))

    # determine the width of H (distance along y axis)
    print("Width of H: " + str(Rectangle._width(H)))

    # determine the perimeter of G
    print("Perimeter of G: " + str(Rectangle.perimeter(G)))

    # determine the area of H
    print("Area of H: " + str(Rectangle.area(H)))

    # determine if point P is strictly inside rectangle G
    if Rectangle._point_inside(G, P):
        print("P is inside G")
    else:
        print("P is not inside G")

    # determine if rectangle G is strictly inside rectangle H
    if Rectangle.rectangle_inside(H, G):
        print("G is inside H")
    else:
        print("G is not inside H")

    # determine if rectangles G and H overlap (non-zero area of overlap)
    if Rectangle.rectangle_overlap(H, G):
        print("G does overlap H")
    else:
        print("G does not overlap H")

    # find the smallest circle that circumscribes rectangle G
    A = Circle()
    print("Circle that circumscribes G: " + str(Circle.circle_circumscribe(A, G)))

    # find the smallest rectangle that circumscribes circle D
    B = Rectangle()
    print("Rectangle that circumscribes D" + str(Rectangle.rectangle_circumscribe(B, D)))

    # determine if the two rectangles have the same length and width
    if H == G:
        print("Rectangle G is equal to H")
    else:
        print("Rectangle G is not equal to H")

    # close the file geom.txt
    inf.close()


if __name__ == "__main__":
    main()
