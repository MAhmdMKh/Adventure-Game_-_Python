"""
Text adventure game - my first Python project.

The player reads a short story and chooses between 2-3 options.
Each choice changes the score. At the end, the score decides win or lose.

File structure:
    1. Setup     : imports, constants, and the lists of random words.
    2. Helpers   : text_sleep, options, add_points, show_result,
                   add_random_list.
    3. Story     : one small function for each event.
    4. Main loop : connects the story functions and lets the player replay.

Practiced: variables, lists, strings, functions, if/elif, while loops,
the random and time modules, and the global keyword.
"""


import time
import random

play_game = True
START_SCORE = 5                 # The difference must be 5
WIN_SCORE = 10                  # The difference must be 5

# For the TIME CONTROLLERS (↓ to increase speed) (↑ to decrease speed):

# The time controller of the Choices after the story -- Original = 30
CHOICE_CHARS_PER_SEC = 1000
# The time controller of the story itself -- Original = 15
STORY_CHARS_PER_SEC = 1000

NAME_KEY = "NAMES"
NAMES = ["*Rayyan*", "*Riad*", "*Imran*", "*Sami*", "*Maimun*"]

ADV_KEY = "adventurer"
ADVENTURERS = [
    "*young adventurer*", "*brave adventurer*", "*teenage adventurer*",
    "*teenage explorer*", "*brave explorer*",
    ]

I_WANT_KEY = "I_WANT_KEY"
TREASURES = [
    "*legendary treasure*", "*rare jewel*", "*great treasure*",
    "*rare gem*", "*hidden gem*",
    ]

WISE_MAN_KEY = "WISE_MAN_KEY"
WISE_MEN = ["*ziad*", "*Ilyas*", "*Rashid*", "*Bilal*", "*Samir*"]

SUR_NAME_KEY = "SUR_NAME_KEY"
SURNAMES = ["*Ayan*", "*Ehsan*", "*Jamal*", "*Mansur*", "*Qasim*"]



def text_sleep(text, modes, sleep_time):
    """
    Print text slowly, so the player has time to read it.

    Text    : the text to print.
    options : "1" to "4" prints Text as a numbered choice
              ("Enter '1' if you want to: ..."). "print" prints Text as
              story text, split into separate lines at every "_c_".
    S_Time  : only used with "print". 0 = wait after each line according
              to its length (len / 1000 seconds). Any other number =
              wait S_Time / 100 seconds after each line.
    """
    if modes in ["1", "2", "3", "4"]:
        choice_text = f"Enter '{modes}' if you want to: {text}"
        print(choice_text)
        time.sleep(len(choice_text) / CHOICE_CHARS_PER_SEC)
    if modes  == "print":
        lines = text.split("_c_")
        for each_item in lines:
            print(each_item)
            if sleep_time == 0:
                time.sleep(len(each_item) / STORY_CHARS_PER_SEC)
            else:
                time.sleep(sleep_time)


def options(first_text_option, second_text_option,
            third_text_option, fourth_text_option):
    """
    Show 2-4 choices, keep asking until the player enters a valid one,
    then return it as a string ("1", "2", "3" or "4").

    T_Fi_OP, T_Se_OP : text of options 1 and 2 (always shown).
    T_Th_OP, T_Fo_OP : text of options 3 and 4. Use "" if not needed.
                       (Option 4 is only used if option 3 is used too.)
    """
    list_check = ["1", "2"]
    print("\n")
    text_sleep(first_text_option, "1", 0)
    text_sleep(second_text_option, "2", 0)
    if third_text_option != "":
        text_sleep(third_text_option, "3", 0)
        list_check.append("3")
        if fourth_text_option != "":
            text_sleep(fourth_text_option, "4", 0)
            list_check.append("4")
    text_sleep("\nWhat do you want to do?", "print", 0)
    user_input = input("-------) ")
    while True:
        if user_input in list_check:
            return user_input
        else:
            text_sleep(
                       "please *choose from the options above* (↑):"
                       , "print", 0
                       )
            user_input = input("-------) ")


def add_random_list(Random_Li, Li):
    """
    Pick a random item from Li the FIRST time Random_Li is used,
    then return that same item every time after that in the same game.

    Random_Li : the label of the group (like NAME_KEY).
    Li        : the list to pick from. After the first call it can be [].
    Check_Random_Li remembers each label and the item chosen for it.
    """
    global check_random_li

    if not Random_Li in check_random_li:
        # First time: pick a random item and remember it.
        check_random_li.append(Random_Li)
        Random_Li = random.choice(Li)
        check_random_li.append(Random_Li)
        return Random_Li
    else:
        # Already picked: return the item stored after the label(Random_Li).
        return check_random_li[check_random_li.index(Random_Li) + 1]


def add_points(points):
    # Add points to the score (use a negative number to subtract).
    global current_score

    current_score += points


def show_result():
    # Print the final score, then the win or lose message.
    text_sleep(
               f"\n\nYour  score  is:    * {current_score} *\n"
               , "print", 2
               )
    if current_score >= WIN_SCORE:
        text_sleep("    !!CONGRATULATIONS!!", "print", 0)
        text_sleep(
                   "     Try to play again\nto explore new ways to win."
                   , "print", 0
                   )
    else:
        text_sleep("         !!OOPS!!", "print", 0)
        text_sleep(
                   "     Try to play again\nto reach the highest score."
                   f"    ({WIN_SCORE})"
                   , "print", 0
                   )





def story_beginning():
    text_sleep("----) !Hello! (----\n", "print", 2)
    text_sleep(f"I am {add_random_list(NAME_KEY, NAMES)}, "
               f"a {add_random_list(ADV_KEY, ADVENTURERS)}._c_"
               f"I want to find the {add_random_list(I_WANT_KEY, TREASURES)}."
               "_c_There are two roads: a sunny one and a dark one.\n",
               "print", 0
               )
    return options("take the sunny road.", "take the dark road.", "", "")

def the_sunny_road():
    add_points(1)
    text_sleep("\n\n"
               f"{add_random_list(NAME_KEY, [])} reached a river._c_"
               f"{add_random_list(WISE_MAN_KEY, WISE_MEN)}, a wise man, "
               "was sitting there._c_"
               f"'The {add_random_list(I_WANT_KEY, [])} is across the river,'"
               f" said {add_random_list(WISE_MAN_KEY, [])}."
               , "print", 0
               )
    return options("Listen to the wise man's advice.",
                   "Ask the wise man to carry you.",
                   "Cross the river alone.", "")

def listen_to_advice():
    add_points(2)
    text_sleep("\n\n"
               "'Think before you move,' "
               f"said {add_random_list(WISE_MAN_KEY, [])}."
               "_c_'How will you cross?'", "print", 0
               )
    return options("Swim across.", "Build a raft.", "Jump on the stones.", "")

def swim_across():
    add_points(1)
    text_sleep("\n\n"
               "The water was too strong._c_"
               f"{add_random_list(NAME_KEY, [])} went back home.", "print", 0
               )

def build_a_raft():
    add_points(2)
    text_sleep("\n\n"
               f"{add_random_list(NAME_KEY, [])} built a raft & crossed safely"
               f"._c_On the other side, the {add_random_list(I_WANT_KEY, [])}"
               " was waiting!", "print", 0
               )

def jump_on_stones():
    add_points(1)
    text_sleep("\n\n"
               f"{add_random_list(NAME_KEY, [])} slipped & fell in the water."
               "_c_The journey ended here.", "print", 0
               )

def ask_for_help():
    add_points(2)
    text_sleep("\n\n"
               "'No one can do this for you,' said "
               f"{add_random_list(WISE_MAN_KEY, [])}._c_"
               f"{add_random_list(NAME_KEY, [])} went home.", "print", 0
               )

def cross_alone():
    add_points(1)
    text_sleep("\n\n"
               f"{add_random_list(NAME_KEY, [])} crossed alone._c_"
               "But the way was long and night came. Too late.", "print", 0
               )

def the_dark_road():
    add_points(2)
    text_sleep("\n\n"
               f"{add_random_list(SUR_NAME_KEY, SURNAMES)}, the guard, "
               f"stopped {add_random_list(NAME_KEY, [])}._c_"
               f"'{add_random_list(ADV_KEY, [])}! What do you want here?'"
               , "print", 0
               )
    return options("Tell the truth.", "Run away.", "", "")

def tell_the_truth():
    add_points(3)
    text_sleep("\n\n"
               "'An honest answer. You may pass,' said "
               f"{add_random_list(SUR_NAME_KEY, [])}._c_"
               f"Behind the gate, {add_random_list(NAME_KEY, [])} found "
               f"the {add_random_list(I_WANT_KEY, [])}!", "print", 0
               )

def run_away():
    add_points(2)
    text_sleep("\n\n"
               f"{add_random_list(NAME_KEY, [])} ran away and never came back."
               , "print", 0
               )





while play_game:
    current_score = START_SCORE
    check_random_li = []

    option_1 = story_beginning()
    if option_1 == "1":
        option_2 = the_sunny_road()
        if option_2 == "1":
            option_3 = listen_to_advice()
            if option_3 == "1":
                swim_across()
            elif option_3 == "2":
                build_a_raft()
            elif option_3 == "3":
                jump_on_stones()
        elif option_2 == "2":
            ask_for_help()
        elif option_2 == "3":
            cross_alone()
    elif option_1 == "2":
        option_2 = the_dark_road()
        if option_2 == "1":
            tell_the_truth()
        elif option_2 == "2":
            run_away()

    show_result()

    if options("Play Again", "End Game", "", "") == "2":
        play_game = False

    print("\n\n\n\n")