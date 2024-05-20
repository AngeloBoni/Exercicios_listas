import random
vezes = [0, 0, 0, 0, 0, 0]

y = int(input("Quantas vezes lançar o dado?: "))

for i in range(y):

    x = random.randint(1, 6)

    vezes[x - 1] += 1

for i in range(6):
    print("Ocorrências de " + str(i + 1) + ": " + str(vezes[i]))