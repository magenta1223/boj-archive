#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7682                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7682                          #+#        #+#      #+#     #
#     Solved: 2024-03-13 16:33:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solve(st, st_flip):
    # 최종상태인지 = 승부가 나거나, 무승부 상태로 꽉 차거나 
    # 1. X 승리 -> cnt가 o보다 1많음. o 틱택토가 없음. 
    # 2. O 승리 -> cnt가 x와 같음. x 틱택토가 없음.
    # 3. 무승부 -> cnt['x']가 o보다 1많음. 틱택토가 둘다 없음 
        
    # 1. 이긴 사람을 확인 -> 1명인지
    # 2. 이긴사람이 없다면, 꽉 찼는지 
    def winner(st, p):
        p*=3
        checks = [st[0:3], st[3:6], st[6:], st[0]+st[4]+st[8], st[2]+st[4]+st[6]]
        if any([ c == p for c in checks]):
            return True 
        else:
            return False 
 
    xwin = winner(st, "X") or winner(st_flip, "X")
    owin = winner(st, "O") or winner(st_flip, "O")
    
    if xwin and cnt['X']==cnt['O']+1 and not owin:
        return "valid"
    if owin and cnt['X'] == cnt['O'] and not xwin:
        return "valid"
    if not xwin and not owin and cnt['X']==5 and cnt['O'] == 4:
        return "valid"
    return "invalid"
 
 
while True:
    st = input().strip()
    if st == 'end':
        break 
    # cnt_x = B.count("X")
    # cnt_o = B.count("O")
    cnt = {"X" : 0, "O": 0, '.' : 0}
    st_flip = st[::3] + st[1::3] + st[2::3]
    for i in range(9):
        cnt[st[i]] += 1 
    
    print(solve(st, st_flip))