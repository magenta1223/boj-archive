#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1796                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1796                          #+#        #+#      #+#     #
#     Solved: 2024-04-25 12:45:59 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from string import ascii_lowercase
 
INF = float('inf')
 
def dist(a, b, l, r): # (a,l,r,b), (a,r,l,b) 비용 중 작은 값 
    return min(abs(a-l)+abs(l-r)+abs(r-b), abs(a-r)+abs(r-l)+abs(l-b))
 
def solve(alpha, pos):
    if alpha == 26:
        return 0
    
    if cache[alpha][pos] != -1:
        return cache[alpha][pos]
    
    ret = INF
    l, r = left[alpha], right[alpha]
    if exist[alpha]:
        for i in range(N):
            # 현재 위치 pos에서 현재 알파벳을 모두 누른 후, i로 가서 다음 알파벳을 누르기 
            ret = min(ret, solve(alpha+1, i) + dist(pos, i, l,r))
    else:
        ret = solve(alpha+1, pos)
    cache[alpha][pos] = ret
    return ret
 
S = input().strip()
N = len(S)
cache = [[-1] * N for _ in range(26)]
left,right = [INF] * 26, [-1] * 26
exist = [False] * 26
 
for j in range(N):
    idx = ascii_lowercase.index(S[j])
    exist[idx] = True
    if left[idx] == INF:
        left[idx] = j
    right[idx] = j
 
print(solve(0, 0) + N)
 