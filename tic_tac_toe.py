
#? tic tac toe - python, define board, define check_win and do the game itself - compare to C - post to Git
import time
def check_win(field):
### function to check win on either side 
    if field[1] == field[2] == field[3]:
        return 1
    elif field[4] == field[5] == field[6]:
        return 1
    elif field[7] == field[8] == field[9]:
        return 1
    elif field[1] == field[4] == field[7]:
        return 1
    elif field[2] == field[5] == field[8]:
        return 1
    elif field[3] == field[6] == field[9]:
        return 1
    elif field[1] == field[5] == field[9]:
        return 1
    elif field[3] == field[5] == field[7]:
        return 1
    elif (field[1] != '1' and field[2] != '2' and field[3] != '3' 
          and field[4] != '4' and field[5] != '5' and field[6] != '6'
          and field[7] != '7' and field[8] != '8' and field[9] != '9'):
          return 0
    else:
        return -1

def board(field):
### function to print the board after every change 

    print("\n\t TICTACTOE THE GAME")
    print("\n")
    print("   Player 01: X and Player 02: O")
    print("\n")
    print("\t___________________\n")
    print("\t|     |     |     |\n")
    print("\t|  "+field[1]+"  |  "+field[2]+"  |  "+field[3]+"  |\n")
    print("\t|_____|_____|_____|\n")
    print("\t|     |     |     |\n")
    print("\t|  "+field[4]+"  |  "+field[5]+"  |  "+field[6]+"  |\n")
    print("\t|_____|_____|_____|\n")
    print("\t|     |     |     |\n")
    print("\t|  "+field[7]+"  |  "+field[8]+"  |  "+field[9]+"  |\n")
    print("\t|_____|_____|_____|\n")


# Needs to start with zero for better orientation - that way the field is easier to read in program
field = ['0','1','2','3','4','5','6','7','8','9']
field2 = ['0','1','2','3','4','5','6','7','8','9']
player = 1; count = 0
mark01 = 'X' ;mark02 = 'O'
board(field)
# main body maximum is nine moves so it is under ten unless the checkwin condition is met 
while count < 9:

    if player == 1:
        mark = mark01
    elif player == 2:
        mark = mark02
    else:
        break

    print("Player "+str(player)+" choose your move: ")
    move = int(input())
    if field[move] == field2[move]:
        field[move] = mark
    else:
        print("Invalid move!")
    
    board(field)
    check = check_win(field)
    print(check)
    if check == 1:
        time.sleep(5)
        print("Congratulation player "+str(player)+" has won!!")
        break
    elif check == 0:
        time.sleep(5)
        print("Draw! Yeeeeii.....")
    elif check == -1:
        count = count + 1
        if player == 1:
            player = 2
        else:
            player = 1
