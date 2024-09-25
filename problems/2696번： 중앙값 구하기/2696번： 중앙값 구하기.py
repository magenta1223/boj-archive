#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2696                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2696                          #+#        #+#      #+#     #
#     Solved: 2024-09-25 05:58:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from heapq import heappop, heappush 

for _ in range(int(input())):
    M = int(input())
    nrow, r = divmod(M, 10)
    A = []
    for _ in range(nrow+1 if r else nrow):
        A += list(map(int, input().split()))
    
    ans = []
    left, right = [], []
    for i in range(M):
        if not left or len(left) <= len(right):
            heappush(left, -A[i])
        elif not right or len(left) > len(right):
            heappush(right, A[i])
        # 교환 
        while left and right and -left[0] > right[0]:
            l = -heappop(left)
            r = heappop(right)
            heappush(left, -r)
            heappush(right, l)
        if not i%2:
            median = -left[0] if len(left) > len(right) else right[0]
            ans.append(median)

    print(len(ans))
    nrow, r = divmod(len(ans), 10)
    for i in range(nrow+1 if r else nrow):
        print(*ans[i*10:i*10+10])