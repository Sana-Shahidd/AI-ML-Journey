import multiprocessing
import math
import sys
import time


sys.set_int_max_str_digits(1000000)

import multiprocessing
import time

def factorial(num):
    if num < 0:
        return None
    
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

if __name__ == "__main__":
    numbers = [1000, 2000, 3000]

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        result = pool.map(factorial, numbers)

    end_time = time.time()

    print("Computed successfully")
    print(f"Time Taken: {end_time - start_time}")