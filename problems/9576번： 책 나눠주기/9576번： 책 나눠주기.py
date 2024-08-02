#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9576                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9576                          #+#        #+#      #+#     #
#     Solved: 2024-08-02 09:52:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 책번호는 1~N 
# 사람은 M명. 각각 a이상 b이하의 책 중에서 하나를 준다. 
# 최대한 많은 사람에서 책을 주자. 

# 1. 원하는 범위를 array로 만들고 
# 2. b,a 를 기준으로 정렬. 
# 3. 이번 사람은 범위의 끝이 같은 사람들 중에는 시작이 가장 작음. -> 줄 수 있는 가장 작은 책을 주면 된다 

input = open(0).readline 

for _ in range(int(input())):
    N,M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)] 
    A.sort(key= lambda x: (x[1], x[0]))
    
    BOOKS = [1] * (N+1)
    ans = 0 

    # 최대 M**2
    for i in range(M):
        a,b = A[i]
        for idx in range(a,b+1):
            if BOOKS[idx]:
                BOOKS[idx]-=1 
                ans += 1 
                break 
    print(ans)
    