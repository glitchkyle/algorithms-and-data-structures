from time import time

def Time(func):
    recursion_depth = 0

    def wrapper(*args, **kwargs):
        nonlocal recursion_depth

        if recursion_depth == 0: print(f"Function {func.__name__} started.")

        recursion_depth += 1

        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_time = end_time - start_time

        recursion_depth -= 1

        if recursion_depth == 0: print(f"Function {func.__name__} took {elapsed_time:.6f} seconds to execute.")

        return result
    return wrapper