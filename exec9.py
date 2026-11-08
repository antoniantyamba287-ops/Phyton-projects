def calcular_media(notas):
    """Recebe uma lista de notas e devolve a média."""
    if len(notas)==0:
        return 0
    soma=sum(notas) #sum() soma todos os elementos
    return soma/len(notas) #média=soma/quantidade
notas_aluno = [7.5, 8.0, 6.5, 9.0]
media = calcular_media(notas_aluno)

print(f"Notas: {notas_aluno}")
print(f"Média: {media:.2f}")   # .2f formata com 2 casas decimais

if media >= 7:
    print("Aprovado ✅")
elif media >= 5:
    print("Recuperação ⚠️")
else:
    print("Reprovado ❌")