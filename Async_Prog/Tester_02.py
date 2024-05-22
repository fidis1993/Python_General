#A synchronous queue example

import queue 
from time import time
from time import perf_counter
from time import monotonic
from time import process_time
from time import thread_time

def start_timer():
    #the start of the most famous timers
    s1 = time()
    s2 = perf_counter()
    s3 = monotonic()
    s4 = process_time()
    s5 = thread_time()
    return s1,s2,s3,s4,s5

def end_timer():
    #ending times of timers
    e1 = time()
    e2 = perf_counter()
    e3 = monotonic()
    e4 = process_time()
    e5 = thread_time()
    return e1,e2,e3,e4,e5


def tasks(name, work_que):
    """
    A simple function that hundles tasks, if they exist.
    """

    while not work_que.empty():
        count =  work_que.get()
        Sum = 0
        print(f"Current Task {name} ")
        for x in range(count):
            Sum+=1
            yield
        print(f"Task's {name} total:{Sum}")

def main():

    # Create the supposed queue of work
    work_que = queue.Queue()

    # Add some tasks in the queue
    for work in [14,3,7,20]:
        work_que.put(work)

    # Start the timers
    s1,s2,s3,s4,s5 = start_timer()

    # Let's create some synchronous tasks.
    some_tasks = [ tasks( "One", work_que), tasks("Two", work_que)]
    
    # Run the tasks
    flag = False
    while not flag:
         for f in some_tasks:
            try:
                next(f)
            except StopIteration:
                some_tasks.remove(f)
            if len(some_tasks) == 0:
                flag =  True
    # Close timers and print the execution time
    e1,e2,e3,e4,e5 =  end_timer()

    # calculate the durations
    d1 = e1 - s1
    d2 = e2 - s2
    d3 = e3 - s3
    d4 = e4 - s4
    d5 = e5 - s5
    # report the durations
    print(f'time: {d1}')
    print(f'perf_counter: {d2}')
    print(f'monotonic: {d3}')
    print(f'process_time: {d4}')
    print(f'thread_time: {d5}')

if __name__ == "__main__":
        main()