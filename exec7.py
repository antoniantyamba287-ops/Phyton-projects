compras=[] #lista vazia

while True:
    item=input("Item(ou 'sair' para terminar):")

    if item.lower()== "sair":
        break

    compras.append(item)  #adiciona no final da lista

    print(f"\nVocê adicionou {len(compras)} itens:")
    for item in compras:
        print(f"- {item}")