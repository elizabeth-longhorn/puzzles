"""
File:        sudoku_checker.py
Description: Given a CSV file filled with a proposed solution for Sudoku,
             ensure it is a valid solution. 
"""

import csv

def parse():
    #Parse CSV file
    with open("sudoku_soln.csv", newline='') as csvfile:
        solnreader = csv.reader(csvfile)
        soln = [[int(item) for item in row] for row in solnreader]
    return(soln)

def checker(soln):
    #Check rows
    for row in soln:
       set_row = set(row);
       if len(set_row) != 9:
           return False

    #Check columns
    for i in range(0,9):
        set_col = set()
        for j in range(0,9):
            set_col.add(soln[j][i])
        if len(set_col) != 9:
            return False

    #Check boxes
    start_row = 0
    start_col = 0
    set_box = set()
    slice_obj = slice(start_col, start_col+3)
    for i in range(0,3):
        for j in range(0,3):
            set_box.update((soln[start_row][slice_obj]))
            set_box.update((soln[start_row+1][slice_obj]))
            set_box.update((soln[start_row+2][slice_obj]))
            if len(set_box) != 9:
                return False 
            start_row += 3
            set_box = set()
        start_row = 0
        start_col += 3 
        slice_obj = slice(start_col, start_col+3) 
    return True

if __name__ == '__main__':
    solution = parse()
    if checker(solution) is True:
        print("Great job! This is the correct solution!")
    else:
        print("Try again. Incorrect attempt.")

                  