n, m = map(int, input().split())

src = []
for _ in range(n):
    tmp = []
    for i in input():
        tmp.append(i)
    tmp = list(map(int, tmp))
    src.append(tmp)
cnt = 0
for i in range(n - 1, -1, -1):
    for j in range( -1, -1, -1):
        if src[i][j]:
            cnt += 1
            for k in range(i + 1):
                for f in range(j + 1):
                    if src[k][f] == 1:
                        src[k][f] = 0
                    else:
                        src[k][f] = 1
print(cnt)