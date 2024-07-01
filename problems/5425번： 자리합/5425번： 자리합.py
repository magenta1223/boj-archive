#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5425                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5425                          #+#        #+#      #+#     #
#     Solved: 2024-05-21 10:23:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solve(n):
    if n < 0:
        return [0] * 10  
 
    str_n = str(n)
    w = 1
    counts = [0] * 10  
 
    while str_n:
        if n < 10: # 한자리 수 
            for i in range(1,n+1):
                counts[i] += w
            break 
 
        # 최소 2자리 수. 마지막 자리를 9로 만든다. 
        while str_n[-1] != "9":
            for s in str_n:
                counts[int(s)] += w 
            n -= 1 
            str_n = str(n)
 
        if n < 10:
            for i in range(1,n+1):
                counts[i] += w
            break 
        else:
            str_n = str_n[:-1]
            n = int(str_n)
            for i in range(10):
                counts[i] += w*(n+1) 
            # counts[0] -= w # 추가로 카운트된 0의 값을 제거. 이 문제는 0이 합에 계산이 안되어 필요가 없음.  
            w *= 10
    return counts
 
 
for _ in range(int(input())):
    a,b = map(int,input().split())
    counts_a, counts_b = solve(a-1), solve(b)
 
    ans = 0
    for i in range(10):
        ans += counts_b[i] * i
    for i in range(10):
        ans -= counts_a[i] * i
    print(ans)