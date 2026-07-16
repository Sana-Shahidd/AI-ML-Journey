import multiprocessing
import time

def square_numbers():
    for i in range(10):
        time.sleep(1.5)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(10):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")


    # Process pool executor
from concurrent.futures import ProcessPoolExecutor
import time

def print_numbers(numbers):
    time.sleep(1)
    return f'Numbers: {numbers}'

numbers=[1,2,3,4,2,3,4,5,6,7,8,9,0]

if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(print_numbers, numbers)

    for result in results:
        print(result)