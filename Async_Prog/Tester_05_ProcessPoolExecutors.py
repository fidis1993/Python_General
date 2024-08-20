# Example with ProcessPoolExecutor, CPU bound workloads.

from concurrent.futures import ProcessPoolExecutor
from functions_classes import MultiTimer

some_values = [1,2,3,4,5,6,7,8,9]

def cube(num):
    print (f" Cube of {num}^3 = {num**3}")
    return num**3

def main():
    results = []
    with ProcessPoolExecutor(max_workers = 3) as exe:
            
        # Map the method cube with a list of values 
        results.append(exe.map(cube, some_values))

    for result in results:
        print (result)
if __name__ == "__main__":
    timer =  MultiTimer()
    main()
    timer.time_calculate()