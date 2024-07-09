#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11658                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11658                         #+#        #+#      #+#     #
#     Solved: 2024-07-09 05:26:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

class FenwickTree2D:
    def __init__(self, n, m) -> None:
        self.n = n 
        self.m = m 
        self.tree2d = [[0] * (m+1) for _ in range(n+1)]

    def update(self, x, y, delta):
        i = x 
        while i <= self.n:
            j = y 
            while j <= self.m:
                self.tree2d[i][j] += delta 
                j += j&-j 
            i += i&-i 
                
    def _query(self, x, y):
        _sum = 0 
        i = x 
        while i > 0:
            j = y 
            while j > 0:
                _sum += self.tree2d[i][j]
                j -= j&-j 
            i -= i&-i 

        return _sum
    

    def query(self, x1,y1, x2,y2):
        return self._query(x2,y2) - self._query(x2,y1-1) - self._query(x1-1, y2) + self._query(x1-1, y1-1)


fwtree2d = FenwickTree2D(N,N)

for i in range(N):
    for j in range(N):
        fwtree2d.update(i+1, j+1, A[i][j])

for _ in range(M):
    query = list(map(int, input().split()))
    if query[0]:
        x1,y1,x2,y2 = query[1:]
        print(fwtree2d.query(x1,y1,x2,y2))
    else:
        x,y,c = query[1:]
        fwtree2d.update(x,y,c-A[x-1][y-1])
        A[x-1][y-1] = c 