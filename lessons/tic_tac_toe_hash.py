board_hash = {
"top-left" : "-",
"top-center" : "-",
"top-right" : "-",
"middle-left" : "-",
"middle-center" : "-",
"middle-right" : "-",
"bottom-left" : "-",
"bottom-center" : "-",
"bottom-right" : "-"
}

def print_board(hash):
    print(board_hash["top-left"], "|", board_hash["top-center"], "|", board_hash["top-right"])
    print("-----------")
    print(board_hash["middle-left"], "|", board_hash["middle-center"], "|", board_hash["middle-right"])
    print("-----------")
    print(board_hash["bottom-left"], "|", board_hash["bottom-center"], "|", board_hash["bottom-right"])

def tic_tac_toe(pos,sym):
    for key, value in board_hash.items():
        board_hash[pos] = sym
        return board_hash

def stop():
    print("You won!")
    quit()

def check(hash):
    for key, value in board_hash.items():
        if board_hash["top-left"]  == board_hash["top-center"] == board_hash["top-right"]:
            if board_hash["top-left"] != "-" :
                stop()
        elif board_hash["middle-left"]  == board_hash["middle-center"] == board_hash["middle-right"]:
            if board_hash["top-left"] != "-" :
                stop()
        elif board_hash["bottom-left"]  == board_hash["bottom-center"] == board_hash["bottom-right"]:
            if board_hash["top-left"] != "-" :
                stop()

def repeat():
    count = 0
    stop = 9
    while count < stop:
        count +=1
        position = input("Where?")
        symbol = input("o or x?")
        new_board = tic_tac_toe(position, symbol)
        check(print_board(new_board))

repeat()
