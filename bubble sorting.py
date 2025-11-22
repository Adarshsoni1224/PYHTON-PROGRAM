n = [5, 15, 6, 8, 1, 12, 24]
for i in range(len(n)):
    for j in range(len(n) - 1):
        if n[j] > n[j + 1]:
            n[j], n[j + 1] = n[j + 1], n[j]
print(n)