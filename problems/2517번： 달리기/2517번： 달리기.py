#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2517                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2517                          #+#        #+#      #+#     #
#     Solved: 2024-08-21 09:52:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


input = open(0).readline 

N = int(input())
A = [(int(input()), i) for i in range(N)]
B = sorted(A)

for j, (v, i) in enumerate(B):
    A[i] = j+1 

class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n 
        self.tree = [0] * (n+1)
        self.total = 0 
    def update(self, x):
        self.total += 1 
        while x <= self.n:
            self.tree[x] += 1  
            x += x&-x
    
    def query(self, x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x -= x&-x 
        return res 
    
    def range_query(self, x):
        return self.total - self.query(x-1)
    
fwtree = FenwickTree(N)
ans = []
for i in range(N):
    fwtree.update(A[i])
    ans.append(fwtree.range_query(A[i]))
print(*ans, sep = '\n')