from sklearn.linear_model import LinearRegression
import numpy as np


def lin_reg(x, y):
    x = np.array(x).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1)
    model = LinearRegression().fit(x, y)
    return model.coef_[0][0], model.intercept_[0]