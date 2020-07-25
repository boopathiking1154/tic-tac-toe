# write your code here


def stage_print(seq):
    """Function to print current field"""
    print("---------")
    print("| {} {} {} |".format(seq[0], seq[1], seq[2]))
    print("| {} {} {} |".format(seq[3], seq[4], seq[5]))
    print("| {} {} {} |".format(seq[6], seq[7], seq[8]))
    print("---------")


def check_win(seq, sign):
    """Function to check if user wins"""
    win_possibility = [[seq[0], seq[1], seq[2]], [seq[3], seq[4], seq[5]], [seq[6], seq[7], seq[8]],
                       [seq[0], seq[3], seq[6]], [seq[1], seq[4], seq[7]], [seq[2], seq[5], seq[8]],
                       [seq[0], seq[4], seq[8]], [seq[2], seq[4], seq[6]]]
    win = False
    for x in win_possibility:
        if x[0] == x[1] == x[2] == sign:
            win = True
            break
    return win


def get_coordinates(user):
    """Function to get coordinates from user"""
    while True:
        col, row = input("Enter the coordinates:").split()
        if not col.isdigit() or not row.isdigit():
            print('You should enter numbers!')
        elif not (1 <= int(col) <= 3) or not (1 <= int(row) <= 3):
            print("Coordinates should be from 1 to 3!")
        else:
            index = (int(col) - 1) + (9 - (3 * int(row)))
            if sequence[index] == ' ':
                sequence[index] = user
                break
            else:
                print("This cell is occupied! Choose another one!")
    stage_print(sequence)


sequence = list(" " * 9)
stage_print(sequence)
user_tag = 'X'
limit = 9

while limit:
    get_coordinates(user_tag)
    limit -= 1
    if sequence.count(" ") < 5:
        if check_win(sequence, user_tag):
            print('{} wins'.format(user_tag))
            break
    if user_tag == 'X':
        user_tag = 'O'
    elif user_tag == 'O':
        user_tag = 'X'
else:
    print("Draw")
