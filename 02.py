c = int(input("Qual o comprimento do retângulo?: "))
h = int(input("Qual a altura do retângulo?: "))



for i in range(h):
    if(i == 0 or i == h - 1):
        print("*" * c)
    for j in range(c):
        if(j == 0 and i < h - 2):
            print("*" + " " * (h - 2) + "*")