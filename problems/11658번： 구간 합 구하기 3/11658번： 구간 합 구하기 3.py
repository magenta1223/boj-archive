#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11658                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11658                         #+#        #+#      #+#     #
#     Solved: 2024-07-01 19:06:06 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

class FenwickTree2D:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.tree = [[0] * (m + 1) for _ in range(n + 1)]
    
    def update(self, x, y, delta):
        i = x + 1
        while i <= self.n:
            j = y + 1
            while j <= self.m:
                self.tree[i][j] += delta
                j += j & -j
            i += i & -i
    
    def query(self, x, y):
        sum_ = 0
        i = x + 1
        while i > 0:
            j = y + 1
            while j > 0:
                sum_ += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return sum_
 
def range_query(ft2d, x1, y1, x2, y2):
    return (ft2d.query(x2, y2)
            - (ft2d.query(x1 - 1, y2) if x1 > 0 else 0)
            - (ft2d.query(x2, y1 - 1) if y1 > 0 else 0)
            + (ft2d.query(x1 - 1, y1 - 1) if x1 > 0 and y1 > 0 else 0))
 
input = open(0).readline
 
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ft2d = FenwickTree2D(N, N)
 
# Initialize Fenwick Tree with initial array values
for i in range(N):
    for j in range(N):
        ft2d.update(i, j, A[i][j])
 
for _ in range(M):
    query = list(map(int, input().split()))
    if query[0] == 0:  # update operation
        x, y, value = query[1] - 1, query[2] - 1, query[3]
        delta = value - A[x][y]
        A[x][y] = value
        ft2d.update(x, y, delta)
    else:  # range sum query
        x1, y1, x2, y2 = query[1] - 1, query[2] - 1, query[3] - 1, query[4] - 1
        result = range_query(ft2d, x1, y1, x2, y2)
        print(result)