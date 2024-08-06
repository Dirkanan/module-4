from math import inf


def divide(first=10, second=0):
    if second != 0:
        return first / second
    elif second == 0:
        return inf
