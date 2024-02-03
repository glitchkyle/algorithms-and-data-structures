import numpy as np
import numpy.typing as npt

def linear_regression(a: npt.NDArray, y: npt.NDArray):
    """
    Creates a linear regression model by calculating the weights 
    given m data points and n dimensions

    :param a: Data + bias values
    :type a: npt.NDArray[mxn]

    :param y: Class labels of shape (mx1)
    :type y: npt.NDArray[mx1]

    :return: Weights of the linear regression model
    :rtype: npt.NDArray[nx1]
    """
    a_trans = a.transpose()
    left = np.dot(a_trans, a)
    right = np.dot(a_trans, y)

    return np.linalg.solve(left, right) 
