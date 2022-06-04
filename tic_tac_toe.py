import time
import sys
import random


def welcome_screen():
    print("Welcome to Tic Tac Toe")
    time.sleep(0.5)


def init_board():
    board = []
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append('.')
    return board


def print_board(board):
    print('   ' + '1' + '   ' + '2' + '   ' + '3')
    print('A  ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('  ' + '---' + '+' + '---' + '+' + '---')
    print('B  ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('  ' + '---' + '+' + '---' + '+' + '---')
    print('C  ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    print('  ' + '---' + '+' + '---' + '+' + '---')


def get_move(board, player):
     row, col = 0, 0
     while True:
        chosen_position = input('Choose a position for player {}: '.format(player)).casefold()
        if chosen_position == 'a1':
            row, col = 0, 0
            if board[row][col] == '.':
                return row, col
        elif chosen_position == 'a2':
            row, col = 0, 1
            if board[row][col] == '.':
                return row, col
        elif chosen_position == 'a3':
            row, col = 0, 2
            if board[row][col] == '.':
                return row, col
        elif chosen_position == 'b1':
            row, col = 1, 0
            if board[row][col] == '.':
                return row, col
        elif chosen_position == 'b2':
            row, col = 1, 1
            if board[row][col] == '.':
                return row, col
        elif chosen_position == 'b3':
            row, col = 1, 2
            if board[row][col] == '.':
                return row, col
        elif chosen_position == 'c1':
            row, col = 2, 0
            if board[row][col] == '.':
                return row, col
        elif chosen_position == 'c2':
            row, col = 2, 1
            if board[row][col] == '.':
                return row, col
        elif chosen_position == 'c3':
            row, col = 2, 2
            if board[row][col] == '.':
                return row, col
        elif chosen_position == 'quit':
            print('You have decided to quit. Farewell!')
            time.sleep(0.2)
            sys.exit()
        else:
            print('Wrong input')
            continue


def get_ai_move(board, player):
    row, col = 0, 0
    possible_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    while True:
        random_move = random.choice(possible_moves)
        if random_move == 'a1':
            row, col = 0, 0
            if board[row][col] == '.':
                return row, col
        elif random_move == 'a2':
            row, col = 0, 1
            if board[row][col] == '.':
                return row, col
        elif random_move == 'a3':
            row, col = 0, 2
            if board[row][col] == '.':
                return row, col
        elif random_move == 'b1':
            row, col = 1, 0
            if board[row][col] == '.':
                return row, col
        elif random_move == 'b2':
            row, col = 1, 1
            if board[row][col] == '.':
                return row, col
        elif random_move == 'b3':
            row, col = 1, 2
            if board[row][col] == '.':
                return row, col
        elif random_move == 'c1':
            row, col = 2, 0
            if board[row][col] == '.':
                return row, col
        elif random_move == 'c2':
            row, col = 2, 1
            if board[row][col] == '.':
                return row, col
        elif random_move == 'c3':
            row, col = 2, 2
            if board[row][col] == '.':
                return row, col


def get_ai_harder_move(board, player):
    row, col = 0, 0
    if player == '1':
        sign = 'X'
    if player == '2':
        sign = '0'
    possible_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    while True:
            if board[0][0] == board[0][1] == sign:
                row, col = 0, 2
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[0][1] == board[0][2] == sign:
                row, col = 0, 0
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif [1][0] == board[1][1] == sign:
                row, col = 1, 2
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[1][1] == board[1][2] == sign:
                row, col = 1, 0
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[2][0] == board[2][1] == sign:
                row, col = 2, 1
                if board[row][col] == ".":  
                    return row, col
                else:
                    continue
            elif board[2][1] == board[2][2] == sign:
                row, col = 2, 0
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[0][0] == board[1][0] == sign:
                row, col = 2, 0
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[1][0] == board[2][0] == sign:
                row, col = 0, 0
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[0][1] == board[1][1] == sign:
                row, col = 2, 1
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[1][1] == board[2][1] == sign:
                row, col = 0, 1
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[0][2] == board[1][2] == sign:
                row, col = 2, 2
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[1][2] == board[2][2] == sign:
                row, col = 0, 2
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[0][0] == board[1][1] == sign:
                row, col = 2, 2
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[1][1] == board[2][2] == sign:
                row, col = 0, 0
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[0][2] == board[1][1] == sign:
                row, col = 2, 0
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            elif board[1][1] == board[2][0] == sign:
                row, col = 0, 2
                if board[row][col] == ".":
                    return row, col
                else:
                    continue
            else:
                random_move = random.choice(possible_moves)
                if random_move == 'a1':
                    row, col = 0, 0
                    if board[row][col] == '.':
                        return row, col
                elif random_move == 'a2':
                    row, col = 0, 1
                    if board[row][col] == '.':
                        return row, col
                elif random_move == 'a3':
                    row, col = 0, 2
                    if board[row][col] == '.':
                        return row, col
                elif random_move == 'b1':
                    row, col = 1, 0
                    if board[row][col] == '.':
                        return row, col
                elif random_move == 'b2':
                    row, col = 1, 1
                    if board[row][col] == '.':
                        return row, col
                elif random_move == 'b3':
                    row, col = 1, 2
                    if board[row][col] == '.':
                        return row, col
                elif random_move == 'c1':
                    row, col = 2, 0
                    if board[row][col] == '.':
                        return row, col
                elif random_move == 'c2':
                    row, col = 2, 1
                    if board[row][col] == '.':
                        return row, col
                elif random_move == 'c3':
                    row, col = 2, 2
                    if board[row][col] == '.':
                        return row, col
                

def eval_hAI(board):         
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            if board[row][0] == 'X':
                return -10
            elif board[row][0] == '0':
                return 10
    for col in range(3):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]):
            if board[0][col] == 'X':
                return -10
            elif board[0][col] == '0':
                return 10
    if (board[0][0] == board[1][1] and board[1][1]== board[2][2]):
        if board[0][0] == 'X':
            return -10
        elif board[0][0] == '0':
            return 10
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if board[0][2] == 'X':
            return -10
        elif board[0][2] == '0':
            return 10
    return 0

    
def minimax(board, depth, isMax):
    score = eval_hAI(board)
    if score == 10:
        return score
    if score == -10:
        return score
    if not is_full(board):
        score = 0
        return score

    if isMax:
        best_score = -1000
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '.':
                    board[i][j] = '0'
                    score = minimax(board, depth + 1, isMax == False)
                    board[i][j] = '.'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, isMax == True)
                    board[i][j] = '.'
                    best_score = min(score, best_score)
        return best_score


def get_move_hAI(board):   
    best_score = -1000
    move = None 
    score = None
    row, col = 0, 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = '.'
                if score > best_score:
                    best_score = score
                    move = (i, j)
                    row = move[0]
                    col = move[1]
    return row, col


def mark(board, player, row, col):       
    if player == '1':
        if board[row][col] == '.':
            board[row][col] = 'X'
            return board
    if player == '2':
        if board[row][col] == '.':
            board[row][col] = '0'
            return board


def check_lines(board, sign):
    if (
       board[0][0] == board[0][1] == board[0][2] == sign or
       board[1][0] == board[1][1] == board[1][2] == sign or
       board[2][0] == board[2][1] == board[2][2] == sign or
       board[0][0] == board[1][0] == board[2][0] == sign or
       board[0][1] == board[1][1] == board[2][1] == sign or
       board[0][2] == board[1][2] == board[2][2] == sign or
       board[0][0] == board[1][1] == board[2][2] == sign or
       board[0][2] == board[1][1] == board[2][0] == sign):
           return True
    else:
        return False


def has_won(board, player):
    winning_player = ''
    if check_lines(board, 'X') == True:
        winning_player = '1'
        return winning_player
    elif check_lines(board, '0') == True:
        winning_player = '2'
        return winning_player
    else:
        winning_player = '0'
        return winning_player


def is_full(board):
    state = any('.' in subboard for subboard in board)
    return not state
    

def print_result(winner):
    if winner != '0':
        print("Player {} has won ! Congrats !".format(winner))
    else:
        print("Wow, it's a tie !")
    

def TEST_humanhuman():
    h_board = init_board()
    print_board(h_board)
    player1 = '1'
    player2 = '2'
    row1, col1 = 0, 0
    row2, col2 = 0, 0
    while not is_full(h_board):
        if check_lines(h_board, 'X') or check_lines(h_board, '0'):
            win_p = has_won(h_board, player1)
            print_result(win_p)
            break
        elif is_full(h_board):
            full_b = has_won(h_board, player1)
            print_result(full_b)
            break
        else:
            row1, col1 = get_move(h_board, player1)
            h_board = mark(h_board, player1, row1, col1)
            print_board(h_board)
            if check_lines(h_board, 'X') or check_lines(h_board, '0'):
                win_p = has_won(h_board, player1)
                print_result(win_p)
                break
            elif is_full(h_board):
                full_b = has_won(h_board, player1)
                print_result(full_b)
                break 
            else:
                row2, col2 = get_move(h_board, player2)
                h_board = mark(h_board, player2, row2, col2)
                print_board(h_board)


def TEST_human_hAI():
    h_board = init_board()                  
    print_board(h_board)
    player1 = '1'
    player2 = '2'
    row1, col1 = 0, 0
    row2, col2 = 0, 0
    while not is_full(h_board):
        if check_lines(h_board, 'X') or check_lines(h_board, '0'):   
            win_p = has_won(h_board, player1)
            print_result(win_p)
            break
        elif is_full(h_board):
            full_b = has_won(h_board, player1)
            print_result(full_b)
            break
        else:
            row1, col1 = get_move(h_board, player1)
            h_board = mark(h_board, player1, row1, col1)
            print_board(h_board)
            if check_lines(h_board, 'X') or check_lines(h_board, '0'):   
                win_p = has_won(h_board, player1)
                print_result(win_p)
                break
            elif is_full(h_board):
                full_b = has_won(h_board, player1)
                print_result(full_b)
                break 
            else:
                row2, col2 = get_move_hAI(h_board)
                h_board = mark(h_board, player2, row2, col2)
                print_board(h_board)


def TEST_human_eAI():
    h_board = init_board()
    print_board(h_board)
    player1 = '1'
    player2 = '2'
    row1, col1 = 0, 0
    row2, col2 = 0, 0
    while not is_full(h_board):
        if check_lines(h_board, 'X') or check_lines(h_board, '0'):
            win_p = has_won(h_board, player1)
            print_result(win_p)
            break
        elif is_full(h_board):
            full_b = has_won(h_board, player1)
            print_result(full_b)
            break
        else:
            row1, col1 = get_move(h_board, player1)
            h_board = mark(h_board, player1, row1, col1)
            print_board(h_board)
            if check_lines(h_board, 'X') or check_lines(h_board, '0'):
                win_p = has_won(h_board, player1)
                print_result(win_p)
                break
            elif is_full(h_board):
                full_b = has_won(h_board, player1)
                print_result(full_b)
                break
            else:
                time.sleep(0.3)
                row2, col2 = get_ai_move(h_board, player2)
                h_board = mark(h_board, player2, row2, col2)
                print_board(h_board)


def TEST_human_harderAI():
    h_board = init_board()
    print_board(h_board)
    player1 = '1'
    player2 = '2'
    row1, col1 = 0, 0
    row2, col2 = 0, 0
    while not is_full(h_board):
        if check_lines(h_board, 'X') or check_lines(h_board, '0'):
            win_p = has_won(h_board, player1)
            print_result(win_p)
            break
        elif is_full(h_board):
            full_b = has_won(h_board, player1)
            print_result(full_b)
            break
        else:
            row1, col1 = get_move(h_board, player1)
            h_board = mark(h_board, player1, row1, col1)
            print_board(h_board)
            if check_lines(h_board, 'X') or check_lines(h_board, '0'):
                win_p = has_won(h_board, player1)
                print_result(win_p)
                break
            elif is_full(h_board):
                full_b = has_won(h_board, player1)
                print_result(full_b)
                break
            else:
                time.sleep(0.3)
                row2, col2 = get_ai_harder_move(h_board, player2)
                h_board = mark(h_board, player2, row2, col2)
                print_board(h_board)


def TEST_AIAI():
    h_board = init_board()
    print_board(h_board)
    player1 = '1'
    player2 = '2'
    row1, col1 = 0, 0
    row2, col2 = 0, 0
    while not is_full(h_board):
        if check_lines(h_board, 'X') or check_lines(h_board, '0'):
            win_p = has_won(h_board, player1)
            print_result(win_p)
            break
        elif is_full(h_board):
            full_b = has_won(h_board, player1)
            print_result(full_b)
            break
        else:
            time.sleep(1)
            row1, col1 = get_ai_move(h_board, player1)
            h_board = mark(h_board, player1, row1, col1)
            print_board(h_board)
            if check_lines(h_board, 'X') or check_lines(h_board, '0'):
                win_p = has_won(h_board, player1)
                print_result(win_p)
                break
            elif is_full(h_board):
                full_b = has_won(h_board, player1)
                print_result(full_b)
                break
            else:
                time.sleep(1)
                row2, col2 = get_ai_move(h_board, player2)
                h_board = mark(h_board, player2, row2, col2)
                print_board(h_board)


def play_again():
    while True:
        response = input("Want to play a game of Tic Tac Toe? (yes/no)").casefold()
        if response == 'yes':
            welcome_screen()
            main_menu()
            return 1
        elif response == 'no':
            print("Alrighty, see you next time !")
            sys.exit()
        else:
            print("Sorry, I didn't get that...")
            continue


def main_menu():
     while True:
         pick_game_mode = input("Please choose a game mode: \n 1: Player vs Player \n 2: Player vs easy AI \n 3: Player vs hard AI[NOT WORKING] \n 4: AI vs AI \n 5: Player vs harder AI \n Player 1 is X Player 2 is 0 \n").casefold()
         if pick_game_mode == '1':   
             TEST_humanhuman()
             play_again()
         elif pick_game_mode == '2':  
             TEST_human_eAI()
             play_again()
         elif pick_game_mode == '3':    
             TEST_human_hAI()
             play_again()
         elif pick_game_mode == '4':  
             TEST_AIAI()
             play_again()
         elif pick_game_mode == '5':
             TEST_human_harderAI()
             play_again()
         elif pick_game_mode == 'quit':
             print('You have decided to quit. Farewell!')
             time.sleep(0.2)
             sys.exit()
         else:
             print('Wrong input')
             continue
        


if __name__ == '__main__':
    play_again()
    if play_again():
        main_menu()

