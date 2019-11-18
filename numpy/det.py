import numpy as np

a=np.array([
    [1, 2],
    [3, 4]
])

b=np.array([
    [0, 4, 1],
    [0, 2, 3],
    [1, 2, 3],
])

print(np.linalg.det(b))
