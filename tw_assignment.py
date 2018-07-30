import sys
import numpy as np

def check(command):     #错误检查
    l = command.split('\n')

    first = l[0]
    list_f = first.split(' ')
    if(len(list_f) != 2):   #第一行拆分后数量不等于2
        print('Incorrect command format.')   #格式错误
        sys.exit()
    for i in range(0, 2):
        if(not list_f[i].isdigit()):   #不是数字
            print('Invalid number format')   #无效的数字
            sys.exit()
        if(int(list_f[i]) <= 0):       #数字<=0
            print('Number out of range.')    #数字超出预定范围
            sys.exit()
    rows = int(list_f[0])
    columns = int(list_f[1])

    second = l[1]
    list_s = second.split(';')
    cell_coor = []
    for i in range(0, len(list_s)):      #按;拆分
        connect_cell = list_s[i].split(' ')       #按空格拆分
        if(len(connect_cell) != 2):    #拆分后长度不为2
            print('Incorrect command format.')
            sys.exit()

        array_cell = []      #以3维list形式保存所有连通cell的坐标对
        for j in range(0, 2):
            cell = connect_cell[j]        #节点j

            list_cell = cell.split(',')  #按,拆分

            if(len(list_cell) != 2):
                print('Incorrect command format.')
                sys.exit()
            for k in range(0, 2):
                if(not list_cell[k].isdigit()):
                    print('Invalid number format')   #无效的数字
                    sys.exit()
                list_cell[k] = int(list_cell[k])
            if(list_cell[0] < 0 or list_cell[0] > rows - 1):
                print('Number out of range​.')
                sys.exit()
            if(list_cell[1] < 0 or list_cell[1] > columns - 1):
                print('Number out of range​.')
                sys.exit()
            array_cell.append(list_cell)    #cell保存到数组中

        if(abs(array_cell[1][0] - array_cell[0][0]) + abs(array_cell[1][1] - array_cell[0][1]) > 1):
            print('Maze format error.')       #连通性错误
            sys.exit()
        cell_coor.append(array_cell)

    return rows, columns, cell_coor

def render(rows, columns, cell_coor):
    out_instruction = np.zeros((2 * rows + 1, 2 * columns + 1))
    for row in range(0, rows):
        for column in range(0, columns):
            out_instruction[2 * row + 1][2 * column + 1] = 1

    for i in range(0, len(cell_coor)):
        cell_pair = cell_coor[i]       #取出一个连通cell对
        cell = np.zeros(2).astype(int)      #保存连通中间点的坐标
        if(cell_pair[0][0] == cell_pair[1][0]):
            cell[0] = cell_pair[0][0] * 2 + 1
            cell[1] = (cell_pair[0][1] * 2 + 1 + cell_pair[1][1] * 2 + 1) / 2
        else:
            cell[1] = cell_pair[0][1] * 2 + 1
            cell[0] = (cell_pair[0][0] * 2 + 1 + cell_pair[1][0] * 2 + 1) / 2
        out_instruction[cell[0]][cell[1]] = 1

    out_string = ''
    for i in range(0, 2 * rows + 1):
        for j in range(0, 2 * columns + 1):
            if(out_instruction[i][j] == 0):
                out_string += '[W]'
            else:
                out_string += '[R]'
            if(j == 2 * columns):
                out_string += '\n'
            else:
                out_string += ' '

    return out_string

command = input() + '\n' + input()
rows, columns, cell_coor = check(command)
maze_text = render(rows, columns, cell_coor)

print(maze_text)




















