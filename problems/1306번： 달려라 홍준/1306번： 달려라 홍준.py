#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1306                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1306                          #+#        #+#      #+#     #
#     Solved: 2024-09-06 04:47:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


N,M = map(int, input().split())
A = list(map(int, input().split()))

TREE = [0] * (4*N)
def init(idx, s, e):
    if s==e:
        TREE[idx] = A[s]
        return TREE[idx]
    mid = (s+e)//2
    l,r = init(idx*2, s,mid), init(idx*2+1,mid+1,e)
    TREE[idx] = max(l,r)
    return TREE[idx]

def get(idx, s,e):
    if e<frm or to<s:
        return 0 
    if frm<=s and e<=to:
        return TREE[idx]
    mid = (s+e)//2
    l,r = get(idx*2,s,mid), get(idx*2+1,mid+1,e)
    return max(l,r)


init(1,0,N-1)
ans = []
for i in range(M-1,N-M+1):
    frm,to = i-M+1, i+M-1
    ans.append(get(1,0,N-1))
print(*ans)
