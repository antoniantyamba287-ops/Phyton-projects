n=int(input("Somar de 1 até:"))

soma=0 #acumulador

contador=1 #controla o laço

while contador <= n:
    soma=soma+contador #acumula
    contador=contador+1 #avança

print(f"A soma de 1 até {n} é {soma} ")