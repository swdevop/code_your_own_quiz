easy_puzzle = 'Kirk Hammett, from Metallica, plays ___1___. He is an avid collector of ___2___ memorabilia. In fact, a ___1___ he owns features a movie ___3___ named Frankenstein. Kirk tends to like using the wah ___4___. '

easy_answers = ["guitar", "horror", "monster", "pedal"]

medium_puzzle = 'The band Judas Priest, led by ___1___ Rob Halford, is considered one of the best ___2___ bands in history. Rob Halford is also considered to have one of the best ___3___ in the genre. He left Judas Priest for a few ___4___ but returned to the excitement of fans.'

medium_answers = ["singer", "metal", "voices", "years"]

hard_puzzle = 'Zakk Wylde, has played ___1___ for Ozzy Osbourne and also for his own band, Black Label Society. He has also ___2___ with bands such as Allman Brothers Band and is highly ___3___ for his ability on ___1___. His ___1___ is famous for the black and white ___4___'

hard_answers = ["guitar", "performed", "respected", "bullseye"]

def difficulty():
    """
    Allows user to choose difficulty
    """
    game_level = raw_input("Enter your desired difficulty (easy, medium, hard): ")

    if game_level == "easy":
        return easy_puzzle, easy_answers
    elif game_level == "medium":
        return medium_puzzle, medium_answers
    elif game_level == "hard":
        return hard_puzzle, hard_answers
    else:
        print "That is not a valid choice!"
        return difficulty()

def answer_puzzle(puzzle, answers):
    """
    Asks user for input for each blank and, if answered correctly, replaces the blank with the correct answer
    """

    answered = []
    player_answer = ""

    index = 0
    blank_number = 1

    while index != len(answers):
        answer_blank = "___" + str(blank_number) + "___"
        player_answer = raw_input("What is your guess for " + answer_blank + "?")

        while player_answer != answers[index]:
            print "That is not the right answer!"
            player_answer = raw_input('Try again: ')

        print "Correct!"
        puzzle = puzzle.replace(answer_blank, player_answer)
        print puzzle
        blank_number = blank_number + 1
        index = index + 1


def play_game():
    """
    Begins the game. Once user has chosen difficulty, will pull the appropriate puzzle and answers. Ends the game once all blanks have been filled.
    """

    puzzle, answers = difficulty()
    print puzzle

    answered = answer_puzzle(puzzle, answers)

    print "You have filled in all the blanks!"

play_game()