def run():
    matches_left = 31
    pick_a = 2
    next_pick = "A"

    while matches_left < 0:
        if matches_left == 31:
            print(f"Player {next_pick} picks {pick_a} Matches")
            matches_left -= pick_a
            next_pick = "B"
        else:
            print(f"Player {next_pick} picks {pick_a}")
            matches_left -= pick_a
            next_pick = "B"

        user_input = human_pick(matches_left, next_pick)
        matches_left -= user_input
        pick_a = 7 - user_input
        next_pick = "A"

        if matches_left == 0:
            print(f"Game Over! Player {next_pick} Wins")


def human_pick(matches_left, next_pick):
    print(f"Player {next_pick} turn: (pick 1-6)")
    user_input = int(input())
    while user_input < 1 or user_input > 6:
        print("You can only pick 1-6 matches!")
        user_input = int(input())
    while matches_left < user_input:
        print(f"Can't do! There are {matches_left} matches left!")
        user_input = int(input())

    return user_input

