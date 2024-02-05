import numpy as np
from ..utils.math_utils import get_u, function_activation_step, calculate_error, calculate_delta_w, calculate_norm, \
    update_w


def execute_perceptron(data):
    matrix = np.insert(np.array(data["matrix"]), 0, 1, axis=1)
    yd = np.array(matrix[:, -1]).astype(int).reshape(-1, 1)
    w = initializer_w(matrix)
    w_eras = [w]
    errors = []
    # iterations = 0
    for era in range(data["eras"]):
        u = get_u(w, matrix)
        yc = function_activation_step(u)
        e = calculate_error(yd, yc)
        delta_w = calculate_delta_w(data["eta"], e, matrix)
        norm = calculate_norm(e)
        errors.append(norm)
        w = update_w(w, delta_w)
        w_eras.append(w)
        # iterations = era
        # if norm <= data["tolerance"]:
        #     break
    info = {
        "eras": data["eras"],
        # "eras_error": iterations,
        "tolerance": data["tolerance"],
        "eta": data["eta"],
        "w_initial": w_eras[0],
        "w_final": w_eras[-1]
    }

    return errors, w_eras, info


def initializer_w(matrix):
    return np.random.random((1, matrix.shape[1] - 1))
