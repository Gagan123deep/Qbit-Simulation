import numpy as np

#A single qubit gate is a 2x2 unitary matrix. This works on an input state of a single qubit to produce an output state.

#U_gate is the most general single qubit gate. All other single qubit gates can be written in this form.
def U_gate(theta,phi,lamda):

    U=np.zeros((2,2))+0*1j
    # 1j is the python way of writing i, the complex number. Adding 0*1j = 0*i, adds a 0 complex part, making the datatype of the
    # matrix complex. This is often safer to do, to later avoid issues about neglecting imaginary parts, which might happen otherwise.

    U[0,0]=np.cos(theta/2)
    U[0,1]=-np.exp(1j*lamda)*np.sin(theta/2)
    U[1,0]=np.exp(1j*phi)*np.sin(theta/2)
    U[1,1]=np.exp(1j*phi+1j*lamda)*np.cos(theta/2)

    return U



# Hadamard is equivalent to U_gate(np.pi/2,0,np.pi)
def Hadamard():

    H=np.zeros((2,2))+0*1j

    H[0,0]=1
    H[0,1]=1
    H[1,0]=1
    H[1,1]=-1

    H=H/2**0.5

    return H


# X_gate is sigmax Pauli matrix, equivalent to U_gate(np.pi,0,np.pi)
def X_gate():

    X=np.array([[0,1],[1,0]]) + 0*1j

    return X

# Y_gate is sigmay Pauli matrix, equivalent to U_gate(np.pi,np.pi/2,np.pi/2)
def Y_gate():

    Y=np.array([[0,-1j],[1j,0]]) + 0*1j

    return Y

# Z_gate is sigmaz Pauli matrix, equivalent to U_gate(0,np.pi,0)
def Z_gate():

    Z=np.array([[1,0],[0,-1]]) + 0*1j

    return Z

# P_gate is equivalent to U_gate(0,0,lamda)
def P_gate(lamda):

    P=np.array([[1,0],[0,np.exp(1j*lamda)]])

    return P

#S_gate is P_gate(np.pi/2)
#T_gate is P_gate(np.pi/4)
#I_gate is U(0,0,0) or P(0)


    
def SQRT_X_gate():

    m=X_gate()

    eigvals,eigvecs=np.linalg.eigh(m)

    a=np.diag([np.exp(-1j*np.pi/2),1])

    gate= eigvecs @ a @ eigvecs.T.conj()

    return gate


def SQRT_Y_gate():

    m=Y_gate()

    eigvals,eigvecs=np.linalg.eigh(m)

    a=np.diag([np.exp(-1j*np.pi/2),1])

    gate= eigvecs @ a @ eigvecs.T.conj()

    return gate


def T_gate():

    gate=np.zeros((2,2))+0*1j

    gate[0,0]=1
    gate[1,1]=np.exp(-1j*np.pi/4)
    #gate[1, 1] = np.exp(-1j * np.pi / 2)

    return gate


def swap():
    gate=np.zeros((4,4))+0*1j
    gate[0,0]=1
    gate[1,2]=1
    gate[2,1]=1
    gate[3,3]=1

    return gate

def CNOT():
    gate=np.zeros((4,4))+0*1j
    gate[0,0]=1
    gate[1,1]=1
    gate[2,3]=1
    gate[3,2]=1

    return gate