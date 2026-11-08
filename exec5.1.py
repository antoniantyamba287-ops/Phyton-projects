num=int(input("Quer a tabuada de qual número"))

for i in range(1,11):
    res=num*i          # ← tem recuo: está DENTRO do ciclo (repete 10 vezes)
    print(f"{num} x {i} = {res}")   # ← sem recuo: está FORA do ciclo (corre só 1 vez)