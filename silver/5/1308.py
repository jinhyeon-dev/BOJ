import sys; input = sys.stdin.readline

def days(y, m, d):
    result = 365 * (y - 1) + d - 1 # 지나온 연도 + 지나온 일수

    # 윤년은 하루 더한다.
    for i in range(1, y):
        if not i % 400 or (not i % 4 and i % 100):
            result += 1

    # 지나온 월
    for i in range(1, m):
        if i & 1 ^ (i >= 8): # 홀수 달(8월부턴 짝수 달)은 31일
            result += 31
        elif i == 2: # 2월
            if not y % 400 or (not y % 4 and y % 100): # 윤년이면 29일
                result += 29
            else: # 아니면 28일
                result += 28
        else: # 나머지는 30일
            result += 30

    return result

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

# 1000년 이상 차이가 나면 'gg' 출력
if y2 - y1 > 1000 or (y2 - y1 == 1000 and (m1 < m2 or (m1 == m2 and d1 <= d2))):
    print('gg')

# 두 날짜의 일수 차이가 D-day가 된다.
else:
    print('D-%d' % (days(y2, m2, d2) - days(y1, m1, d1)))
