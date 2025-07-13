import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error

df = pd.read_csv("polynomial_regression_data.csv")

x = df["x"]
Y = df["y"]

def poly3(x,a0,a1,a2,a3):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3

params, cov = curve_fit(poly3, x ,Y)

Y_predict = poly3(x, *params)

rmse = np.sqrt(mean_squared_error(Y,Y_predict))

print("Fitted coefficients >> ", params)
print("RMSE >> ", rmse)
