#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13458                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13458                         #+#        #+#      #+#     #
#     Solved: 2024-02-08 14:23:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input().strip())
A=list(map(int, input().split()))
B,C=map(int,input().split())
def find(Ai):
    # 총감독만으로 전부 가능한 경우 
    # 총감독은 반드시 있어야 함 
    if Ai >= B:
        return (Ai - B) // C + 2  if (Ai - B) % C else (Ai - B) // C + 1 
    else:
        return 1
 
print(sum([ find(ai) for ai in A]))