board=['X']*10
board[3]=' '
def get_move():
    num=''
    err = False
    while not num:
        # set prompt string
        if err:
            prompt =f"Ok {player}, try again...\n"   # if looped at least once already
        else:
            prompt = f"Ok {player}, your turn...\n" # first time only
        err = True # force 'Try again' prompt for subsequent loops
        # get number input
        num = input(prompt)
        # check is a number
        if not num.isnumeric():
            # if not number
            print(f'{num} is not a number! Try again.')
            num='' # reset num so while loop runs again
            continue
        # if num is a number
        num=int(num) # cast to int
        # check num is in range
        if num not in range(0,10):
            # out of range
            print(f'{num} is out of range')
            num='' # reset num so while loop runs again
            continue
        # check square available
        if board[num] != ' ':
            # not available
            print(f"Sorry {player}, that square is already taken!\nTry again...\n")
            num='' # reset num so while loop runs again
            continue
    return num