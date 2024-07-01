#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11658                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11658                         #+#        #+#      #+#     #
#     Solved: 2024-07-01 09:05:06 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 2차원 세그먼트트리임. 
# 일단 1차원 세그먼트 트리를 작성하고 이를 2차원에 맞게 조회 및 수정하는 방법을 찾아봅시다. 

# https://seongmok.com/5 참고. 


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
                self.tree[i][j] += delta # 편차만큼 트리의 값을 변경 
                j += j & -j # 가장 오른쪽 1 제거 
                # 1. 음수의 bimask: bitmask반전 한 다음+1 
                # 2. 그 결과는 원래 정수의 bitmask에서 가장 오른쪽 1부터 같은 숫자가 나타남. 그 앞은 전부 다르고
                # 3. & 연산자를 취하면 같은 부분만 남는다. 
                # 4. 이를 원래 정수에서 빼주면 가장 오른쪽 1이 제거됨
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
    
    def range_query(self, x1, y1, x2, y2):
        # 누적합 구하듯이
        return (self.query(x2, y2)
                - (self.query(x1 - 1, y2) if x1 > 0 else 0)
                - (self.query(x2, y1 - 1) if y1 > 0 else 0)
                + (self.query(x1 - 1, y1 - 1) if x1 > 0 and y1 > 0 else 0))

input = open(0).readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ft2d = FenwickTree2D(N, N)

for i in range(N):
    for j in range(N):
        ft2d.update(i, j, A[i][j])

for _ in range(M):
    query = list(map(int, input().split()))
    if query[0] == 0:  
        x, y, value = query[1] - 1, query[2] - 1, query[3]
        delta = value - A[x][y]
        A[x][y] = value
        ft2d.update(x, y, delta)
    else:  # range sum query
        x1, y1, x2, y2 = query[1] - 1, query[2] - 1, query[3] - 1, query[4] - 1
        result = ft2d.range_query(x1, y1, x2, y2)
        print(result)




# 한방에 2D를 하는건 어려우니
# 1. 각 줄별로 세그트리를 수행하고 
# 2. 각 줄에 대해서 쿼리를 스르륵 날려서 구하면 되겠다 .. 그치? 
# 예상대로 졸라느림.. 

# 1. 2차원 array를 1d로 편 이후
# 2. 트리에서 index를 잘.. ? 


"""
4 2
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
1 2 2 3 4
1 3 4 3 4

ans
27
6





"""