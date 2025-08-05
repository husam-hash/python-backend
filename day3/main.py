

import math
import statistics
import random
import os
import sys
import requests  

from utils import math_utils

print("Custom Utilities:")
print("Square of 4:", math_utils.square(4))
print("Cube of 3:", math_utils.cube(3))
print("Factorial of 5:", math_utils.factorial(5))


data = [random.randint(1, 100) for _ in range(10)]
print("\nRandom Data:", data)

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Standard Deviation:", statistics.stdev(data))
print("Square root of max:", math.sqrt(max(data)))


print("\nCurrent Directory:", os.getcwd())
print("Python Version:", sys.version)

try:
    response = requests.get("https://api.github.com")
    print("\nGitHub API status:", response.status_code)
except Exception as e:
    print("Error fetching GitHub API:", e)
