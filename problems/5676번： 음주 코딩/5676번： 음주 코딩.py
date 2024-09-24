#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5676                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5676                          #+#        #+#      #+#     #
#     Solved: 2024-09-24 06:19:40 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 

def init(idx, s, e):
    if s==e:
        TREE[idx] = X[s]
        return TREE[idx]
    mid = (s+e)//2 
    l,r = init(idx*2, s,mid), init(idx*2+1, mid+1,e)
    TREE[idx] = l*r
    return TREE[idx]

def update(idx, s, e):
    # target을 포함하는가? 
    if not s<=target<=e:
        return TREE[idx]
    
    if s==e:
        TREE[idx] = V 
        return TREE[idx]
    mid = (s+e)//2 
    l,r = update(idx*2, s,mid), update(idx*2+1, mid+1,e)
    TREE[idx] = l*r
    return TREE[idx]

def get(idx, s ,e):
    if to < s or e < frm:
        return 1 
    if frm<=s and e<=to:
        return TREE[idx]

    mid = (s+e)//2 
    l,r = get(idx*2, s,mid), get(idx*2+1, mid+1,e)
    return l*r

def parse(v):
    return '+' if v>0 else ('-' if v<0 else '0')

while True:
    try:
        N,K = map(int, input().split())
        X = list(map(int, input().split()))
        X = [1 if x>0 else (-1 if x<0 else 0) for x in X]
        TREE = [0] * (4*N)
        init(1,0,N-1)
        ans = ''
        for _ in range(K):
            cmd,a,b = input().split()

            if cmd == "C":
                target,V = int(a)-1, int(b)
                V = 1 if V>0 else (-1 if V<0 else 0)
                update(1,0,N-1)
            else:
                frm,to = int(a)-1, int(b)-1
                ans += parse(get(1,0,N-1))
        print(ans)
    except Exception:
        break 
