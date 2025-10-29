import numpy as np


def calculate(list):

    if len(list) > 9 or len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    input = [[] for _ in range(3)]
    for i in range(9):
        input[i // 3].append(list[i])

    matrix = np.array(input, dtype=np.int32)

    np_cbs = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum,
    }

    calculations = {}
    for key, val in np_cbs.items():
        calculations[key] = calculate_stats(matrix, val)

    return calculations


def calculate_stats(matrix, np_cb):
    axis1 = np_cb(matrix, axis=0)
    axis2 = np_cb(matrix, axis=1)
    flattened = np_cb(matrix)
    return [axis1.tolist(), axis2.tolist(), flattened]

