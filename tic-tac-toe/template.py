n=3
mat=[['.']*n for i in range(n)]

win_list=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

#主函数：通过调用get_move，让两位玩家X和O交替落子
def main():
    r=c=0
    num_moves = 0
    print_mat()
    print('Move are r,c,or "0" to exit')
    exit_flag = False
    while not exit_flag:
        num_moves += 1
        if num_moves > 9:
            print('No more space left.')
            break
        if num_moves % 2>0:
            cell_n=r*3+c+1
            r,c=get_comp_move(num_moves,cell_n)
            mat[r][c]='X'
            print('\nOkay,my move...\n')
            print_mat()
            if test_win(r,c):
                print('\nX WIN THE GAME!')
                break
            else:
                exit_flag,r,c=get_move('O')
                if (not exit_flag) and test_win(r,c):
                    print('\nO WIN THE GAME!')
                    break

#获得落子位置的函数，不断让X和O落子
#并以行，列的方式指定落子的位置
#然后将这个子加入棋盘并打印棋盘
def get_move(player):
    while True:
        prompt='Enter move for ' + player + ':'
        s=input(prompt)
        a_list=s.split(',')
        if len(a_list)>=1 and int(a_list[0])==0:
            print('Bye now.')
            return True,0,0
        elif len(a_list)<2:
            print('Use row,col.Re-enter')
        else:
            r=int(a_list[0])-1
            c=int(a_list[1])-1
            if r<0 or r>=n or c<0 or c>=n:
                print('Out of range,Re-enter')
            elif mat[r][c]!='.':
                print('Occupied,re-enter')
            else:
                mat[r][c]=player
                print_mat()
                break
    return False,r,c

#输出棋盘
def print_mat():
    s='  1 2 3\n'
    for i in range(n):
        s+=str(i+1)+' '
        for j in range(n):
            s+=str(mat[i][j])+' '
        s+='\n'
    print(s)

#判断当前玩家是否获得胜利
#这个函数检查所有my_win_list的组合
#只要有一个组合包含3个X或者3个O，就返回True
def test_win(r,c):
    cell_n=r*3+c+1
    my_win_list=[ttt_list for ttt_list in win_list if cell_n in ttt_list]
    for ttt_list in my_win_list:
        num_x,nums_o,num_blanks=test_way(ttt_list)
        if num_x==3 or nums_o==3:
            return True
    return False

def test_way(ttt_list):
    letters_list=[]
    for cell_n in ttt_list:
        r=(cell_n-1)//3
        c=(cell_n-1)%3
        letters_list.append(mat[r][c])
    num_x=letters_list.count('X')
    nums_o=letters_list.count('0')
    nums_blanks=letters_list.count('.')
    return num_x,nums_o,nums_blanks

#确定计算机下一步要走的地方
#对于棋盘
def get_comp_move(num_moves,opp_cell):

    #如果这是第3步，且对手第2步下在边上，就下在中央
    if num_moves==3 and opp_cell in [2,4,6,8]:
        return 1,1

    #生成一个包含所有空单元格的列表
    cell_list=[(i,j) for j in range(n)
               for i in range(n) if mat[i][j]=='.']

    #检查每个单元格，看它能否让我方立即获胜
    for cell in cell_list:
        if test_to_win(cell[0],cell[1]):
            return cell[0],cell[1]

    #检查每个单元格，看它能否让敌方立即获胜
    for cell in cell_list:
        if test_to_block(cell[0],cell[1]):
            return cell[0],cell[1]

    #检查每个单元格，看它能否成双二
    for cell in cell_list:
        if test_db1_threat(cell[0],cell[1]):
            return cell[0],cell[1]

    #棋子落子的优先队列
    prefix=[1,9,3,7,5,2,4,6,8]
    for i in prefix:
        r=(i-1)//3
        c=(i-1)%3
        if mat[r][c]=='.':
            return r,c

#检查能否获胜：检查包含当前单元格的每个获胜组合
#如果其中包含两个X，就能立即获胜
def test_to_win(r,c):
    cell_n=r*3+c+1
    my_win_list=[ttt_list for ttt_list in win_list
                 if cell_n in ttt_list]
    for ttt_list in my_win_list:
        num_x,num_o,num_blanks=test_way(ttt_list)
        if num_x==2:
            print('Watch THIS:')
            return True
    return False

#检查能否对手获胜：检查包含当前单元格的每个获胜组合
#如果其中包含两个O，就能立即获胜
def test_to_block(r,c):
    cell_n=r*3+c+1
    my_win_list=[ttt_list for ttt_list in win_list
                 if cell_n in ttt_list]
    for ttt_list in my_win_list:
        num_x,num_o,num_blocks=test_way(ttt_list)
        if num_o==2:
            print('Ha ha,I am going to block you.')
            return True
    return False

#检查能否成双二：检查包含所有单元格的所有获胜组合
#如果有两个组合都有X，就能成双二
def test_db1_threat(r,c):
    threats=0
    cell_n=r*3+c+1
    my_win_list=[ttt_list for ttt_list in win_list
                 if cell_n in ttt_list]
    for ttt_list in my_win_list:
        num_x,num_0,num_blocks=test_way(ttt_list)
        if num_x==1 and num_blocks==2:
            threats+=1
        if threats>=2:
            print('I hava you now!')
            return True
    return False

# main()
print_mat()