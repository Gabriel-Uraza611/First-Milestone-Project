from tabulate import tabulate

def start(matrix, players, turn):

    table = [matrix[i:i+3] for i in range(0, 9, 3)] 
    print(tabulate(table, tablefmt="fancy_grid"))

    position = input(f"player {turn + 1} select the position you want to play: ")

    while(True):

        if position in '123456789':
            position = input("Please, enter a valid value:")
            continue

        if int(position) not in range(1, 10):
            position = input("Please, enter a valid value:")
            continue

        if int(position) not in matrix:
            position = input("That position has been already played, please try anotherone:  ")
            continue

        break

    return replacer(matrix, players, turn,  int(position))

def replacer(matrix, players, turn, position):
    
    replace = matrix.index(position)
    matrix[replace] = players[turn]

    if turn == 0:
        return analisis(matrix, players, turn=1)
    else:
        return analisis(matrix, players, turn=0)
    
def analisis(matrix, players, turn):

    full = True

    for elem in matrix:
        if elem in range(1,10):
            full = False

    if full == True:
        return print("all position has been played, GG")
    else:
        return start(matrix, players, turn)

def main():
    print(" \n ______Welcome to tic tac toe______ \n")

    figure = input("Player 1: Do you want to be X or O?: ").upper()

    while(figure not in  'XO'):
        figure = input("Please select X or O: ").upper()

    if figure == 'O':
        players = {0 : 'O', 1 : 'X'}
    else:
        players = {0 : 'X', 1 : 'O'}
    
    turn = 0
    matrix = [7,8,9,4,5,6,1,2,3]
        
    return analisis(matrix, players, turn)

if __name__ == '__main__':
    main()
