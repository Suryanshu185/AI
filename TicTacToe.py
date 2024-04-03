import random

board = [' ' for _ in range(10)]

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('NEXT BOARD AHEAD')

def isWinner(b, l):
    return (
        (b[1] == l and b[2] == l and b[3] == l) or
        (b[4] == l and b[5] == l and b[6] == l) or
        (b[7] == l and b[8] == l and b[9] == l) or
        (b[1] == l and b[4] == l and b[7] == l) or
        (b[3] == l and b[6] == l and b[9] == l) or
        (b[2] == l and b[5] == l and b[8] == l) or
        (b[1] == l and b[5] == l and b[9] == l) or
        (b[3] == l and b[5] == l and b[7] == l)
    )

def spaceIsFree(pos):
    return board[pos] == ' ' 
def insertLetter(letter, pos):
    board[pos] = letter

def playerMove(symbol):
    if symbol == 'X':
        move = input(f"Player X, please select a position to enter the X between 1 to 9: ")
        try:
            move = int(move)
            if 1 <= move <= 9 and spaceIsFree(move):
                insertLetter(symbol, move)
            else:
                print('Invalid move. Try again.')
                playerMove(symbol)
        except ValueError:
            print('Please type a number.')
            playerMove(symbol)
    else:
        # Simple AI - makes a random move
        move = random.randint(1, 9)
        while not spaceIsFree(move):
            move = random.randint(1, 9)
        insertLetter(symbol, move)

def boardFull():
    return ' ' not in board[1:]

# Main game loop
def playTicTacToe():
    while True:
        printBoard(board)

        # Player X move
        playerMove('X')

        # Check for a winner
        if isWinner(board, 'X'):
            printBoard(board)
            print('Player X wins!')
            break

        # Check for a tie
        if boardFull():
            printBoard(board)
            print('It\'s a tie!')
            break

        printBoard(board)

        # Player O move (AI)
        playerMove('O')

        # Check for a winner
        if isWinner(board, 'O'):
            printBoard(board)
            print('Player O (AI) wins!')
            break

        # Check for a tie
        if boardFull():
            printBoard(board)
            print('It\'s a tie!')
            break

if __name__ == "_main_":
    playTicTacToe()