import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X_trans = np.transpose(X)
	z = np.dot(X_trans, X)
	inv = np.linalg.inv(z)
	v = np.dot(inv, X_trans)
	theta = np.dot(v, y)
	return theta