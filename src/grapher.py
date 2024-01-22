from typing import Literal, Callable
from matplotlib import pyplot as plt
import time


# timer decorator
def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start)
        return end - start
    return wrapper


def measure_time(func: Callable, params: list | dict) -> float:
    """
    Runs a given function once with a list of parameters and return the runtime of the function in milliseconds.
    :param func: Callable function to time.
    :param params: List of parameters for the function in order.
    :return: float runtime in milliseconds.
    """
    if not callable(func):
        raise TypeError('The function must be callable')
    if type(params) is dict:
        start = time.perf_counter()
        func(**params)
        end = time.perf_counter()
    else:
        start = time.perf_counter()
        func(*params)
        end = time.perf_counter()
    return (end - start) * 1000


def graph_time(func: Callable, params: list[list | dict] = (), plot_type: Literal['line', 'scatter'] = 'line') -> None:
    """
    Given a function and a list of parameters, graph the runtime of the function.
    :param func: Callable function
    :param params: List of lists or dicts containing the parameters for the function.
    :param plot_type: The plot type for the graph, 'line' = line graph, 'scatter' = scatter graph.
    :return: None
    """
    if not callable(func):
        raise TypeError('The function must be callable')
    results = []
    start = time.time()
    for param in params:
        results.append(measure_time(func, param))
    end = time.time()
    print(f"Timing completed: Total time: {end - start}s")
    match plot_type:
        case 'scatter':
            plt.scatter(params, results)

        case 'line':
            plt.plot(results)

        case _:
            raise ValueError(f'Unknown plot type: {plot_type}')

    plt.xlabel('Iteration Number')
    plt.ylabel('Runtime (ms)')
    plt.title(f"Runtime {plot_type} graph of {func.__name__}")
    plt.show()
