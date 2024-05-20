notas = []
peso = []
somapeso = 0
soma = 0

x = int(input("Quantas notas serão digitadas?: "))

for i in range(x):
    notas.append(float(input("Digite a " + str(i + 1) + "ª nota: ")))
    peso.append(int(input("Digite o peso dessa nota: ")))

for i in range(len(notas)):
    soma = (notas[i] * peso[i]) + soma
    somapeso += peso[i]

media = soma / somapeso

media = round(media, 2)

print("A média ponderada é: " + str(media))