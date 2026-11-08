n1=float(input("Digite o primeiro numero: "))
n2=float(input("Digite o segundo numero: "))
soma=n1+n2
subtracao=n1-n2
multiplicacao=n1*n2
divisao=n1/n2

if n2!=0:
    divisao=n2/n1
else :
    divisao="indefinida(divisão por zero)"

print(f"\nSoma: {soma}")
print(f"Subtração:     {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão:       {divisao}")