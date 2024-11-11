import math

# Definir o chute inicial x0 e o erro relativo
x0 = float(input("Digite o valor inicial x0: "))
erro = float(input("Digite o valor do erro relativo (ex: 0.01): "))

# Definir a função g(x)
funcao_g_str = input("Digite a função g(x) na forma x = g(x) (exemplo: (x**2 + 5)/6): ")

# Função g(x) para o método de ponto fixo
def g(x):
    # Avaliar a função usando eval com escopo restrito para segurança
    return eval(funcao_g_str, {"x": x, "math": math})

# Implementação do método de ponto fixo 
def ponto_fixo(x0, erro):
    x_anterior = x0
    iteracao = 0
    
    while True:
        x_atual = g(x_anterior)
        iteracao += 1
        print(f"Iteração {iteracao}: x = {x_atual}")

        # Verificar se o erro relativo atende ao critério de parada
        if abs(x_atual - x_anterior) < erro:
            print(f"A raiz aproximada é: {x_atual}")
            return x_atual
        x_anterior = x_atual


raiz = ponto_fixo(x0, erro)
