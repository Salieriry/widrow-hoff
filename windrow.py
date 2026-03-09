import numpy as np


def novo_peso(W, X, E, Eac, alpha):
    # calcular o novo peso
    for i in range (0,len(W)):
        if Eac < abs(E[i]):
            W[i] = W[i] + alpha * E[i] * (1/np.power(X[i],2)) * X[i]  

def saida_rele(X, S, Y):
    # saída usando relê 
    for i in range(0, len(X)):
        if(S[i] >= 0):
            Y[i] = 1
        else:
            Y[i] = -1
            
def saida_sigmoide(Y, S, lamb):
    # saída usando sigmóide
    for i in range (0, len(S)):
        Y[i] = (1-np.exp(-lamb * S[i])) / (1+np.exp(-lamb * S[i]))             

def windrow_holff(X, bias, W, Eac=0.5, alpha=0.5, lamb=0.5):
    

    S = np.zeros(len(X)) # intermediário

    Y = np.zeros(len(X)) # saída

    E = np.ones(len(X)) # erro final
    D = np.array([0.5, -0.5, -0.5, -0.5]) # saída aceitável / desejável
    
    
    for i in range(0, len(X)):
        # calculo da saída intermediaria
        for e in range(0, len(X[i])):
            S[i] += X[i][e] * W[i][e]
        
        E[i] = D[i] - S[i]
    
    novo_peso(W, X, E, Eac, alpha) 

        
    saida_sigmoide(Y, S, lamb)
                      
    print(f"\033[1;92m {'   X1':<10} {'   X2':<10} {'  Bias':<10} {'    S':<10} {'    Y':<10}")
    print('='*60, '\033[m')

    for i in range (0, len(X)):
        for e in range(0, (len(X[i]))):
            print(f'{X[i][e]:>8.4f}', end=" | ")
        print(f'{S[i]:>8.4f}', end=" | ")
        print(f'{Y[i]:>8.4f}', end=" | ")
        print('')
