a=int(input("Digite um numero: "))
b=int(input("Digite outro numero: "))
c=int(input("Digite outro numero: "))

if a>=b and a>=c:
    maior=a
elif b>=a and b>=c:
    maior=b
else:
    maior=c
print(f"O maior numero é {maior}")