#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3954                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3954                          #+#        #+#      #+#     #
#     Solved: 2024-09-24 06:39:24 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


"""
+-.,
qwe

포인터 숫자를 올리고 0 -> 1 
내리고 1 -> 0 
출력하고 0 
문자 하나를 읽어서 포인터에 저장
q를 0에 저장 
-> 끝 

포인터가 가리키는 수만 잘 저장하고 있다가~! 

+[+-]
1. +: 0 -> 1 
2. [: 1이므로 다음
3. +: 1->2 
4. -: 2->1
5. ]: 1이므로 [의 다음명령으로
6. +: 1->2 

-> 루프 

+++++[->++<]>[-<+++++++>]<[->+>+>+>+<<<<]>+++>--->++++++++++>---<<<.>.>.>.
1. +가끝나면 -> 5
2. - -> 4
3. >: 한칸 오른쪽. 1
4. ++: 3 
5. <: 다시 왼쪽. 4 
그러면 루프가 시작할 때 5, 다음 루프에서 4 -> 언젠가는 0이 되어 끝난다

뭐 이렇게 하면 된다는거지 


"""


input = open(0).readline 
import sys 


def find_loop(cmd):
    jump = {}
    brackets = []
    for i, c in enumerate(cmd):
        if c == '[':
            brackets.append(i)
        elif c == ']':
            to = brackets.pop()
            jump[i] = to
            jump[to] = i
    return jump


for _ in range(int(input())):
    M, C, I = map(int, input().split())
    cmd = input().strip()
    string = input().strip()

    array = [0] * M 
    array_ptr, cmd_ptr, string_ptr, cnt = 0, 0,0 ,0
    jump = find_loop(cmd)
    max_ptr = C
    maxexec = 50000000
    flag = False

    while cmd_ptr < C:
        c = cmd[cmd_ptr]

        if c == '+':
            array[array_ptr] = (array[array_ptr]+1)%256
        elif c == '-':
            array[array_ptr] = (array[array_ptr]-1)%256
        elif c == '<':
            array_ptr = (array_ptr-1)%M
        elif c == '>':
            array_ptr = (array_ptr+1)%M
        elif c == '[' and array[array_ptr] == 0:
                cmd_ptr = jump[cmd_ptr]
        elif c == ']' and array[array_ptr] != 0:
                cmd_ptr = jump[cmd_ptr]
        elif c == ',':
            if string_ptr < I:
                array[array_ptr] = ord(string[string_ptr])
                string_ptr+=1
            else:
                array[array_ptr] = 255


        if cnt > maxexec:
            max_ptr = min(max_ptr, cmd_ptr)

        cnt += 1 
        cmd_ptr += 1 

        if cnt > 2*maxexec:
            flag = True 
            sys.stdout.write('Loops {} {}\n'.format(max_ptr, jump[max_ptr]))
            break 

    if not flag:
        sys.stdout.write('Terminates\n')
    




import sys

def find_loop(cmd):
    jump = {}
    brackets = []
    for i, c in enumerate(cmd):
        if c == '[':
            brackets.append(i)
        elif c == ']':
            to = brackets.pop()
            jump[i] = to
            jump[to] = i
    return jump



input = open(0).readline 

for _ in range(int(input())):
    M, C, I = map(int, input().split())
    cmd = input().strip()
    string = input().strip()
    
    array = [0] * M 
    array_ptr, cmd_ptr, string_ptr, cnt = 0, 0,0 ,0
    jump = find_loop(cmd)
    max_ptr = C
    maxexec = 50000000
    flag = False

    while cmd_ptr < C:
        c = cmd[cmd_ptr]

        if c == '+':
            array[array_ptr] = (array[array_ptr]+1)%256
        elif c == '-':
            array[array_ptr] = (array[array_ptr]-1)%256
        elif c == '<':
            array_ptr = (array_ptr-1)%M
        elif c == '>':
            array_ptr = (array_ptr+1)%M
        elif c == '[' and array[array_ptr] == 0:
                cmd_ptr = jump[cmd_ptr]
        elif c == ']' and array[array_ptr] != 0:
                cmd_ptr = jump[cmd_ptr]
        elif c == ',':
            if string_ptr < I:
                array[array_ptr] = ord(string[string_ptr])
                string_ptr+=1
            else:
                array[array_ptr] = 255

        if cnt > maxexec:
            max_ptr = min(max_ptr, cmd_ptr)
        cmd_ptr+=1
        cnt+=1

        if cnt > 2*maxexec:
            flag = True
            sys.stdout.write('Loops {} {}\n'.format(max_ptr, jump[max_ptr]))
            break
    if not flag:
        sys.stdout.write('Terminates\n')