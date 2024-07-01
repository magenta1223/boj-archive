#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2448                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2448                          #+#        #+#      #+#     #
#     Solved: 2024-04-02 16:28:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
MAXK = 1
while N > 3*(2**MAXK):
    MAXK+= 1 
def draw(i):
    if i == 1:
        return "*"
    elif i == 2:
        return "* *"
    k = MAXK
    while i < 3*(2**k):
        k -= 1
    phase = 3*(2**k)
    
    if i == phase:
        full = ["*"] * (2*i-1)
        for j in range(5,2*i-1, 6):
            full[j] = " "
        return "".join(full)
    else:
        sub = draw(i - phase)
        return sub + (phase*4-2*i+1) * " " + sub
 
WIDTH = 2*N-1
for i in range(1,N+1):
    margin = " " * (N-i)
    print(margin + draw(i) + margin)