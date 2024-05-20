lista = []
x = ""

while x != "n":
    lista.append((int(input("Adicione um número a lista: "))))
    x = input("Deseja continuar?(S/N): ")
    x.lower()

cont = 0

for i in range(len(lista)):
    if(lista[i] > cont):
        cont = lista[i]

print("O maior número dessa lista é: " + str(cont))