
"""
    INTRODUCTION:
        i want to make a trivia about halo
        i will have 4 stages with 17 questions in each and they get more difficult.
        you need 170 points to finish a stage
        if they have a correct answer they will +10 if they have a wrong answer  they will get -10
        i will have 3 types of questions: yes-no, multi choice, and you type in the answer question.

    OPTIONAL IDEAS
        color if we have time
        make a gulty spark in the background. and cange the background as questions go by.

"""


def RunIntroduction():
    print(  "welcome reclamer,")
    print ("i am 343 gulty spark, i have been observing for the last melenium. and not only"
          + " do i see the halo plan sucsessfull, but i see a lot has changed. and i have a few questions. "
          + "can you anwer them?")

def RunLevel_1():
    level1Score = 0
    user_input = raw_input("respond yes or no: ")
    if user_input == "yes":
        level1Score += 10
    else:
        print ("reclamer!?... ALREADY!!? YOU DISCUST ME!!!")
        level1Score -= 10
    user_input = raw_input("great! now just in case.... do you know what reclamer means? (one word awnser) ")
    if user_input.lower() in ("human"): # what will you do if the user typed Human, or HuMaN are they still correct?
        level1Score += 10
    else:
        print ("reclamer!?... how do you not know your species formal name!!? this is disoponting..")
        level1Score -= 10
    user_input = raw_input("next do you know how old the master cheif is? ")
    if user_input == "18":
        level1Score += 10
    else:
        print ("reclamer!?... how do you not know your species savior? you are clearly not good at this..")
        level1Score -= 10
    user_input = raw_input("who is Thel Vadum? (2 word answer start with: the (YOUR ANSWER)")
    if user_input.lower() in ("the arbiter"):
        level1Score += 10
    else:
        print ("reclamer!?... how do you not know your species allys leaders? you disopont me... you are wasting my time!")
        level1Score -= 10

    return level1Score


def RunLevel_2():
    #NYI
    return 0



def RunTheGame():
    RunIntroduction()
    totalScore = 0
    passScore = 170

    scoreForLevel_1 = RunLevel_1()
    totalScore = totalScore + scoreForLevel_1
    if scoreForLevel_1 < passScore:
        RunGameOver("obsevation 1", totalScore)
        return

    scoreForeLevel_2 = RunLevel_2()
    totalScore = totalScore + scoreForeLevel_2
    if scoreForeLevel_2 < passScore:
        RunGameOver("obsevation 2", totalScore)
        return

def RunGameOver(levelName, score):
    print("Failed in {} score is {}".format(levelName, score))
    print ("reclamer, arn't you soposed to know yourself! arn't you soposed to know the present! ann't you soposed to know! i will terminate you for wasting my time!@@$#$!@!!!!!!")

if __name__ == "__main__":
    RunTheGame()