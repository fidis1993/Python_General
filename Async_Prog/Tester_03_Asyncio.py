# A test code using the asyncio func

import asyncio
from time import time
from time import perf_counter
from time import monotonic
from time import process_time
from time import thread_time

class MultiTimer:
    #The MultiTimer class will use the time module and calculate all possible times.
    def __init__(self): 
        self.tim = time()
        self.perf_count = perf_counter()
        self.mono = monotonic()
        self.proc_tim = process_time()
        self.thr_tim = thread_time()

    def start_timer(self):
        # Override the start timer of the object.
        self.tim = time()
        self.perf_count = perf_counter()
        self.mono = monotonic()
        self.proc_tim = process_time()
        self.thr_tim = thread_time()

    def time_calculate(self):
        #ending times of timers
        d1 = time() - self.tim
        d2 = perf_counter() - self.perf_count
        d3 = monotonic() - self.mono
        d4 = process_time() - self.proc_tim
        d5 = thread_time() - self.thr_tim

        print(f'time: {d1:.2f}')
        print(f'perf_counter: {d2:.2f}')
        print(f'monotonic: {d3:.2f}')
        print(f'process_time: {d4:.2f}')
        print(f'thread_time: {d5:.2f}')
 
async def sleep(timer):
    # A function that prints current time, sleeps 1sec

    print (f'Time: {timer.time_calculate()}')
    await asyncio.sleep(1)

async def Sum (name, calculations, timer):
    #prints task name and current calculations asynchronous.
    total = 0
    for calc in calculations:
        print (f" Task {name}: executing {total} + {calc} ")
        await sleep(timer)
        total += calc
    print(f" Task {name}: Sum = {total}")

def main():
    timer  = MultiTimer()

    loop =  asyncio.get_event_loop()
    tasks = [
            loop.create_task(Sum("Code 1", [13, 22,44],timer)),
            loop.create_task(Sum("Code 2", [3, 7, 3],timer )),]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()    

if __name__ == "__main__" :
    main()