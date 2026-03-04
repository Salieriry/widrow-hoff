import numpy as np
import os

os.system( 'cls' if os.name == 'nt' else 'clear')

print('\033[1;33m='*60)
print('{: ^60}'.format('Windrow Holff'))
print('='*60)
print('\033[m')

X = np.array([[1,1], [1,-1], [-1,-1], [-1,1]])
bias = np.ones((len(X),1))

X = np.hstack((X, bias)) # entradas

W = np.ones(X.shape) # pesos

S = np.zeros(len(X)) # intermediário

Y = np.zeros(len(X)) # saída

Eac = 0.5 # erro aceitável
alpha = 0.5
lamb = 0.5 # lambda

E = np.ones(len(X)) # erro final
D = np.array([0.5, -0.5, -0.5, -0.5]) # saída aceitável / desejável

# calculo da saída intermediaria

for i in range(0, len(X)):
    
    for e in range(0, len(X[i])):
        S[i] += X[i][e] * W[i][e]
    
    E[i] = D[i] - S[i]
 
# calcular o novo peso
for i in range (0,len(W)):
    if Eac < abs(E[i]):
        W[i] = W[i] + alpha * E[i] * (1/np.power(X[i],2)) * X[i]   

# saída usando relê 
for i in range(0, len(X)):
    if(S[i] >= 0):
        Y[i] = 1
    else:
        Y[i] = -1   

# saída usando sigmóide
for i in range (0, len(S)):
    Y[i] = (1-np.exp(-lamb * S[i])) / (1+np.exp(-lamb * S[i]))
    
                   
print(f"\033[1;92m {'   X1':<10} {'   X2':<10} {'  Bias':<10} {'    S':<10} {'    Y':<10}")
print('='*60, '\033[m')

for i in range (0, len(X)):
    for e in range(0, (len(X[i]))):
        print(f'{X[i][e]:>8.4f}', end=" | ")
    print(f'{S[i]:>8.4f}', end=" | ")
    print(f'{Y[i]:>8.4f}', end=" | ")
    print('')
