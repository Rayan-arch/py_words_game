import time as t
import matplotlib.pyplot as plt
import random as r

#This program have been created for practice writing code in python
#Exercise from Udemy:
#https://www.udemy.com/course/learn-python-programming-a-step-by-step-course-to-beginners/learn/lecture/13722356#questions
#
#Create program to help the user type faster. Give him a word and ask him
#to write five times. Check how manny secounds it took him to type the word
#at each round.

y=[]
x=[1,2,3,4,5]
mistakes=0
wodospad=['wodospad','szkola','co','kto','mama','lucyna','przedszkole']
word_set = r.randrange(len(wodospad)+1)

print("Program to practice speed up typing words")
print("Try to type '"+wodospad[word_set]+"' five times and do not make mistakes")
ready=input("Can we start?(Y?N)").lower()

if ready == "y":
    print("start!")
    for fast in range(1,6):
        t.sleep(2)
        start=t.time()
        word=input("Round "+str(fast)+": ")
        end=t.time()
        time=end-start
        y.append(time)
        if word == wodospad[word_set]:
            print("Good work!\nYou can do it faster!")
        else:
            print("What a shame.\nTry again.")
            mistakes += 1
        print("It took you {} sec.".format(round(time,2)))
    print("You did {} mistake(s)".format(mistakes))
    print("You did it five times, how it feels?\nLet see your results!")
    

#And now show it on plot!

    plt.plot(x,y)
    legend=['1','2','3','4','5']
    plt.xticks(x,legend)
    plt.ylabel("Time (sec)")
    plt.xlabel("Attempts")
    plt.title("Your typing evolution")
    t.sleep(3)
    plt.show()
else:
    print("Mabe next time!")
    t.sleep(1)
    quit()
