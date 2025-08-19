import time

# === Closure Example ===
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)  # This is a closure
print("Closure example - double(5):", double(5))  # Output: 10

# === Decorator to Measure Execution Time ===
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

# === Custom Decorator to Log Function Calls ===
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

# === Sample Function Using Multiple Decorators ===
@timer_decorator
@logger_decorator
def compute_sum(n):
    """Function to compute sum from 1 to n"""
    time.sleep(1)  # simulate delay
    return sum(range(1, n+1))

# === Context Manager Example ===
def write_to_file(filename, content):
    """Context manager to write to a file safely"""
    with open(filename, 'w') as file:  # file is automatically closed after the block
        file.write(content)

# === Main Execution ===
if __name__ == "__main__":
    result = compute_sum(100000)

    file_content = f"The result is: {result}\n"
    file_content += "This was written using a context manager.\n"

    write_to_file("output.txt", file_content)

    print("Output written to 'output.txt'")
