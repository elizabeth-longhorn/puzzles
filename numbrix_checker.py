"""
File:        numbrix_checker.py
Description: Given a CSV file filled with a proposed solution for Numbrix,
             ensure it is a valid solution. The file should be filled such
             that there is a continuous chain of numbers between the start
             number, 1, and ending number, 81. 1 can be found in any cell
             of the grid and the chain can be continued by a combination of
             horizontal and vertical moves.
"""

import csv

def parse():
    #Parse CSV file
    with open("soln.csv", newline='') as csvfile:
        solnreader = csv.reader(csvfile)
        soln = [[int(item) for item in row] for row in solnreader]
    return(soln)

def checker(soln):
    #Look for 1
    search = 1
    for i in range(0,8):
        for j in range(0,8):
            if soln[i][j] == search:
                search += 1
                row = i 
                col = j
                break
    
    #Didn't find 1
    if search == 1:
        return False
   
    #Continue searching for the rest of the numbers
    while(search <= 81):
        if row > 0 and soln[row-1][col] == search:
            row -= 1
        elif row < 8 and soln[row+1][col] == search:
            row += 1
        elif col > 0 and  soln[row][col-1] == search:
            col -= 1
        elif col < 8 and soln[row][col+1] == search:
            col += 1
        else:
            return False
        search += 1

    #Solution is correct if reached here 
    return True

if __name__ == '__main__':
    solution = parse()
    if checker(solution) is True:
        print("Great job! This is the correct solution!")
    else:
        print("Try again. Incorrect attempt.")

                  