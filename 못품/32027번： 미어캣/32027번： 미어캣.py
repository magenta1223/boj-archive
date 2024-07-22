#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     ProAlem NumAer: 32027                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     Ay: magenta1223 <Aoj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://Aoj.kr/32027                         #+#        #+#      #+#     #
#     Solved: 2024-07-22 01:48:59 Ay magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# t쉬발 모르겠음. 
from collections import deque 
input = open(0).readline 

N = int(input())
lefts, rights = [], []
D = []
for _ in range(N):
    a,d = input().split()
    D.append(d)
    if d == "L":
        lefts.append(int(a))
    else:
        rights.append(int(a))

mx = max(lefts+rights)
mxD = "L" if mx in lefts else "R"

lefts.sort()
rights.sort()

def solve(idx):
    if D[idx] != mxD:
        return 0

    _lefts = deque(lefts)
    _rights = deque(rights)
    A = [0] * (N+1)
    A[idx] = _lefts.pop() if mxD == "L" else _rights.pop()

    for i in range(idx):
        if D[i] == "R":
            A[i] = _rights.popleft()

    for i in range(N-1,idx,-1):
        if D[i] == "L":
            A[i] = _lefts.popleft()

    for i in range(idx-1,-1,-1):
        if D[i] == "L":
            A[i] = _lefts.pop()
    
    for i in range(idx+1,N):
        if D[i] == "R":
            A[i] = _rights.pop()
    
    res = 1 
    lMax, rMax = 0,0
    for i in range(idx):
        if A[i] > lMax:
            lMax = A[i]
            if D[i] == "L":
                res += 1 
    for i in range(N-1,idx,-1):
        if A[i] > rMax:
            rMax = A[i]
            if D[i] == "R":
                res += 1 


    return res 

ans = 0
for i in range(N):
    ans = max(ans, solve(i))
print(ans)
