seq = [1, 2, 3, 4, 5]
seq2 = []

for i in range(len(seq) -1, -1, -1):
  seq2.append(seq[i])

print(seq2)