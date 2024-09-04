#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3653                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3653                          #+#        #+#      #+#     #
#     Solved: 2024-09-03 06:27:01 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 맨 위로 올리는 경우만 존재 
# -> 앞에 M개를 비워놓고, 그 앞에 차례대로 삽입 

class FenwickTree:
    def __init__(self, n):
        self.n = n 
        self.tree = [0] * (n+1)

    def update(self, x, delta):
        while x<=self.n:
            self.tree[x] += delta 
            x += x&-x 
        
    def get(self, x):
        res = 0 
        while x > 0:
            res += self.tree[x]
            x -= x&-x 
        return res 

for _ in range(int(input())):
    N,M = map(int, input().split())
    RENTAL = list(map(int, input().split()))
    
    pos = [i+M for i in range(N+1)]
    fwtree = FenwickTree(N+M)

    for i in range(1,N+1):
        fwtree.update(M+i,1)

    ans = []
    for i in range(M):
        r = RENTAL[i]
        ans.append(fwtree.get(pos[r]-1))
        fwtree.update(pos[r], -1)
        fwtree.update(M-i, 1)
        pos[r] = M-i 
    print(*ans)

