import numpy as np
from matplotlib import pyplot as plt
import time
import multiprocessing


# timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start)
        return end - start
    return wrapper


@timer
def loop(lst: list) -> None:
    for _ in lst:
        continue
    return


def measure_time(func, params):
    start = time.perf_counter()
    func(params)
    end = time.perf_counter()
    return end - start


def graph_time(func: callable, params: list):
    # create a pool of processes with optimal number of workers
    with multiprocessing.Pool(multiprocessing.cpu_count()):
        results = np.vectorize(measure_time)(func, params)

    print(results)
    plt.scatter(params, results)
    plt.xlabel('Iteration Number')
    plt.ylabel('Runtime (ms)')
    plt.show()


def double_loop(length: int) -> None:
    for i in range(length):
        for _ in range(i, length):
            continue
    return


if __name__ == '__main__':
    params = [[x] for x in np.arange(10**2, 50*(10**2), 10**2)]
    graph_time(double_loop, params)
