# Example with ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
from functions_classes import MultiTimer

some_values = [3,4,5,6,7,8,9]

def cube(num):
    print (f" Cube of {num}^3 = {num**3}")
    return num**3

def main():
    results = []
    with ThreadPoolExecutor(max_workers = 5) as exe:
        results.append(exe.submit(cube,2))
            
        # Map the method cube with a list of values 
        results.append(exe.map(cube, some_values))

    print ("Printing cube of 2-9: ")
    for result in results:
        print (result)
if __name__ == "__main__":
    timer =  MultiTimer()
    main()
    timer.time_calculate()
