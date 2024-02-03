import numpy as np
import numpy.typing as npt
from typing import Callable

def Newton(
        initial_approx: npt.NDArray,
        continuous_func: Callable[[npt.NDArray], float],
        gradient_func: Callable[[npt.NDArray], npt.NDArray],
        hessian_func: Callable[[npt.NDArray], npt.NDArray],
        residual_threshold=10**-6,
        max_iter=100
    ) -> npt.NDArray:
    """
    Write a Python function to implement Newton’s iteration to minimize f (x).
    Your function (named Newton) should take as inputs an initial approximation x0, the
    gradient function ∇f (x), and the Hessian function Hf (x), and iterate until the residual
    error ‖∇f (xk)‖2 < 10−6 with the maximum iteration set to 100. Print the iterates xk,
    f (xk), and ‖∇f (xk)‖2. Test your Newton on the function in Problem 1 by manually
    computing ∇f (x) and the Hessian Hf (x), and passing them to your Newton function.
    Use each of [1, 1]T , [1, −1]T , [2, −2]T as the initial approximation.
    """
    next_approximation = initial_approx
    
    for _ in range(max_iter):
        error = np.linalg.norm(gradient_func(next_approximation), 2) 
        if error < residual_threshold:
            break
        
        print(f"\nxk: {next_approximation}")
        print(f"f (xk): {continuous_func(next_approximation)}")
        print(f"error: {error}")

        next_approximation -= np.linalg.solve(hessian_func(next_approximation), gradient_func(next_approximation))

    return next_approximation
