import time
import random


Play_Game = 1

Name = "Names"
Names= ["*Rayyan*", "*Riad*", "*Imran*", "*Sami*", "*Maimun*"]

adv = "adventurer"
Advs = [
    "*young adventurer*", "*brave adventurer*", "*teenage adventurer*",
    "*teenage explorer*", "*brave explorer*",
    ]

I_want = "I_want"
I_Wants = [
    "*legendary treasure*", "*rare jewel*", "*great treasure*",
    "*rare gem*", "*hidden gem*",
    ]

Wise_man = "Wise_man"
Wise_Men = ["*ziad*", "*Ilyas*", "*Rashid*", "*Bilal*", "*Samir*"]

Sur_Name = "Sur_Name"
sur_Names = ["*Ayan*", "*Ehsan*", "*Jamal*", "*Mansur*", "*Qasim*"]





def text_sleep(Text, options, S_Time):
    # Add, Print, options the text, Then sleep after that.
    # "Text" is what I want to print.(Add it to list, Then print it).
    # "options" is If there is a specific word I want to write,
    # Like the beginning of all options(1/2../print).
    # "S_Time" if I want to sleep text a specific or the length of
    # a text / 10 "time"(0/ != 0).
    if options in ["1", "2", "3", "4"]:
        Op = f"Enter '{options}' if you want to: {Text}"
        print(Op)
        time.sleep(len(Op) / 1000)
    if options  == "print":
        List = Text.split("_c_")
        for each_item in List:
            print(each_item)
            if S_Time == 0:
                time.sleep(len(each_item) / 1000)
            else:
                time.sleep(S_Time/100)
        List = []


def options(T_Fi_OP, T_Se_OP, T_Th_OP, T_Fo_OP):
    #Print options, Make the user choose from them,
    #and Run the function of the option chosen by the user.
    # "T_Fi_OP" is the text of the first option.
    # "T_Se_OP" is the text of the second option.
    # "T_Th_OP" is the text of the third option.
    # "T_Fo_OP" is the text of the forth option.
    list_check = ["1", "2"]
    print("\n")
    text_sleep(T_Fi_OP, "1", 0)
    text_sleep(T_Se_OP, "2", 0)
    if T_Th_OP != "":
        text_sleep(T_Th_OP, "3", 0)
        list_check.append("3")
        if T_Fo_OP != "":
            text_sleep(T_Fo_OP, "4", 0)
            list_check.append("3")
            list_check.append("4")
    text_sleep("\nWhat do you want to do?", "print", 0.5)
    User_Input = input("-------) ")
    while True:
        if User_Input in list_check:
            return User_Input
        else:
            text_sleep(
                       "please *enter from the options above* (↑):"
                       , "print", 0.5
                       )
            User_Input = input("-------) ")


def score(New_s, End):
    # Changing the score and conditions for winning or losing.
    # "New_s" changes the result by adding or subtracting.
    # "End" if 1)This means that the game is over and the score will be
    # compared to the winning rate.
    global Current_score

    Current_score += New_s
    text_sleep(
               f"\n\nYour  score  is:    * {Current_score} *\n"
               , "print", 0
               )
    if End == "1":
        if Current_score >= 10:
            text_sleep(f"   !!congratulations!!", "print", 0)
            text_sleep(
                       f"    Try to play again\nto explore new ways to win."
                       , "print", 0
                       )
        if Current_score < 10:
            text_sleep(f"        !!Oops!!", "print", 0)
            text_sleep(
                       f"   Try to play again\nto reach the highest score."
                       , "print", 0
                       )


def add_random_list(Random_Li, Li):
    # This creates a list and adds arguments to it,
    # Then randomize the arguments and return one of them.
    # "Random_Li" That is the name of the list.
    # "Li" It's all on the list [Add, Random, Return] it.
    global Check_Random_Li

    if not Random_Li in Check_Random_Li:
        #If (Random_Li) list doesn't exist in this list(Check_Random_Li),
        #Add (Random_Li) list name, random result to this list(Check_Random_Li)
        Check_Random_Li.append(Random_Li)
        Random_Li = random.choice(Li)
        Check_Random_Li.append(Random_Li)
        return Random_Li
    else:
        #if the list name(Random_Li) exist, return the next value in this list
        #Check_Random_Li
        return Check_Random_Li[Check_Random_Li.index(Random_Li) + 1]





def story_begining():
    #The story will begin and options to next event.

    text_sleep("----) !Hello! (----\n", "print", 3)
    text_sleep("My Name is "\
               f"{add_random_list(Name, Names)}._c_I am a "\
               f"{add_random_list(adv, Advs)}._c_Who is on a quest to find a "\
               f"{add_random_list(I_want, I_Wants )} within a Magical Forest!\
               \n_c_"f"{add_random_list(Name, [])} had always heard tales of "\
               "the Magical Forest.They talked about strange things that "\
               "were happening in the Forest._c_One of them is the "\
               f"{add_random_list(I_want, [])} that could change anyone\'s"\
               " life completely.\n_c_After a while,"\
               f"{add_random_list(Name, [])} armed with a map.\n"\
               f"{add_random_list(Name, [])} goes on a journey to find the "\
               f"{add_random_list(I_want, [])} by entering into the Forest."\
               "\n_c_In the Forest,\nThere was a crossroads, with two "
               "different paths leading in opposite directions.\n_c_"\
               "The -first path- was quiet & safe, with flowers blooming on "\
               "both sides & birds chirping with a beautiful composition._c_"\
               "The -second path- was filled with trees, shadows, and a sense"\
               " of secrets. It was darker and more scary.\n", "print", 0
               )
    return options("go to the first path   *quiet & safe*.",
                   "go to the second path   *filled with trees*.", "", ""
                   )

def the_path_of_light():
    #The continuation, happens when user enter 1 in (story_begining) function.
    global Current_score
    Current_score += 1
    text_sleep("\n\n"\
               f"{add_random_list(Name, [])} followed the path of Light:\n_c_"\
               "The flowers along the path as if welcome to a "\
               f"{add_random_list(adv, [])} and The Birds chirped with a "\
               "beautiful composition.\n_c_After a while,\n"\
               f"{add_random_list(Name, [])} found a beautiful glade."\
               "In the center of the glade was a large, ancient tree with "\
               "golden leaves, At the base of it set a wise old elf,"\
               " Whose eyes were filled with knowledge and kindness.\n_c_"\
               "\'Hello to our Magical Forest,\' the elf said gently. "\
               "\'I have been expecting you, I am "\
               f"{add_random_list(Wise_man, Wise_Men)}, the guardian of this "\
               "glade. What brings you to our Magical Forest?!\n_c_"\
               f"{add_random_list(Name, [])} explained his quest for the "\
               f"{add_random_list(I_want, [])}.\n_c_"\
               "\'The treasure you want is real\' "\
               f"{add_random_list(Wise_man, [])} said,_c_\'but it is "\
               "protected by a superpower and can only be found by those with"\
               " a pure heart and wisdom mind.\nTo help you on your journey,"\
               "I can offer you a gift._c_But first, you must prove your "\
               "wisdom by answering a riddle\'.\n_c_"\
               f"{add_random_list(Name, [])} agreed, and "\
               f"{add_random_list(Wise_man, [])} presented the riddle.\n_c_"\
               "The riddle is:\n    \'I speak without a mouth and hear "\
               "without ears. I have nobody, but I come alive with the wind."\
               "What am I?\' ", "print", 0
               )
    return options("Answer the riddle correctly.",
                   f"Ask for a hint from "f"{add_random_list(Wise_man, [])}."\
                   , "Politely decline and continue without the gift.", ""
                   )

def answer_the_riddle_correctly():
    #The continuation, happens when user enter 1 in(the_path_of_light)function.
    global Current_score
    Current_score += 2
    text_sleep("\n\n"\
               f"{add_random_list(Name, [])} thinks the riddle for a moment.."\
               "_c_\n\'An echo\', "f"{add_random_list(Name, [])} said it "\
               "confidently.\n_c_\'You are correct, "\
               f"{add_random_list(adv, [])}\' "\
               f"{add_random_list(Wise_man, [])} said.\n\'\"An echo\" it is, "\
               "Your wisdom has proven your worth\'\n_c_"\
               f"{add_random_list(Wise_man, [])} handed a small amulet to "\
               f"{add_random_list(Name, [])} and told him._c_\'When this"\
               "amulet glows brightly, it means that the treasure you found"\
               "is real or you are on your way to it.\' "\
               f"{add_random_list(Wise_man, [])} said._c_\n"\
               f"{add_random_list(Name, [])} thanked "\
               f"{add_random_list(Wise_man, [])} and continued along the Path"\
               "of Light, feeling more confident with the amulet on his neck."\
               "\n_c_The path led him to a lake that mirrored the sky. At the"\
               "edge of the lake, "\
               f"{add_random_list(Name, [])} noticed a boat with a strong "\
               "light.\n_c_"f"{add_random_list(Name, [])} thinks for "\
               "a moment.", "print", 0
               )
    return options("Take the boat across the lake.",
                   "Walk around the lake, exploring the surroundings.",
                   "Reset by the lake and search for any signs to help him.",
                   "")

def across_the_lake():
    #The continuation, happens when the user enter 1 in(a_t_r_correct)function.
    global Current_score
    Current_score += 2
    text_sleep("\n\n"\
               f"{add_random_list(Name, [])} decided to take the boat across "\
               "the lake, feeling that it would lead to the next part of the "\
               "journey.\n_c_In the middle way to the other side of the lake,"\
               " A guy appeared on another boat!\n\n\'Hello! I\'m "\
               f"{add_random_list(Sur_Name, sur_Names)}. The Guardian of the "\
               "Lake.\nYou have shown incredible courage and wisdom to come "\
               "this far all your journey._c_To reach your goal, you must "\
               "pass the final test."\
               "Answer me this: What is the true treasure you seek?\'\n_c_"\
               f"{add_random_list(Name, [])} answered \'"\
               f"{add_random_list(I_want, [])}\'_c_\'think deeply about all "\
               "the journey you have\' "\
               f"{add_random_list(Sur_Name, [])} said.\n_c_"\
               f"{add_random_list(Name, [])} think deeply about the journey "\
               "and answer._c_\'oh! Yes, The Treasure is the knowledge, "\
               "growth, and experiences gained along the way. It is about "\
               "understanding the world & the connections we make with it.\'"\
               f"{add_random_list(Name, [])} said\n_c_"\
               f"{add_random_list(Sur_Name, [])} smiled, Then he ordered the "\
               "boat to go ahead to the hidden island, where an ancient chest"\
               " was buried under a tree there.\n_c_After a while...\n"\
               "The chest was opening, The amulet around "\
               f"{add_random_list(Name, [])}\’s neck glowed brightly,"\
               "which meant the treasure was real.", "print", 0
               )

def walk_around():
    #The continuation, happens when the user enter 2 in(a_t_r_correct)function.
    global Current_score
    Current_score += 1
    text_sleep("\n\n"\
               f"{add_random_list(Name, [])} decided to explore the erea, "\
               f"{add_random_list(Name, [])} walked along the edge of the "\
               "lake._c_The water was so clear that "\
               f"{add_random_list(Name, [])} could see fish swimming, "\
               "and the air was filled with the scent of flowers.\n_c_As Alex"\
               " walked, he noticed something unusual._c_There was a strange "\
               "writing near the shore on a large rock._c_The writing said:"\
               "\'Continue your journey, do not give up, and remember that "\
               "the real treasure is obtaining knowledge\'\n_c_"\
               f"{add_random_list(Name, [])} realized the importance of the"\
               " message, so he continued along the path._c_\nAfter some time"\
               ", the path guided him to a cave. Upon entering, he discovered"\
               " an ancient chest in the center of the cave._c_"\
               f"{add_random_list(Name, [])} approached the chest and noticed"\
               " that there was a lock on it, so he took a deep breath, and "\
               "he tried to put the amulet in the lock, and the chest opened "\
               "with a soft click.\n_c_Inside the chest, there was the "\
               f"{add_random_list(I_want, [])} that he was looking for from "\
               "the beginning._c_\nA voice said :\n  \'Congratulations, "\
               f"{add_random_list(adv, [])}. You have proven your wisdom\'"
               , "print", 0
               )

def observe_the_area():
    #The continuation, happens when the user enter 3 in(a_t_r_correct)function.
    global Current_score
    Current_score += 1
    text_sleep("\n\n"\
               f"{add_random_list(Name, [])} decided to rest by the lake,"\
               " looking at the lake.\n_c_"\
               f"{add_random_list(Name, [])} sat down on a smooth rock at the"\
               " water\'s edge, pulling out the map to study it more closely."\
               "\n_c_Surprise! A glow came out from the amulet and into a "\
               "specific area on the map that "f"{add_random_list(Name, [])}"\
               "hadn\'t noticed before. "\
               f"{add_random_list(Name, [])} realized it was very close to "\
               "his current location.\n_c_"\
               f"{add_random_list(Name, [])} looked around the lake and "\
               "noticed a small, hidden cave, Then the amulet’s light grew "\
               "brighter, "f"{add_random_list(Name, [])} realized that the "\
               "cave he had found inside contained what he had been looking "\
               "for._c_\ninside the cave, he found a small, ancient chest "\
               "with beautiful designs.\n_c_With a sense of excitement, "\
               f"{add_random_list(Name, [])} opened the chest. "\
               "Inside, he found not gold or jewels, but a beautiful book "\
               "with a glowing cover.\n_c_Opening the book, "\
               f"{add_random_list(Name, [])} discovered it was filled with "\
               "knowledge.\n_c_As Alex get out from the cave, book in hand, "\
               f"{add_random_list(Wise_man, [])} appeared once more."\
               "\n_c_\'You have found the true treasure,\' "\
               f"{add_random_list(Wise_man, [])} said with a smile. \'So you"\
               " now realize that the real treasure is knowledge."\
               "\nUse it wisely\'"\
               f"{add_random_list(Name, [])} thanked "\
               f"{add_random_list(Wise_man, [])} and, with the book and "\
               "amulet began the journey back home.\' ", "print", 0
               )

def ask_for_a_hint():
    #The continuation, happens when user enter 2 in(the_path_of_light)function.
    global Current_score
    Current_score += 1
    text_sleep("\n\n"\
               f"{add_random_list(Name, [])} thinks for a moment but found it"\
               " quite perplexing. \'Could you give me a hint, "\
               f"{add_random_list(Wise_man, [])}?\'"\
               f"{add_random_list(Name, [])} asked politely.\n_c_"\
               f"{add_random_list(Wise_man, [])} smiled kindly. \'Think about"\
               " something that can be heard but not seen\'\n_c_With the hint"\
               f", {add_random_list(Name, [])} thought harder and finally"\
               " realized the answer._c_\'You are an echo!\' "\
               f"{add_random_list(Name, [])} exclaimed.\n_c_You are correct."\
               "An echo it is.\n_c_"\
               f"{add_random_list(Wise_man, [])} handed "\
               f"{add_random_list(Name, [])} a beautiful book.\n\'This book "\
               "contains most of what you will need during your journy\' "\
               f"{add_random_list(Wise_man, [])} said."\
               f"{add_random_list(Name, [])} thanked the old elf and "\
               "continued his journey, Feeling more confused with the book.\n"\
               f"_c_As {add_random_list(Name, [])} continued to explore, "\
               "doubts began to creep in. The journey had been long and "\
               "challenging, The stories of the treasure had always"\
               " seemed like a distant dream._c_"\
               f"{add_random_list(Name, [])} thought about the village, the "\
               "familiar faces, and the warmth of home.\n_c_After a while, "\
               f"{add_random_list(Name, [])} remmeber the book that "\
               f"{add_random_list(Wise_man, [])} give him, So he opened the "\
               "book\n_c_The first thing written in the book is \'Don\'t"\
               " give up, \nYou are almost at the treasure.\'\n_c_"\
               f"{add_random_list(Name, [])} followed the advices in the "\
               "book,\nThen he found what he was looking for.\n\n"\
               f"The {add_random_list(I_want, [])}", "print", 0
               )

def politely_decline():
    #The continuation, happens when user enter 3 in(the_path_of_light)function.
    global Current_score
    Current_score += 2
    text_sleep("\n\n"\
               f"{add_random_list(Name, [])} thought for a moment. Though "\
               "intrigued by the challenge, he decided to rely on his own "\
               f"skills.\n_c_{add_random_list(Name, [])} said, \'Thank you, "\
               f"{add_random_list(Wise_man, [])}, but I believe I must"\
               " continue this journey on my own\'\n_c_"\
               f"{add_random_list(Wise_man, [])} smiled warmly. Very well, "\
               f"{add_random_list(adv, [])}.\n\n_c_"\
               f"As {add_random_list(Name, [])} continued to explore, doubts "\
               "began to creep in. The journey had been long and challenging,"\
               "The stories of the treasure had always seemed like a distant "\
               f"dream.\n_c_{add_random_list(Name, [])} thought about the "\
               "dream.\n_c_village, the familiar faces, and the warmth of "\
               "home.\n_c_After a while, "\
               f"{add_random_list(Name, [])} decided to turn back home."\
               f"{add_random_list(Name, [])} returned to the village "\
               "with determination, despite feeling heavy-hearted.", "print", 0
               )

def the_path_of_shadows():
    #The continuation, happens when user enter 1 in (story_begining) function.
    global Current_score
    Current_score += 0
    text_sleep("\n\n"\
               f"{add_random_list(Name, [])} choose the Path of Shadows, "\
               "feeling a strange pull towards. As they walked, the air "\
               "grew cooler, and the sounds of the forest quieted.\n_c_"\
               f"After some time, {add_random_list(Name, [])} stumbled upon"\
               " an ancient stone archway covered in vines. Stepping through,"\
               " they found themselves in a hidden glade, illuminated by a "\
               "soft, silver light from an unseen source._c_In the center of "\
               "the glade stood a pedestal with an ornate chest "\
               "resting on top._c_Approaching cautiously, "\
               f"{add_random_list(Name, [])} opened the chest to reveal the "\
               "legendary treasure: a glowing, crystal amulet.", "print", 0
               )





while Play_Game == 1:
    Current_score = 5
    Check_Random_Li = []

    # fuctions that make the game more fun
    option_1 = story_begining()
    if option_1 == "1":
        option_2 = the_path_of_light()
        if option_2 == "1":
            option_3 = answer_the_riddle_correctly()
            if option_3 == "1":
                across_the_lake()
            elif option_3 == "2":
                walk_around()
            elif option_3 == "3":
                observe_the_area()
        elif option_2 == "2":
            ask_for_a_hint()
        elif option_2 == "3":
            politely_decline()
    elif option_1 == "2":
        the_path_of_shadows()



    if options("Play Again", "End Game", "", "") == "2":
        Play_Game = 2
        score(0, "1")