import numpy as np

def qubit2_op(n,p,q,state,op):
    final_state=np.zeros(2**n,dtype=np.complex128)
    for v in range(0,2**n):
        r=int((2**(n-p))&v)/(2**(n-p))
        s=int((2**(n-q))&v)/(2**(n-q))
        u=int(2*r+s)
        w=(2**(n-p))+(2**(n-q))
        v3=int(v|w)
        v0=int(w^v3)
        v1=int((2**(n-p))^v3)
        v2=int((2**(n-q))^v3)
        final_state[v]=op[u,0]*state[v0]+op[u,1]*state[v1]+op[u,2]*state[v2]+op[u,3]*state[v3]
    return final_state
