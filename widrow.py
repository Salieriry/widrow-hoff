import numpy as np


def novo_peso(W, X, E, Eac, alpha):
    # calcular o novo peso
    
    for i in range (0,len(W)):
        if Eac < abs(E[i]):
            norma_x = np.dot(X[i], X[i])
            W[i] = W[i] + alpha * E[i] * ((1/norma_x) * X[i]) 
            #W[i] = W[i] + alpha * E[i] * (1/np.power(X[i],2)) * X[i] 

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

def windrow_holff(X, bias, W, Eac, alpha, lamb, iteracoes):
    

    Y = np.zeros(len(X)) # saída
    S = np.zeros(len(X))
    E = np.zeros(len(X)) # erro final
    D = np.array([0.5, -0.5, -0.5, -0.5]) # saída aceitável / desejável
    
    
    for epoca in range(iteracoes):
        
        maior_erro = 0       
        for i in range(0, len(X)):
            
            S[i] = 0
            # calculo da saída intermediaria
            for e in range(0, len(X[i])):
                S[i] += X[i][e] * W[i][e]
            
            E[i] = D[i] - S[i]
            if (abs(E[i]) > maior_erro):
                maior_erro = abs(E[i])
                
        print(f"Maior erro: {maior_erro}")
        
        if maior_erro <= Eac:
            print(f"\033[1;92m Treinamento concluído (Iteração {epoca+1}): Erro {maior_erro} menor ou igual a {Eac}")
    
            break
        
        novo_peso(W, X, E, Eac, alpha) 
            
        saida_rele(X, S, Y)
        
        print(f"\033[1;92m {' ':<20} Iteração {epoca+1} ")                    
        print(f"\033[1;92m {'   X1':<10} {'   X2':<10} {'  Bias':<10} {'    S':<10} {'    Y':<10}")
        print('='*60, '\033[m')

        for i in range (0, len(X)):
            for e in range(0, (len(X[i]))):
                print(f'{X[i][e]:>8.4f}', end=" | ")
            print(f'{S[i]:>8.4f}', end=" | ")
            print(f'{Y[i]:>8.4f}', end=" | ")
            print('')
        print('\n')
        
        
        
        
        
    
    