# Exercício 1:
# Enunciado: Crie uma função em Python para calcular a soma dos termos de uma série geométrica infinita,
# dada a razão (r) e o primeiro termo (a1).

def soma_serie_geometrica(a1, r, n):
    soma = a1 * (1 - r**n) / (1 - r)
    return soma

# Exemplo de uso
a1 = 2
r = 0.5
n = 5
resultado = soma_serie_geometrica(a1, r, n)
print(f'A soma dos primeiros {n} termos da série é: {resultado}')

# Exercício 2:
# Enunciado: Implemente uma função para calcular o valor aproximado de π usando a série de Gregory-Leibniz até o n-ésimo termo.

def aproximar_pi(n):
    soma = 0
    for k in range(n):
        soma += ((-1)**k) / (2*k + 1)
    return 4 * soma

# Exemplo de uso
n = 100000
pi_aproximado = aproximar_pi(n)
print(f'Valor aproximado de π com {n} termos: {pi_aproximado}')

# Exercício 3:
# Enunciado: Escreva uma função para calcular a soma dos termos da série de Taylor para a função exponencial (e^x) até o n-ésimo termo.

import math

def soma_serie_exponencial(x, n):
    soma = sum((x**k) / math.factorial(k) for k in range(n))
    return soma

# Exemplo de uso
x = 2
n = 10
resultado_exponencial = soma_serie_exponencial(x, n)
print(f'Valor aproximado de e^{x} com {n} termos: {resultado_exponencial}')

# Exercício 4:
# Enunciado: Crie uma função para calcular a soma dos termos da série de Fourier para uma função quadrada até o n-ésimo termo.

import numpy as np
import matplotlib.pyplot as plt

def soma_serie_fourier_quadrada(x, n):
    soma = 0
    for k in range(1, n+1, 2):
        soma += (1/k) * np.sin(k * x)
    return (4/np.pi) * soma

# Exemplo de uso
x_vals = np.linspace(0, 2*np.pi, 1000)
n = 5
y_vals = [soma_serie_fourier_quadrada(x, n) for x in x_vals]

plt.plot(x_vals, y_vals, label=f'Série de Fourier (n={n})')
plt.title('Aproximação de uma função quadrada usando Séries de Fourier')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Exercício 5:
# Enunciado: Implemente uma função para calcular a soma dos termos da série de potência para a função seno até o n-ésimo termo.

def soma_serie_seno(x, n):
    soma = sum(((-1)**k) * (x**(2*k+1)) / math.factorial(2*k+1) for k in range(n))
    return soma

# Exemplo de uso
x = 1
n = 10
resultado_seno = soma_serie_seno(x, n)
print(f'Valor aproximado de sen({x}) com {n} termos: {resultado_seno}')
