# function to determine the score of a single roll
def roll_score(pins):
    return pins

# function to determine the score of a frame
def frame_score(roll1, roll2):
    if roll1 == 10:
        return 10 + roll_score(roll2) + roll_score(roll3)
    elif roll1 + roll2 == 10:
        return 10 + roll_score(roll3)
    else:
        return roll_score(roll1) + roll_score(roll2)

# function to determine the total score of the game
def game_score(rolls):
    total_score = 0
    roll_index = 0
    for frame in range(10):
        if rolls[roll_index] == 10:
            total_score += frame_score(rolls[roll_index], 0, rolls[roll_index+1])
            roll_index += 1
        else:
            total_score += frame_score(rolls[roll_index], rolls[roll_index+1])
            roll_index += 2
    return total_score

# example usage
rolls = [10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1]
print("Total score:", game_score(rolls))
