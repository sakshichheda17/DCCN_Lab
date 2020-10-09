"""
Exp5 Task1
Group 2
ISHITA BADOLE: 2018130001
SAKSHI CHHEDA: 2018130005
AISHWARYA GHAIWAT: 2018130012

"""

import numpy as np


def mod2(A):
    return np.mod(A,2)
    

def equal(a, b):
    return np.array_equal(a,b)


def syndrome_decode(codeword, n, k, G):
    #G = I(kxk)|A
    #calculate A
    A = G[0:k,k:n]
    print("The generated A matrix :")
    print(A)
    
    #calculate H
    At = A.transpose()
    I = np.identity(n-k,dtype=int)
    H = np.concatenate((At,I), axis=1)
    print("\nThe generated H matrix :")
    print(H)

    #calculate cdash
    rT = r.transpose()
    x = H.dot(rT)
    cdash = mod2(x)
    print("\nThe generated cdash :")
    print(cdash)

    for i in range(k):
        #generate syndromes of interest
        T = np.array([0,0,0,0,0,0,0])
        T[i] = 1
        syndrome = H.dot(T.transpose())
        
        #check if syndrome is equal to cdash
        if equal(syndrome,cdash):
            print("\nError detected: Flipped bit at position",i+1)
            r[i] = not(r[i])
            break
    return(r[:k])

if __name__ == "__main__":
    n=7 #Length of codeword
    k=4 #Length of message
    # G is the k × n generator matrix
    G = np.array([1,0,0,0,1,1,0,
                0,1,0,0,1,0,1,
                0,0,1,0,0,1,1,
                0,0,0,1,1,1,1
                ]).reshape(k,n)

    c = np.array([1,0,1,0,1,0,1])   #correct codeword

    #Test case1      
    r = np.array([1,1,1,0,1,0,1])   #received code with error at position 2
    codeword =  r       
    message = syndrome_decode(codeword, n, k, G)  
    print("\nThe corrected message :",message)

    #Test case2
    # r = np.array([1,0,1,0,0,0,1])   
    # codeword =  r       
    # message = syndrome_decode(codeword, n, k, G)  
    # print("\nThe corrected message :",message)

    





