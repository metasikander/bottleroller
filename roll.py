#!/usr/bin/env python3
# coding: utf-8
import sys
import re
import random

try:
    # Use the system PRNG if possible
    random = random.SystemRandom()
except NotImplementedError:
    import warnings
    warnings.warn("A secure pseudo-random number generator is not available "
                  "on your system. Falling back to Mersenne Twister.")  # Mersenne twister is the default Python PRNG


# Takes no input and returns the results for a DnD 5e stats roll (4d6 drop lowest)
def stats_roll():
    stat_rolls = ''
    for i in range(6):
        total, rolls = dice_roller("4d6")
        lowest = int(min(rolls).split("/")[0])
        total = int(total) - lowest
        stat_rolls = stat_rolls + str(total) + str(rolls) + "\n"

    return stat_rolls

# Roll direction
def dir_roll():
    dir = ['N','NE','E','SE','S','SW','W','NW','Stay']
    dir_rolls = str(random.choice(dir))

    return dir_rolls


# Takes in a string with dice and returns the rolled dice and the sum
def dice_roller(input_text):
    # Function Variables
    r_dice = re.compile('\d*d\d+')               # Regex for detecting dice notation
    rolls = []                                   # List for keeping track of the rolls

    # dice rolling code
    def roll_dice(d):
        result = 0
        dice = d.group(0)                        # Zeroth group of regex match is the match itself

        # Split the string at the letter d
        dice_split = dice.split("d")

        times = int(dice_split[0]) if dice_split[0] is not '' else 1  # reads the number of rolls, falls back to one
        sides = int(dice_split[1])

        # Actually rolling the dice
        for t in range(times):
            roll = random.randrange(1, sides+1)
            rolls.append(str(roll) + "/" + str(sides))
            result += roll

        return str(result)

    # Regex the input and automatically run the dice rolling code when dice notation is detected and evaluate the output
    output = eval(r_dice.sub(roll_dice, input_text))

    return output, rolls


# Prints helpful information (Its own function for easier expansion later)
def info():
    print('Syntax is: roll <dice_code>\nExample: roll 2d8 + 6 + d8')
    print('Instead of a dice code you can also put "stats" or "dir" for a stats roll or direction roll respectively')


# Gets called whenever an error occurs
def error():
    info()
    sys.exit(2)


# Main function
def main():
    # If no arguments are given
    if len(sys.argv) is 1:
        error()

    # Commandline input handling
    input_list = sys.argv[1:]                    # Command line input (is a list)
    input_string = ''.join(input_list)           # Push everything together in a string

    if 'stats' in input_string.lower():
        print(stats_roll())
        sys.exit(0)

    # Directionroll
    if 'dir' in input_string.lower():
        print(dir_roll())
        sys.exit(0)

    # Check if help flag i is passed
    if "-h" in input_string.lower():
        info()
        sys.exit(0)

    # Execute the function and handle errors
    try:
        total, rolls = dice_roller(input_string)
        # Print the results
        print("Total:", total)
        print("Rolls:", rolls)
    except (SyntaxError, NameError):
        error()
    except ZeroDivisionError:
        print("You can not divide by zero")
        sys.exit(2)


if __name__ == "__main__":
    main()