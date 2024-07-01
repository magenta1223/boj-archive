#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1700                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1700                          #+#        #+#      #+#     #
#     Solved: 2024-05-16 11:07:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def find_last(k,p):
    # k번째 이후로, p가 나오는 인덱스를 찾아보자 
    return A[k:].index(p) + k if p in A[k:] else float("inf") 
 
N,K = map(int,input().split())
A = list(map(int,input().split()))
 
PLUGS = [0] * N
ans = 0
 
for k in range(K):
    if A[k] in PLUGS:
        continue 
    if 0 in PLUGS:
        PLUGS[PLUGS.index(0)] = A[k]
    else:
        # 가장 마지막걸 뺀다고
        idx, target = -1, -1 
        for p in PLUGS:
            # A에서 p가 나오는 마지막 인덱스 
            _idx = find_last(k,p)
            if idx < _idx:
                idx = _idx
                target = p     
 
        PLUGS[PLUGS.index(target)] = A[k]
        ans += 1 
 
print(ans)