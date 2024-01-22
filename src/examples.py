from src.grapher import *


def loop(length: int) -> None:
    for _ in range(length):
        continue
    return


def double_loop(length: int) -> None:
    for _ in range(length):
        for _ in range(length):
            continue
    return


def log_loop(n: int) -> None:
    i = n
    while i != 0:
        i = i // 2


def multi_input(length: int, name: str) -> None:
    for _ in range(length * len(name)):
        continue
    return


def str_loop(s: str) -> None:
    for _ in range(len(s)):
        continue


if __name__ == '__main__':
    # O(n) time complexity. Using list of parameters
    params = [[x] for x in range(10 ** 2, 100 * (10 ** 2), 10 ** 2)]
    graph_time(loop, params)

    # O(n^2) time complexity. Using dictionary of parameters.
    params = [{'length': x ** 2} for x in range(10, 100, 10)]
    graph_time(double_loop, params)

    # O(log(n)) time complexity
    params = [{'n': x} for x in range(10 ** 4, 100 * (10 ** 4), 10 ** 4)]
    graph_time(log_loop, params)

    # O(nk) time complexity n = length, k = len(name)
    params = [{'length': x, 'name': 'Hello'} for x in range(10 ** 2, 100 * (10 ** 2), 10 ** 2)]
    graph_time(multi_input, params)
