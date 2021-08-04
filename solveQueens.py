# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/n-queens/

def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    def generateBoard():
        """
        生成可打印的棋盘
        :type
        :rtype: List[str]
        """
        board = []
        for i in range(n):
            row[queens[i]] = 'Q'
            board.append("".join(row))
            row[queens[i]] = '.'
        return board


    def backtrack(row:int):
        """
        按行生成棋盘（因为每行只能有一个皇后）
        :type row:int
        :rtype
        """
        if row == n:
            board = generateBoard()
            solutions.append(board)
        else:
            for i in range(n):
                if i in columns or row-i in diagona1 or row+i in diagona2:
                    continue
                queens[row] = i
                columns.add(i)
                diagona1.add(row-i)
                diagona2.add(row+i)
                backtrack(row+1)
                columns.remove(i)
                diagona1.remove(row-i)
                diagona2.remove(row+i)


    # 记录所有摆放的可能
    solutions = list()
    # 记录每行摆放的位置
    queens = [-1]*n
    # 记录哪些列已经摆放了皇后
    columns = set()
    # 记录↘的斜线方向, 同一方向的 row-i 相同
    diagona1 = set()
    # 记录↙的斜线方向，同一方向的 row+i 相同
    diagona2 = set()
    # 打印的行
    row = ["."]*n
    backtrack(0)
    return solutions

print(solveNQueens(4))
