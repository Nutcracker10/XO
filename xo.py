theBoard = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9'};

def boardPrinter(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3']);
    print('-+-+-');
    print(board['4'] + '|' + board['5'] + '|' + board['6']);
    print('-+-+-');
    print(board['7'] + '|' + board['8'] + '|' + board['9']);

def rules():
    print('');
    print('The goal of this game is to get three of your letter in a line.');
    print('To make a move, enter the number of the position you want to place your letter.');
    print('This starts with 1 at the top left hand corner, and 9 at the bottom left.');
    print('For example, if you want to fill the middle space, that is 5. The middle right is 6.\n');

def winchecker(board, turn):
    #checking horizontals
    if(board['1'] == turn and board['2'] == turn and board['3'] == turn):
        return 1;

    elif(board['4'] == turn and board['5'] == turn and board['6'] == turn):
        return 1;

    elif(board['7'] == turn and board['8'] == turn and board['9'] == turn):
        return 1;

    #checking verticals
    elif(board['1'] == turn and board['4'] == turn and board['7']  == turn):
        return 1;

    elif(board['2'] == turn and board['5'] == turn and board['8'] == turn):
        return 1;

    elif(board['3'] == turn and board['6'] == turn and board['9'] == turn):
        return 1;

    #checks diagonals
    elif(board['1'] == turn and board['5'] == turn and board['9'] == turn):
        return 1;

    elif(board['3'] == turn and board['5'] == turn and board['7'] == turn):
        return 1;

    else:
        return 0;

def drawchecker(board):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
    counter = 0;

    for i in range (0,9):
        if (numbers[i] in theBoard.values()):
            counter = counter + 1;

    if (counter == 0):
        return 1;

    else:
        return 0;


print('Welcome to X\'s and O\'s!');
print('Player X enter your name: ');
playerX = input();

print('Player O enter your name: ');
playerO = input();

rules();#displays rules

turn = 'X';

while True:
    boardPrinter(theBoard);
    print('');
    #allows player X to make a move
    if(turn == 'X'):
        print(playerX + ' name your move:');
        move = input();
        theBoard[move] = turn;

        check = winchecker(theBoard, turn);
        if(check == 1):
            boardPrinter(theBoard);
            print(playerX + ' has won!');
            break;

    #allows player 0 to make a move
    elif(turn == 'O'):
        print(playerO + ' name your move:');
        move = input();
        theBoard[move] = turn;

        check = winchecker(theBoard, turn);
        if(check == 1):
            boardPrinter(theBoard);
            print(playerO + ' has won!');
            break;

    #changes turn
    if(turn == 'X'):
        turn = 'O';
    else:
        turn = 'X';

    drawcheck = drawchecker(theBoard);
    if (drawcheck == 1):
        print('It is a draw, no one wins.');
        break;
