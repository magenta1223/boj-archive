#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12837                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12837                         #+#        #+#      #+#     #
#     Solved: 2024-09-25 06:32:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 

class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n 
        self.tree = [0] * (n+1)

    def update(self, x, delta):
        while x<=self.n:
            self.tree[x] += delta 
            x += x&-x
    
    def query(self, x):
        res = 0
        while x>0:
            res += self.tree[x]
            x -= x&-x 
        return res 
    
    def range_query(self, a, b):
        return self.query(b) - self.query(a-1)


N,Q = map(int, input().split())
fwtree = FenwickTree(N)
for _ in range(Q):
    a,b,c = map(int,input().split())
    if a==1:
        fwtree.update(b,c)
    else:
        print(fwtree.range_query(b,c))