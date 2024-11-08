import math

# Definir o intervalo [a, b] e o erro relativo
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
erro = float(input("Digite o valor do erro relativo (ex: 0.01): "))

# Definir a função f(x)
funcao_str = input("Digite a função f(x) (exemplo: x**2 - 5): ")

# Função de avaliação
def f(x):
    # Avaliar a função usando eval com um escopo restrito para segurança
    return eval(funcao_str, {"x": x, "math": math})

# Verificar se a função muda de sinal no intervalo [a, b]
if f(a) * f(b) < 0:
    while math.fabs(b - a) / 2 > erro:
        x = (a + b) / 2
        if f(x) == 0:
            print("A raiz da função é:", x)
            break
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
    # Exibir o valor aproximado da raiz
    print("A raiz aproximada da função é:", x)
else:
    print("Não há raiz nesse intervalo.")
