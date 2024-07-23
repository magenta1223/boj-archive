#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 21479                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/21479                         #+#        #+#      #+#     #
#     Solved: 2024-07-23 10:35:58 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# # 여러 줄의 입력을 받기 위해 sys.stdin.read()를 사용
input = open(0).readline 
A = []
while True:
    x = input().strip()
    if x:A.append(x)
    else:break 
print(int("".join(sorted(A, key=lambda x:x*101)[::-1])))



