#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2268                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2268                          #+#        #+#      #+#     #
#     Solved: 2024-08-13 01:57:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



input = open(0).readline 

N,M = map(int,input().split())

class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n 
        self.tree = [0] * (n+1)

    def update(self, x, delta):
        while x <= self.n:            
            self.tree[x] += delta 
            x += x&-x 
 
    def query(self, x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x -= x&-x 
        return res 
    
    def range_query(self, i, j):
        return self.query(j) - self.query(i-1)


fwtree = FenwickTree(N)
arr = [0] * (N+1)


for _ in range(M):
    f,i,jk = map(int, input().split())

    if f:
        fwtree.update(i, jk - arr[i]) 
        arr[i] = jk 
    else:
        print(fwtree.range_query(*sorted([i,jk]))) 



"""
3 5
0 1 3
1 1 2
1 2 3
0 2 3
0 1 3

"""