import random


def turn():
    pass

def correct_guess(userInput, word):
    bool = False
    if(userInput in word):
        bool = True
    return bool 
def update_board(user_input, word, board):
    for i in range(len(word)):
        if(user_input == word[i] ):
            board[i] = user_input    
    return board

def current_board(word):
    board = []
    for i in range(len(word)):
        board.append("_")
    return board

def game_loop():
    word_list = ["Appendix","Heart","Valve"]
    word = word_list[random.randint(0,len(word_list) - 1)]
    word = word.lower()
    board = current_board(word)
    print("Welcome to Hangman type quit to exit type solve to solve")

    turn_count = 0
    user_input = ""
    while True:
        print("This is Hangman type quit to exit type solve to solve")
        print(board)
        if(turn_count == 6):
            print("You lost")
            print(board)
            print(word)
            break
        if(list(word) ==  board):
            print("You win")
            print("Word:", word)
            break
        if(user_input == "quit"):
            break
        if(user_input == "solve"):
            solve_input = input("What is the word?")
            if(solve_input == word):
                break
            else:
                print("Wrong answer!")
    

        while True:
                user_input = str(input("Enter a letter").lower())
                if(user_input.isalpha() and len(user_input) == 1 ):
                    break
                else:
                    print("Please single letter")
             
        
        if(user_input in word and user_input not in board):
            update_board(user_input, word, board)
        else:
            turn_count += 1


    
game_loop()

    


    



