#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3687                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3687                          #+#        #+#      #+#     #
#     Solved: 2024-05-13 09:26:55 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n_stick = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
 
def find_max(n):
    max_num = ""
    while n > 3:
        n -= 2
        max_num = "1" + max_num
    return ("7" if n==3 else "1") + max_num
 
def find_min(n):
    min_num = ""
    while n > 17:
        n -= 7
        min_num = "8" + min_num 
    ans = "" 
    def recur(n,s,min_num):
        nonlocal ans 
        for i in range(s,10):
            tmp = min_num + str(i)
            if n==n_stick[i]:
                if not ans:
                    ans = tmp 
                elif int(ans) > int(tmp):
                    ans = tmp 
            elif n > n_stick[i] + 1:
                recur(n-n_stick[i], 0, tmp)
    recur(n,1, "")
    return ans+min_num
 
for _ in range(int(input())):
    N = int(input())
    print(find_min(N), find_max(N))