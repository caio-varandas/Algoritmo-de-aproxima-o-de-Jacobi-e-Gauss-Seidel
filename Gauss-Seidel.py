import numpy as np

def gauss_seidel(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)
    
    for k in range(max_iterations):
        x_new = np.copy(x)
        
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new
        
        x = x_new
    
    raise Exception("Gauss-Seidel method did not converge")

# Example usage
A = np.array([[4, 1, 2],
              [3, 5, 1],
              [1, 1, 3]], dtype=np.double)
b = np.array([4, 7, 3], dtype=np.double)

solution = gauss_seidel(A, b)
print("Solution:", solution)