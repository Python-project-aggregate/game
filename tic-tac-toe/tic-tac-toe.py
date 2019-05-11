
import os
n = 3
mat = [['.']*n for i in range(n)]
print(mat)
# 判断输出错误情况,对用户进行提示
def get_move(player):
    while True:
        prompt = 'Enter move for '+ player + ':'
        s = input(prompt)
        a_list = s.split(',')
        if len(a_list) >= 1 and int(a_list[0]) == 0:
            print('Bye now.')
        elif len(a_list)< 2:
            print('Use row, col.re-enter')
        else:
            r = int(a_list[0])-1
            c = int(a_list[1])-1
            if r <0 or r>= n or c< 0 or c>=n:
                print('out of range')
            elif mat[r][c] !='.':
                print('occupied')
            else:
                mat[r][c] = player
                print_mat()
                break
    return False, r, c
# 输出棋盘
def print_mat():
    s = '  1 2 3\n'
    for i in range(n):
        s += str(i+1)+' '
        for j in range(n):
            s += str(mat[i][j])+' '
        s += '\n'
    print(s)
# 定义主函数 :通过调用get_move, 让两位玩家x和o交替落子
# def main():
#     r = c = 0
#     num_moves = 0
#     os.system('cls')
#     print_mat()
#     print('移动 r,c 输入0 结束')
#     exit_flag = False
#     while not exit_flag:
#         num_moves += 1
#         if num_moves > 9:
#             print('没有空间')
#             break
#         if num_moves % 2 > 0:
#             cell_n = r * 3 + c + 1
#             r, c =
def main():
    begin = True
    while begin:
        player = input(">>")
        get_move(player)
        if

if __name__ == '__main__':
    main()