#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1033                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1033                          #+#        #+#      #+#     #
#     Solved: 2024-06-11 09:37:34 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import lcm, gcd 
 
def dfs(a):
    for b,p,q in A[a]:
        #i는 (b,p,q)형태로 저장되어 있음
        if visited[b]:
            continue
        visited[b] = True
        P[b] = P[a]*q//p #v번째 상대가격을 이용한 next의 상대 가격
        dfs(b)
 
N = int(input())
A = [[] for _ in range(N)]
visited = [False]*N
P = [0]*N # 가격의 상대 비율
_lcm = 1
 
for i in range(N-1):
    a, b, p, q = map(int, input().split())
    _gcd = gcd(p,q)
    p,q = p//_gcd, q//_gcd
    A[a].append((b,p,q)) #a가 p가격일 때 b는 q 가격
    A[b].append((a,q,p)) #b가 q가격일 때 a는 p 가격    
    _lcm*= p*q*_gcd 
 
P[0] = _lcm # lcm(*_lcm)
visited[0] = True 
dfs(0)
_gcd = gcd(*P)
print(*[p//_gcd for p in P])