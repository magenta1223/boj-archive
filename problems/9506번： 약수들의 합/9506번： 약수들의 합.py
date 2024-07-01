#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9506                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9506                          #+#        #+#      #+#     #
#     Solved: 2023-10-17 16:52:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def check_perfect(N):
    cs= []
    for i in range(1, N):
        if N % i == 0:
            cs.append(i)
        if sum(cs) > N:
            break
 
    if sum(cs) == N:
        print(f"{N} = {' + '.join([str(c) for c in cs])}")
    else:
        print(f"{N} is NOT perfect.")
                
while True:
    N = int(input())
    if N == -1:
        break 
    else:
        check_perfect(N)