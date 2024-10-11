sub = int(input())

scr = list(map(int, input().split()))

m = max(scr)

for i in range(sub):
    scr[i] = scr[i] / m*100

print(sum(scr)/sub)