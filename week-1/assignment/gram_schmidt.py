import numpy as np

def gram_schmidt(A: np.ndarray) -> np.ndarray:
    A=A.T
    U=np.zeros_like(A,dtype=float)
    n=A.shape[0]
    for i in range(n):
        v=A[i]
        if i>0:
            s=np.sum(((np.sum(v*U[:i],axis=1)/np.sum(U[:i]*U[:i],axis=1)).reshape(-1,1))*U[:i],axis=0)
            U[i]=v-s
        else:
            U[i]=v
    norm=np.linalg.norm(U,axis=1)
    Q=(U/norm[:,None]).T
    if np.allclose(Q.T@Q,np.eye(Q.shape[1])):
        return Q
    raise Exception("Q^TQ is not identity")
