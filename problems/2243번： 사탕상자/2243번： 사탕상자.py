#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2243                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2243                          #+#        #+#      #+#     #
#     Solved: 2024-08-02 08:55:58 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 맛의 범위는 1~1_000_000. 숫자가 작을수록 좋다 
# cmd는 A,B or A,B,C
# A,B: B번째로 맛있는 사탕을 꺼내서 준다,  
# A,B,C: 맛이 B인 사탕을 C개 추가한다. 

# 사탕의 최대 갯수는 2B개. 
# 없는 사탕을 꺼내는 경우는 없다. 

# 꺼내는 사탕의 맛의 번호를 출력 

# fenwick tree
# 1. arr: 길이는 1M. arr[i] = 맛이 i인 사탕의 개수 
# 2. fenwick tree: arr의 누적합을 계산 

# 3. 쿼리 수행
# 1) 꺼내기: 트리의 값이 B이상이 되는 지점을 찾으면 됨 -> 이분탐색 
# 2) 넣기: 트리의 값 변경 

input = open(0).readline 

class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n 
        self.tree = [0] * (n+1) 
    
    def update(self, i, x):
        while i <= self.n:
            self.tree[i] += x
            i += i&-i

    def query(self, x):
        res = 0 
        while x > 0:
            res += self.tree[x]
            x -= x&-x
        return res 
    
    def pop(self, b):
        # 1. 이분탐색으로 누적합이 b개 이상이 되는 최소지점을 찾고 
        # 2. 그 지점의 갯수를 -1  
        # 3. 리턴 
        s, e = 1, self.n # 펜윅트리는 인덱스가 1부터 N개임 
        while s<=e:
            mid = (s+e)//2 
            
            if self.query(mid) >= b:
                e = mid-1 
            else:
                s = mid+1
        
        self.update(s, -1)
        return s 
    


N = int(input())

tree = FenwickTree(1_000_000)

for _ in range(N):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        B = cmd[1] 
        print(tree.pop(B))
    else:
        B,C = cmd[1:]
        tree.update(B,C)