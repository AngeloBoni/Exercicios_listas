matriz = []
matriz2 = []
matriz3 = []

x = int(input("Qual o tamanho da primeira matriz?(A soma só sera possível com tamanhos iguais): "))
y = int(input("Qual o tamanho da segunda matriz?(A soma só sera possível com tamanhos iguais): "))

for i in range(x):
    lista = []
    lista1 = []
    for j in range(x):
     lista.append(int(input("Qual o valor da primeira matriz nos índices: [" + str(i) + "][" + str(j) + "]: ")))
     lista1.append(0)
    matriz.append(lista)
    matriz3.append(lista1)

for i in range(y):
    lista = []
    for j in range(y):
     lista.append(int(input("Qual o valor da segunda matriz nos índices: [" + str(i) + "][" + str(j) + "]: ")))
    matriz2.append(lista)

print("Primeira matriz: ")

for i in range(len(matriz)):
    print(matriz[i])

print("Segunda matriz: ")

for i in range(len(matriz2)):
    print(matriz2[i])

if x == y:


    print("Matriz resultante: ")

    for i in range(x):
        for j in range(x):
            matriz3[i][j] = matriz[i][j] + matriz2[i][j]
        print((matriz3[i]))

else:
    print("As matrizes não são iguais")