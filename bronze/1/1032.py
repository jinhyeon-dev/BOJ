n = int(input()) 
fw = list(input())
fwl = len(fw)

for i in range(n - 1):
    ow = list(input())
    for j in range(fwl):
        if fw[j] != ow[j]:
            fw[j] = '?'
            
print(''.join(fw))
    