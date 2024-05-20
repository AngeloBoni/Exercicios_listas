t1 = input("Digite os elementos da primeira tupla separados por vírgula: ")
t2 = input("Digite os elementos da segunda tupla separados por vírgula: ")

elementos1 = t1.split(",")
elementos2 = t2.split(",")

primeira = tuple(elemento.strip() for elemento in elementos1)
segunda = tuple(elemento.strip() for elemento in elementos2)

print(f"Valor da primeira tupla: {primeira}")
print(f"Valor da segunda tupla: {segunda}")

aux = []

for i in primeira:
    if i not in aux:
        aux.append(i)

for i in segunda:
    if i not in aux:
        aux.append(i)

terceira = tuple(aux)

print(f"Valor da tupla resultante, sem repetições: {terceira}")