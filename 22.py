entrada = input("Digite os números da tupla separados por vírgula: ")
elementos = entrada.split(",")
tupla = tuple(int(elemento.strip()) for elemento in elementos)

aux = []

for i in tupla:
    if not(i in aux):
        aux.append(i)

print(f"Tupla geraada: {tupla}\n")
print(f"A tupla possui {len(aux)} elementos únicos")