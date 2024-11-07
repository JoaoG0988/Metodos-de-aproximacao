import math

# Definir o intervalo [a, b] e o erro relativo

a = 4
b = 6
erro = 0.01

# Definir a função f(x)

def f(x):
    return x**2 - 5

# Verificar se a função muda de sinal no intervalo [a, b]
if f(a) * f(b) < 0:
    while (math.fabs(b-a) / 2 > erro):
        x = (a + b) / 2
        if f(x) == 0:
            print("A raiz da função é: ", x)
            break
        else:
            if f(a) * f(x) < 0:
                b = x
            else:
                a = x
    print("A raiz da função é: ", x)

else:
    print("Não há raíz nesse intervalo")
    
    
    


