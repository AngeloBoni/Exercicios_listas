lista = []

i = 0
soma = 0;
x = " "
while x != "n":
    numero = int(input("Adicione um número para ser somado: "))
    lista.append(numero)
    v = input("Deseja continuar?(S/N): ")
    x = v.lower()

for i in range(0, len(lista), 1):
    soma = soma + lista[i]

print("A soma dos elementos " + str(lista) + " é: "+str(soma))