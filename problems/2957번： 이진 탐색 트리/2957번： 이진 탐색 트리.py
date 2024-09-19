#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2957                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2957                          #+#        #+#      #+#     #
#     Solved: 2024-09-12 06:03:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# N개의 수가 있는 배열 A의 수를 순서대로 삽입, 이진트리를 만든다
# 최악의 경우 N번수행하게 됨. 

# 어떤 수를 삽입할 때 증가하는 카운터의 수 = 그 수의 level임. 
# 그 수의 level은 그 부모의 level+1이고, 그 부모는 그 좌측에서 가장 가까운 수 or 우측에서 가장 가까운 수
# mostleft의 rightchild가 존재 + mostright의 leftchild가 부재 -> mostright의 leftchild에 넣기
# 그 역도 성립
# 둘 다 없다면? 그런건 없어용~ 
# leftmost와 rightmost를 찾고
# 둘 중 하나만 있다면 -> 거기에 넣으면 그만
# 둘 다 있을 때는 -> rightchild of leftmost or leftchild of rightmost 

# 세그먼트 트리 + 이진탐색으로 leftmost와 rightmost를 찾고 
# 규칙에 맞게 처리 


input = open(0).readline 
N = int(input())
A = [int(input()) for _ in range(N)]
LEVEL = [0] * (N+1)
L, R =  [0] * (N+1),  [0] * (N+1)
Counter = 0 

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
        while x>0:
            res += self.tree[x]
            x -= x&-x
        return res 
    
    def find_leftmost(self, x):
        s,e = 1,x 
        c = self.query(x)
        while s<=e:
            mid = (s+e)//2 
            if self.query(mid) < c-1:
                s = mid+1 
            else:
                e = mid-1 
        return s 


    def find_rightmost(self, x):
        s,e = x+1, self.n  # 오른쪽 범위 설정
        c = self.query(x)
        res = -1  # 찾은 지점을 저장할 변수
        while s<=e:
            mid = (s+e)//2
            query_mid = self.query(mid)
            if query_mid == c:
                s = mid+1  
            elif query_mid == c + 1:
                res = mid 
                e = mid-1  
            else:
                e = mid-1 
        return res  


    def cex(self, x):
        global Counter
        # 1. x가 들어옴 
        self.update(x, 1)

        # 2. 가장 왼쪽 수, 오른쪽 수를 찾기 
        left, right = self.find_leftmost(x), self.find_rightmost(x)

        # 3. left, right가 child를 하나라도 가지는지 검사 
        if not LEVEL[left]:
            LEVEL[x] = LEVEL[right]+1 
            L[right] = 1 
        elif not LEVEL[right]:
            LEVEL[x] = LEVEL[left]+1 
            R[left] = 1 
            
        elif R[left]:
            LEVEL[x] = LEVEL[right]+1 
            L[right] = 1 
        else:
            LEVEL[x] = LEVEL[left]+1 
            R[left] = 1    

        Counter += LEVEL[x]-1


fwtree = FenwickTree(N)

fwtree.update(A[0], 1)
LEVEL[A[0]] = 1 
ANS = [0]

for a in A[1:]:
    fwtree.cex(a)
    ANS.append(Counter)
print(*ANS, sep = '\n')