n = 3
mat = [['.' * n for i in range(n)]]
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
                print()