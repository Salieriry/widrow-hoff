import os
import numpy as np
import windrow as wd

def interface():
    os.system( 'cls' if os.name == 'nt' else 'clear')

    print('\033[1;33m='*60)
    print('{: ^60}'.format('Widrow-Hoff'))
    print('='*60)
    print('\033[m')
    
    while True:
        try:
            Eac = float(input("Insira o valor do erro aceitável (padrão 0.5): "))
            if (Eac > 0):
                break
            else:
                print("Inserindo valor padrão.")
                Eac = 0.5
                break
        except ValueError:
            print("Entrada inválida. Por favor insira um número.")
               
    while True:
        try:
            alpha = float(input("Insira o valor do alfa (padrão 0.5): "))
            if (alpha >= 0 and alpha <= 2):
                break
            else:
                print("Inserindo valor padrão.")
                alpha = 0.5
                break
        except ValueError:
            print("Entrada inválida. Por favor insira um número.")
            
    while True:
        try:
            lamb = float(input("Insira o valor do lambda (padrão 0.5): "))
            if (lamb > 0):
                break
            else:
                print("Inserindo valor padrão.")
                lamb = 0.5
                break
        except ValueError:
            print("Entrada inválida. Por favor insira um número.")
              
    while True:
        try:
            print("")
            iteracoes = int(input("Insira a quantidade de iterações (padrão 2): "))
            if (iteracoes > 0):
                break
            else:
                print("Inserindo valor padrão")
                iteracoes = 2
                break
        except ValueError:
            print("Entrada inválida. Por favor insira um número.")
    
    X = np.array([
                [1,1], 
                [1,-1], 
                [-1,-1], 
                [-1,1]
            ])
    
    bias = np.ones((len(X),1))

    X = np.hstack((X, bias)) # entradas
    
    W = np.ones(X.shape) # pesos
    
    wd.windrow_holff(X, bias, W, Eac, alpha, lamb, iteracoes)
    
    
        