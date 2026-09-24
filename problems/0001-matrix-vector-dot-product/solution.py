def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	
	ans = []

	for row in a:
		total = 0
		for j in range(len(b)):
			total += row[j] * b[j]
		ans.append(total)
	
	return ans
