#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1517                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1517                          #+#        #+#      #+#     #
#     Solved: 2024-07-10 02:39:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



input = open(0).readline 

N = int(input())
A = list(map(int,input().split()))
A = [(A[i], i) for i in range(N)]
A.sort()

# 펜윅 
class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n 
        self.tree = [0] * (n+1)

    def update(self, x, delta):
        while x <= self.n:
            self.tree[x] += delta 
            x += x&-x
    
    def _query(self, x):
        _sum = 0
        while x > 0:
            _sum += self.tree[x] 
            x -= x&-x
        return _sum 
    
    def query(self, frm, to):
        return self._query(to) - self._query(frm-1)

fwtree = FenwickTree(N)
ans = 0
for i in range(N):
    value, idx = A[i]
    # value가 나보다 작으면서 index가 나보다 큰 수의 개수 
    fwtree.update(idx+1, 1)
    ans += fwtree.query(idx+2,N)


print(ans)