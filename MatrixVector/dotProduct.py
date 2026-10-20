import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	numpyA = np.array(a)
	numpyB = np.array(b)

	if numpyA.shape[1] != numpyB.shape[0]:
		return -1
		
	c = np.dot(numpyA, numpyB)
	return c
	pass

def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:
    A = np.array(a)
    B = np.array(b)
              
    if A.shape[1] != B.shape[0]:
        return -1
    c = np.dot(A, B)
    return c
