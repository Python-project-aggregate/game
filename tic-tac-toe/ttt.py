import os

mat = {
    '1':'.', '2':'.', '3':'.',
    '4':'.', '5':'.', '6':'.',
    '7':'.', '8':'.', '9':'.'
}
#判断是否满足条件
# def winer():
#     if mat[1]==mat[2]==mat[3]:
#         return True
#     if mat[1]==mat[2]==mat[3]:
#         return True
#     if mat[1]==mat[2]==mat[3]:
#         return True
#     if mat[1]==mat[2]==mat[3]:




def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def test_win():

def main():
    begin = True
    while begin:
        begin = False
        turn = 'x'
        counter = 0
        print_board(mat)
        while counter < 9:
            move = input('轮到{}走棋, 请输入位置:'.format(turn))
            mat[move] = turn
            print_board(mat)
            if turn == 'x':
                turn ='o'
            else:
                turn = 'x'
            os.system('cls')

if __name__ == '__main__':
    main()