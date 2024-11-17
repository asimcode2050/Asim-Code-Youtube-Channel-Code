import time  # Import the time module for measuring execution time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@timer_decorator
def slow_function():
    time.sleep(2)


slow_function()
