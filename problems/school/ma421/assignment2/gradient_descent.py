import numpy as np
import numpy.typing as npt
from typing import Callable

def GD(
        initial_approx: npt.NDArray, 
        continuous_func: Callable[[npt.NDArray], float],
        gradient_func: Callable[[npt.NDArray], npt.NDArray],
        learning_rate: float,
        residual_threshold=10**-6,
        max_iter=100
    ) -> npt.NDArray:
    """
    Write a Python function to implement the gradient descent iteration (GD) to
    minimize f (x). Your function (named GD) should take as inputs an initial approximation
    x0, a learning rate, and the gradient function ∇f (x), and iterate until the residual error
    ‖∇f (xk)‖2 < 10−6 with the maximum iteration set to 100. Print the iterates xk, f (xk),
    and ‖∇f (xk)‖2. Test your GD on the function in Problem 1 by manually computing
    ∇f (x) and passing it to your GD function. Use each of [1, 1]T , [1, −1]T , [2, −2]T as the
    initial approximation and each of α = 1, 10−1, 10−2, 10−3) as the learning rate.
    """
    next_approximation = initial_approx
    
    for _ in range(max_iter):
        error = np.linalg.norm(gradient_func(next_approximation), 2) 
        if error < residual_threshold:
            break
        
        print(f"\nxk: {next_approximation}")
        print(f"f (xk): {continuous_func(next_approximation)}")
        print(f"error: {error}")

        next_approximation -= learning_rate * gradient_func(next_approximation)

    return next_approximation