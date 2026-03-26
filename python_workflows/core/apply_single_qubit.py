#Function for Qbit operation
import numpy as np
def Q_Operate(N, p,psi,U):
    psi_1=np.zeros(2**N,dtype=np.complex128)
    a=2**(N-p)
    for r in range (2**N):
        q=int(int(a & r)/a) #helps in selecting which coefficient of U is to be used for each decimal representation
        q1=int(1^q) #same as above
        r1=int(r^a) #the flip bit of the chosen bit to be operated on
        psi_1[r] = U[q,q]*psi[r] + U[q,q1]*psi[r1]
    return psi_1

