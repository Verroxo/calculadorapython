import math
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
raiz = soma * soma
potencia = pow(soma, 2)
arredondado = round(soma)
numeromaximo = max(num1, num2)


print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Raiz:", raiz)
print("Potenciacão:", potencia)
print("Numero arredondado:", arredondado)
print("Numero máximo:", numeromaximo)
print("Raiz:", math.sqrt(soma + soma))
