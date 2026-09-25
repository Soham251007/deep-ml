def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np
	trace = matrix[0][0] + matrix[1][1]
	det = np.linalg.det(matrix)
	coeff = [1, -trace, det]
	eigenvalues = np.roots(coeff)

	return eigenvalues