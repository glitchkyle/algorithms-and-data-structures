from utils.decorators import Time

@Time
def fibonacci_recursive(num):
    """
    Calculate the n-th Fibonacci number using a recursive approach.

    The Fibonacci sequence is a series of numbers where each number
    is the sum of the two preceding ones, starting from 0 and 1.

    Args:
    n (int): The position of the desired Fibonacci number in the sequence.

    Returns:
    int: The n-th Fibonacci number.
    """
    if num <= 1:
        return num
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)

@Time
def fibonacci_dynamic(num):
    """
    Calculate the n-th Fibonacci number using dynamic programming (bottom-up approach).
    
    The Fibonacci sequence is a series of numbers where each number
    is the sum of the two preceding ones, starting from 0 and 1.
    
    This implementation uses a bottom-up dynamic programming approach
    to efficiently compute Fibonacci numbers without redundant calculations.
    
    Args:
    n (int): The position of the desired Fibonacci number in the sequence.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    # Array for storing fibonacci numbers
    fib = [0, 1]

    if num < 0: raise ValueError("Invalid number for position")
    
    for i in range(2, num + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[num]
