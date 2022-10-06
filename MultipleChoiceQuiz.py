# This is a general knowledge, 10 question, multiple choice quiz.
Questions=["1. What is the biggest ocean?", "2. What is roughly the speed of sound? (mph/kph)", "3. What was the first country to use tanks in combat during WWI?", "4. Which of these ground animals are the fastest?", "5. What is the capital city of the Czech Republic?", "6. What is the highest amount you can get in a single throw of a dart (in darts)?"]
# ["7. ", "8. "],
# ["9. ", "10. "]]
Options=[["A-Arctic", "B-Indian", "C-Pacific", "D-Atlantic"],["A-330/500", "B-770/1200", "C-1200/2000", "D-2000/3200"],["A-Germany", "B-France", "C-Russia", "D-Britain"],["A-Cheetah", "B-Leopard", "C-Elephant", "D-Tiger"],["A-Warsaw", "B-Stockholm", "C-Prague", "D-Rome"],["A-180", "B-60", "C-30", "D-50"]]#,["A-", "B-", "C-", "D-"],["A-", "B-", "C-", "D-"],["A-", "B-", "C-", "D-"],["A-", "B-", "C-", "D-"]]
#        1.   2.   3.   4.   5.   6.   7.   8.   9.   10.
Answer=["C", "B", "D", "A", "C", "B"]#, "", "", "", ""]
Answers=["1. C-Pacific", "2. B-770/1200", "3. D-Britain", "4. A-Cheetah", "5. C-Prague", "6. B-60"]#, "7. ", "8. ", "9. ", "10. "]
import time
##################################################################################################################################
def MQuiz_Game():
    score = 0
    for question in Questions: # n starts at 1, goes up to the number of questions(6)(would be 10).
        nAnswer = 0 # This determines what number answer you are on. Previously i.
        # x = 0
        print(question) # Prints the question for the user to answer.
        print("Your options are:")
        print(Options)
        print()
        UserAnswer=input("Type in the letter of your answer for this question. (A, B, C or D)")
        print()
        if len(UserAnswer) > 1 or len(UserAnswer) < 1: # Check to see if answer is valid.
            print("Answer is invalid!")
        # else:
        #     UserAnswer.upper() != "A" or "B" or "C" or "D"
        #     print("Answer is invalid!")
        if UserAnswer.upper() == Answer[nAnswer]: # Converts users answer into upper case to save another array (of lower case numbers) and ultimately make it easier.
            time.sleep(0.5)
            print("Correct!")
            score = score+1 # Increments users score by 1 when answer is correct.
        else:
            time.sleep(0.5)
            print("Incorrect!")
        nAnswer = nAnswer+4 # This updates the answer for the next question.
        #if len(Questions)>n:
        print("Next question is:") # Ignore on last loop.
        time.sleep(0.5)
    print("You got", score, "out of", +len(Questions)) # Prints the end score that was achieved.
    print("This is all of the answers: ", Answers)
    return question, score, nAnswer # Returns the values of these varibles for next use of function.

MQuiz_Game()
# NOTES: