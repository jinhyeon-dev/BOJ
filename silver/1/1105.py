L, R = input().split()

# 두 수의 자리수가 다른 경우 8이 들어가는 횟수는 최소 0이 나온다.
answer = 0
if len(L) != len(R):
    answer = 0
# 그렇다면 자리수가 같으 경우에 대해서 생각
# 앞에서부터 생각해서
# 각 자리수가 같은 8이면 +1 다음 생각
# 자리수의 숫자가 8이 아니고 같으면 +0 다음 생각
# 자리수의 숫자가 다르면 그대로 끝 - 최소이므로 다음을 생각할 필요가 없다
else:
    for i in range(len(L)):
        if L[i] == '8' and R[i] == '8':
            answer += 1
        elif L[i] != R[i]:
            break

print(answer)