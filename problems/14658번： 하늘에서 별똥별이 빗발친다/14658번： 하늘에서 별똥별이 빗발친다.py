#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14658                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14658                         #+#        #+#      #+#     #
#     Solved: 2024-05-09 11:26:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def count(l,r,u,d):
    return sum([1 for x,y in S if l<=x<=r and d<=y<=u])
N,M,L,K = map(int, input().split())
S = [list(map(int,input().split())) for _ in range(K)]
ans=  0
for i in range(K):
    l = S[i][0]
    r = l+L
    for j in range(K):
        d = S[j][1]
        u = d+L 
        ans = max(ans, count(l,r,u,d))
print(K-ans)