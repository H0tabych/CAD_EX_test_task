"""
Assignment 1. 3D curves evaluation application.
Design a small program in C++, C#, Java or other object-oriented language that would implement support of
3D curves' hierarchy.
1. Support two types of 2D geometric curves – lines and ellipses. (See details below). Each curve
should be able to return a 2D point and a first derivative (2D vector) per parameter t along the curve.
2. Populate a container (e.g. vector or list) of objects of these types created with random or fixed
parameters.
3. Print coordinates of points and derivatives of all curves in the container at t=PI/4.
Requirements to the implementation:
1. The implementation must use virtual methods.
Curve definitions:
- All curves are parametrically defined, i.e. a point is calculated using some C(t) formula.
- Line is defined by its origin point O and direction D: C(t) = O + D*t.
- Ellipse is defined by its two radii, along X and Y axes.
"""


from abc import ABC, abstractmethod
from typing import Tuple
from math import pi, sin, cos
from random import uniform


class Curve(ABC):
    def __init__(self):
        """
        Base abstract class for geometric curves
        """
        pass

    @abstractmethod
    def calc(self, t: float) -> tuple:
        """
        Basic abstract method for determining the coordinates of a point by a function parameter
        :param t: parameter along the curve. type: float
        :return: tuple with point coordinates. type: tuple
        """
        pass

    @abstractmethod
    def fst_derivative(self, t: float) -> tuple:
        """
        Basic abstract method for finding the vector of the derivative of a function with respect to a given parameter
        :param t: parameter along the curve. type: float
        :return: vector of the derivative of a function at a given point. type: tuple
        """
        pass


class Line(Curve):
    def __init__(self, d: Tuple[float, float, float], o: Tuple[float, float, float]):
        """
        class of geometric curves - line
        :param d: coordinates of some point on the line. type: tuple
        :param o: direction vector of a straight line. type: float
        """
        super().__init__()
        self.d = d
        self.o = o

    def calc(self, t: float) -> tuple:
        """
        Method for determining the coordinates of a point on a line by a function parameter
        :param t: parameter of the parametric equation of the straight line. type: float
        :return: tuple with point coordinates. type: tuple
        """
        point = tuple(self.d[j] * t + self.o[j] for j in range(len(self.d)))
        return point

    def fst_derivative(self, t: float) -> tuple:
        """
        Method for finding the vector of the derivative of a function with respect to a given parameter
        :param t: parameter of the parametric equation of the straight line. type: float
        :return: vector of the derivative of a function at a given point. type: tuple
        """
        d_point = self.d
        return d_point


class Ellipse(Curve):
    def __init__(self, rx: float, ry: float):
        """
        class of geometric curves - ellipse
        :param rx: radius along the x-axis
        :param ry: radius along the y-axis
        """
        super().__init__()
        self.rx = rx
        self.ry = ry

    def calc(self, t: float) -> tuple:
        """
        Method for determining the coordinates of a point on an ellipse by a function parameter
        :param t: angle of inclination to the abscissa axis. type: float
        :return: tuple with point coordinates. type: tuple
        """
        x = self.rx * sin(t)
        y = self.ry * cos(t)
        z = 0

        return x, y, z

    def fst_derivative(self, t: float) -> tuple:
        """
        Method for finding the vector of the derivative of a function with respect to a given parameter
        :param t: angle of inclination to the abscissa axis. type: float
        :return: vector of the derivative of a function at a given point. type: tuple
        """
        x = -1 * self.rx * cos(t)
        y = self.ry * sin(t)
        z = 0

        return x, y, z


def output(param: float, list_object: list):
    curve_name = type(list_object[0]).__name__
    print(curve_name, ':')

    for k in range(len(list_object)):
        match curve_name:
            case 'Line':
                print(f'origin point: x = {list_object[k].o[0]: .2f}, '
                      f'y = {list_object[k].o[1]: .2f}, '
                      f'z = {list_object[k].o[2]: .2f}')
                print(f'direction vector: x = {list_object[k].d[0]: .2f}, '
                      f'y = {list_object[k].d[1]: .2f}, '
                      f'z = {list_object[k].d[2]: .2f}')
            case 'Ellipse':
                print(f'radius along the x-axis: {list_object[k].rx: .2f}')
                print(f'radius along the y-axis: {list_object[k].ry: .2f}')
        print(f'coordinates at pi/4: x = {list_object[k].calc(param)[0]: .2f}, '
              f'y = {list_object[k].calc(param)[1]: .2f}, '
              f'z = {list_object[k].calc(param)[2]: .2f}')
        print(f'first derivative at pi/4: x = {list_object[k].fst_derivative(param)[0]: .2f}, '
              f'y = {list_object[k].fst_derivative(param)[1]: .2f}, '
              f'z = {list_object[k].fst_derivative(param)[2]: .2f}', '\n')


if __name__ == '__main__':
    dim_space = 3
    amount = 10
    lines = [Line(tuple(uniform(1, 10) for _ in range(dim_space)),
                  tuple(uniform(1, 10) for _ in range(dim_space))) for _ in range(amount)]
    output(pi/4, lines)

    ellipse = [Ellipse(uniform(1, 10), uniform(1, 10)) for _ in range(10)]
    output(pi/4, ellipse)
