
"""
    INTRODUCTION:
        i want to make a trivia about halo
        i will have 4 stages with 17 questions in each and they get more difficult.
        you need 170 points to finish a stage
        if they have a correct answer they will +10 if they have a wrong answer  they will get -10
        i will have 3 types of questions: yes-no, multi choice, and you type in the answer question.

    OPTIONAL IDEAS
        color if we have time
        make a gulty spark in the background.

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
        level1Score += 170
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