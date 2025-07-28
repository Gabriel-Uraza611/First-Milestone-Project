from tabulate import tabulate
from time import sleep

def start(matrix, players, turn):
    sleep(1)
    table = [matrix[i : i + 3] for i in range(0, 9, 3)] 
    print(tabulate(table, tablefmt="fancy_grid"))

    position = input(f"player {turn} select the position you want to play: ")

    while(True):
        if position in '123456789':
            if int(position) not in range(1, 10):
                position = input("Please, enter a valid value:")
            else:
                if int(position) not in matrix:
                    position = input("That position has been already played, please try anotherone:  ")
                else:
                    break
        else:
            position = input("Please, enter a valid value: ")

    return replacer(matrix, players, turn,  int(position))

def replacer(matrix, players, turn, position):
    
    replace = matrix.index(position)
    matrix[replace] = players[turn]
    analisis(matrix, players, turn)
    
def analisis(matrix, players, turn):
    full = True
    for elem in matrix:
        if elem in range(1,10):
            full = False

    if full == True:
        print("TIE!, GG")
        return retry()
    else:
        win = {
            1 : str(matrix[0]) + str(matrix[3]) + str(matrix[6]),
            2 : str(matrix[1]) + str(matrix[4]) + str(matrix[7]),
            3 : str(matrix[2]) + str(matrix[5]) + str(matrix[8]),
            4 : str(matrix[0]) + str(matrix[1]) + str(matrix[2]),
            5 : str(matrix[3]) + str(matrix[4]) + str(matrix[5]),
            6 : str(matrix[6]) + str(matrix[7]) + str(matrix[8]),
            7 : str(matrix[0]) + str(matrix[4]) + str(matrix[8]),
            8 : str(matrix[2]) + str(matrix[4]) + str(matrix[6]),
        }

        for i in range(1, 9):
            if win[i] == 'XXX' or win[i] == 'OOO':
                sleep(1)
                print("****** HERE THE RESULTS ********")
                sleep(1)
                table = [matrix[i : i + 3] for i in range(0, 9, 3)] 
                print(tabulate(table, tablefmt="fancy_grid"))
                sleep(1)
                print(f"Congratulations, the winner has been the player {turn}")
                return retry()
                
        if turn == 1:
            return start(matrix, players, turn=2)
        else:
            return start(matrix, players, turn=1)
        

def retry():
    sleep(1)
    choice = input("Wanna play again?[Y/n]: ").lower()
    
    while(True):
        if choice == 'y':
            return main()
        elif choice == 'n':
            return print("Seeeee YAAAAAAAAAAA!")
        else:
            choice = input("Try again, [Y/n]?: ")
    
def main():
    print(" \n ______Welcome to tic tac toe______ \n")

    figure = input("Player 1: Do you want to be X or O?: ").upper()

    while(figure not in  'XO'):
        figure = input("Please select X or O: ").upper()

    if figure == 'O':
        players = {1 : 'O', 2 : 'X'}
    else:
        players = {1 : 'X', 2 : 'O'}
    
    turn = 2
    matrix = [7,8,9,4,5,6,1,2,3]

    return analisis(matrix, players, turn)

if __name__ == '__main__':
    main()
