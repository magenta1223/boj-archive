#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 31937                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/31937                         #+#        #+#      #+#     #
#     Solved: 2024-07-11 03:46:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
N,M,K = map(int,input().split())
Infested = set(map(int,input().split()))
Logs = [list(map(int,input().split())) for _ in range(M)]
Logs.sort()

# 둘 다 감염된 최초의 시간은 아님.
# 그걸 전송하고 나중에 감염됐을 수도 

# t순으로 정렬하고
# infested의 각 컴퓨터에 대해 감염시뮬레이션 시작 
# 정답이 Infested인가? 

def solve(start):
    infested = set([start])
    for t,a,b, in Logs:
        if a in infested:
            infested.add(b)
    return infested

for start in Infested:
    res = solve(start)
    if res == Infested:
        ans = start 
        break 
print(ans)