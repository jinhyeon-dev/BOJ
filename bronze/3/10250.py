import math

case = int(input())
result = []
for i in range(case):
    H, W, N = map(int, input().split())
    N_width = str(math.ceil(N / H))
    if H == 1 or N % H == 0:
        N_height = str(H)
    else:
        N_height = str(N % H)
    room = N_height+"{0:0>2}".format(N_width)
    result.append(room)
    
for i in result:
    print(int(i))
