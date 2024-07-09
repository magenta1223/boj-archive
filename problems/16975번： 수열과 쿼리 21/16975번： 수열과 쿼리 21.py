#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16975                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16975                         #+#        #+#      #+#     #
#     Solved: 2024-07-09 05:56:53 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
N = int(input())
A = list(map(int,input().split()))
M = int(input())

class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n 
        self.tree = [0] * (n+1)
    
    def _update(self, x, delta):
        i = x 
        while i<=self.n:
            self.tree[i] += delta 
            i += i&-i 

    def update(self, frm, to, delta):
        self._update(frm, delta)
        self._update(to+1, -delta) 

    def query(self, x):
        _sum = 0 
        i = x 
        while i > 0:
            _sum += self.tree[i]
            i -= i&-i 
        return _sum 


fwtree = FenwickTree(N)

for i in range(N):
    fwtree.update(i+1, i+1, A[i])


for _ in range(M):
    query = list(map(int,input().split()))

    if query[0] == 1:
        i,j,k = query[1:]
        fwtree.update(i,j,k)
    else:
        x = query[1]
        print(fwtree.query(x))
