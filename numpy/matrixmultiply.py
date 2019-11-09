import numpy as np

def do_mul(M, K, N, AT, BT):
    m, k, n = M, K, N
    A_Trans = AT
    B_Trans = BT

    if A_Trans == True:
        A = np.reshape(np.arange(m*k), (k, m), order='F').transpose()
    else:
        A = np.reshape(np.arange(m * k), (m, k), order='F')

    if B_Trans == True:
        B = np.reshape(np.arange(k*n, 0, -1), (n, k), order='F').transpose()
    else:
        B = np.reshape(np.arange(k*n, 0, -1), (k, n), order='F')

    C = np.dot(A, B)
    print("A=\n", A)
    print("B=\n", B)
    print("C=\n", C)

do_mul(2, 3, 2, True,False)

