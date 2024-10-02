n, m = map(int, input().split())

mtr = []
cnt = []
for i in range(n):
    mtr.append(input())
    
for a in range(n - 7):
    for b in range(m - 7):
        windex = 0
        bindex = 0
        for i in range(a, a+8):
            for j in range (b, b+8):
                if (i+j)%2==0:
                    if mtr[i][j] != 'W':
                        windex += 1
                    else:
                        bindex += 1
                else:
                    if mtr[i][j] != 'W':
                        bindex += 1
                    else:
                        windex += 1
                        
        cnt.append(windex)
        cnt.append(bindex)
print(min(cnt))