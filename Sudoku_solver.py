# Python program to solve a sudoku puzzle by Raj Pratap Singh

import os
def solve(board):
    find=find_empty(board)
    if not find:
        return True
    else:
        row,col=find
    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col]=i
            if solve(board):
                return True
            board[row][col]=0
    return False
def valid(board,num,pos):
    #check for row
    for i in range(9):
        if board[pos[0]][i]==num and pos[1]!=i:
            return False
    #check for column
    for i in range(9):
        if board[i][pos[1]]==num and pos[0]!=i:
            return False
    #check for box
    box_x=pos[1]//3
    box_y=pos[0]//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if board[i][j]==num and (i,j)!=pos:
                return False
    return True
def print_sudoku(board):
    for i in range(9):
        if i==3 or i==6:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j==3 or j==6:
                print("|",end=" ")
            print(board[i][j],end=" ")
        print()
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)
    return None
if __name__=="__main__":
    os.system('cmd /c "color a"')
    print("  ==>   Sudoku Solver   <==")
    print("     --------------------")
    print("Enter the sudoku row by row and")
    print("separate each element in a row by space")
    print("and at the blank spaces enter 0")
    print("eg., 0 0 8 5 3 1 0 6 0 \n")
    sudoku=[]
    for i in range(9):
        temp=list(map(int,input().split()))
        sudoku.append(temp)
    solve(sudoku)
    print()
    print_sudoku(sudoku)
    print("Developed by Raj pratap singh")
