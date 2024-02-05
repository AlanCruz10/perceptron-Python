import numpy as np


def get_u(w, matrix):
    x = matrix[:, :(matrix.shape[1] - 1)]
    return np.dot(x, w.T)


def function_activation_step(u):
    return np.where(u >= 0, 1, 0).astype(int)


def calculate_error(yd, yc):
    # return yc - yd
    return yd - yc


def calculate_norm(e):
    return np.linalg.norm(e)


def calculate_delta_w(eta, e, matrix):
    x = matrix[:, :(matrix.shape[1] - 1)]
    # return (-eta) * np.dot(e.T, x)
    return eta * np.dot(e.T, x)


def update_w(w, delta_w):
    return w + delta_w
