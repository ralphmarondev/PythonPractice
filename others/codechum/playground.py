t = [[[k for k in range(5)] for j in range(5)] for i in range(5)]

print(t)
for i in range(5):
    for j in range(5):
        for k in range(5):
            print(t[i][j][j],end="")
        print()
