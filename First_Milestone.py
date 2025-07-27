from tabulate import tabulate


def start(matrix, players, turn):
    
    #* aqui se le pide a los jugadores que posicion quieren mover---------

    table = [matrix[i:i+3] for i in range(0, 9, 3)] #* table solo se usa para imprimir 
    print(tabulate(table, tablefmt="fancy_grid"))

    position = input(f"player {turn + 1} select the position you want to play: ")

    while(not position.isdigit() or int(position) not in matrix):
        full = True
        for elem in matrix:
            if elem in range(1,10):
                full = False
        
        if full == True:
            return print("all position has been played, GG")
        else:
            position = input("Please enter a valid value: ")

    tic_tac_toe(matrix, players, turn,  int(position))

def tic_tac_toe(matrix, players, turn, position):
    #* aqui solo se reasignan posiciones-----------
    
    if position in matrix :
        replace = matrix.index(position)
        matrix[replace] = players[turn]
    else:
        print("all position has been played")
        return analisis()

    if turn == 0:
        start(matrix, players, turn=1)
    else:
        start(matrix, players, turn=0)

def analisis():
    pass
    #* aqui se analisa la matriz y se da un veredicto segun el caso-----------------------

def main():
    print(" \n ______Welcome to tic tac toe______ \n")

    figure = input("Player 1: Do you want to be X or O?: ").upper()

    while(figure not in  'XO'):
        figure = input("Please select X or O: ")

    if figure == 'O':
        players = {0 : 'O', 1 : 'X'}
    else:
        players = {0 : 'X', 1 : 'O'}
    
    turn = 0
    matrix = [7,8,9,4,5,6,1,2,3]
        
    start(matrix, players, turn)

if __name__ == '__main__':
    main()