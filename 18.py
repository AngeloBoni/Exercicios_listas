lista = []
contagem = [0, 0, 0, 0, 0]

for i in range(5):
    lista.append(input(f"Digite a {i + 1}ª palavra: "))

print(f"Os as palavras digitadas foram: {lista}")

for v in lista:
    for letra in v:
        if letra.lower() in "a":
            contagem[0] = contagem[0] + 1
        elif letra.lower() in "e":
            contagem[1] = contagem[1] + 1
        elif letra.lower() in "i":
            contagem[2] = contagem[2] + 1
        elif letra.lower() in "o":
            contagem[3] = contagem[3] + 1
        elif letra.lower() in "u":
            contagem[4] = contagem[4] + 1

print(f"Nessas palavras ocorreram:\n "
      f"{contagem[0]} ocorrências da letra 'A'\n"
      f"{contagem[1]} ocorrências da letra 'E'\n"
      f"{contagem[2]} ocorrências da letra 'I'\n"
      f"{contagem[3]} ocorrências da letra 'O'\n"
      f"{contagem[4]} ocorrências da letra 'U'")