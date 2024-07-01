#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1517                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1517                          #+#        #+#      #+#     #
#     Solved: 2024-07-01 03:53:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# Segtree 

# Segtree에는 idx에 해당하는 범위에 n보다 작은 자연수가 몇 개 존재하는지를 저장함. 
# 쿼리를 할건데
# N미만의 인덱스 i에 대해
# i번째 이후에 i보다 작은 수의 개수를 찾아서 리턴 


from math import log2, ceil

N = int(input())
A = list(map(int, input().split()))
TREE = [0] * ( 1 << (ceil(log2(N)) + 1))

def update(idx, s, e):
    if not s<=target<=e: 
        return TREE[idx]
    if s==e:
        TREE[idx]=1
        return TREE[idx]
    mid = (s+e)//2 
    TREE[idx]=update(idx*2, s, mid)+update(idx*2+1, mid+1, e)
    return TREE[idx]

def query(idx,s,e):
    if e<frm or to<s:
        return 0
    if frm<=s and e<=to:
        return TREE[idx]
    mid = (s+e)//2 
    return query(idx*2, s, mid) + query(idx*2+1, mid+1, e)


wIdx = [(A[i], i) for i in range(N)]
wIdx.sort(key = lambda x: x[0])
ans=0
for i in range(N):
    _, target=wIdx[i]
    frm, to = target+1, N-1
    ans += query(1,0,N-1)
    update(1,0,N-1)

print(ans)