import random

# Name: Gal Arad
# description: The agent will check if there is an empty spot in it's row.
#              If there is, it will check if the dirty spot is from the left or right of it
#              and will move accordingly to this. If there is no dirty spot = means the whole row is clear,
#              it will move down to the next row.
#              The agent's behavior is rational because if there is a clean row it will just keep moving forward (down)
#              It can also "locate" the dirty spots.

class RobotVacuumAgent:

    def __init__(self,filename):
        """
        init function establishes board, robotRow, robotCol
        :param filename: establishes board
        """
        with open(filename, "r") as file:
            self.board = [[x for x in line.split()] for line in file]

        self.num_spaces = 0 # number of potential clean/dirty spaces in board

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.num_spaces += 1
                if self.board[r][c] == '@' or self.board[r][c] == '!': # find the location of the robot
                    self.robotRow = r;
                    self.robotCol = c;


    def print(self):
        """
        displays board to console
        """
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                print(self.board[r][c], end = ' ')
            print()


    def do_something(self):
        """
        TODO: Implement this funtion with more intelligence
        Loops are not allowed
        can suck up dirt or move robot
        """
       
        if self.board[self.robotRow][self.robotCol] == '!':
            self.board[self.robotRow][self.robotCol] = '@'; #just sucked up the dirt
            
          
        else:
            if "*" in self.board[self.robotRow]: # cheking if there is a dirty spot in the the current row
                if self.board[self.robotRow].index("*") > self.robotCol: # if so, checking if its from the left or right and moving accordingly.
                    self.move_right()
                else:
                    self.move_left()
            else:
                if self.out_of_bounds(self.robotRow +1, self.robotCol) == True:  #In a case there is a hole in the row under, it checks wheter
                    if self.out_of_bounds(self.robotRow , self.robotCol +1) == False: # is should moves to the left or right and then go down.
                        self.move_left()
                    else:
                        self.move_right()
                    
                else:
                    self.move_down()
            
        
    def out_of_bounds(self, row, col):
        """
        :param row:
        :param col:
        :return: True if (row,col) will be out of bounds of self.board
                otherwise, returns False
        """
        try:
            if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[row]):
                return True
            else:
                return False
        except:
            print('exception occurred -- out of bounds')
            return True


    def move_up(self):
        """
        moves robot 1 space up (north)
        :return:
        """
        if not self.out_of_bounds(self.robotRow -1, self.robotCol):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotRow -= 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'

    def move_down(self):
        """
        moves robot 1 space down (south)
        """
        if not self.out_of_bounds(self.robotRow+1, self.robotCol):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotRow += 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'


    def move_left(self):
        """
        moves robot 1 space left (west)
        """
        if not self.out_of_bounds(self.robotRow, self.robotCol-1):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotCol -= 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'


    def move_right(self):
        """
         moves robot 1 space right (east)
         """
        if not self.out_of_bounds(self.robotRow, self.robotCol+1):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotCol += 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'


    def utility(self):
        """
        :return: the number of clean spots in the room
        """
        result = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == '.' or self.board[r][c] == '@':
                    result += 1
        return result

    def is_goal(self):
        """
        :return: True if all of the spaces are clean; otherwise, False
        """
        if self.utility() == self.num_spaces:
            return True
        else:
            return False


if __name__ == '__main__':
    # create agent
    agent = RobotVacuumAgent("room2.txt")

    count = 0; # number of time steps

    # run the vacuum until room is clean
    while not agent.is_goal():
        print(count)
        agent.print()

        count += 1
        agent.do_something()

    # final state
    print(count)
    agent.print()