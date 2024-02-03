import numpy as np
import numpy.typing as npt

from problems.school.ma421.assignment2.newton import Newton
from problems.school.ma421.assignment2.gradient_descent import GD
from problems.school.ma421.linear_regression import linear_regression

def problem3():
    init = np.array([[1], [-1]])

    def my_continuous_func(input: npt.NDArray) -> float:
        x1 = input[0][0]
        x2 = input[1][0]
        return float((2 * x1**2) + x2**2 - (2*x1*x2) + (2*x1**3) + (x1**4))
    
    def my_gradient_func(input: npt.NDArray) -> npt.NDArray: 
        x1 = input[0][0]
        x2 = input[1][0]
        return np.array([[(4 * x1) - (2 * x2) + (6 * x1**2) + (4 * x1**3)], [(2 * x2) - (2 * x1)]])

    def my_hessian_func(input: npt.NDArray) -> npt.NDArray:
        x1 = input[0][0]
        x2 = input[1][0]
        return np.array([[4 + (12 * x1) + (12 * x1**2), -2], [-2, 2]])

    result = Newton(init, my_continuous_func, my_gradient_func, my_hessian_func)
    print(f"\nResult: {result}")

def problem4():
    init = np.array([[1], [-1]])

    def my_continuous_func(input: npt.NDArray) -> float:
        x1 = input[0][0]
        x2 = input[1][0]
        return float((2 * x1**2) + x2**2 - (2*x1*x2) + (2*x1**3) + (x1**4))
    
    def my_gradient_func(input: npt.NDArray) -> npt.NDArray: 
        x1 = input[0][0]
        x2 = input[1][0]
        return np.array([[(4 * x1) - (2 * x2) + (6 * x1**2) + (4 * x1**3)], [(2 * x2) - (2 * x1)]])

    result = GD(init, my_continuous_func, my_gradient_func, 0.1)
    print(f"\nResult: {result}")

if __name__ == '__main__':
    a = np.array([[1, 274, 2450], [1, 180, 3254], [1, 375, 3802], [1, 205, 2838], [1, 86, 2347]])
    y = np.array([[162], [120], [223], [131], [67]])

    weights = linear_regression(a, y)

    x = np.array([[1, 220, 2500]])
    print(np.dot(x, weights))
    print(weights)