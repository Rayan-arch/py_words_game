import time as t
import matplotlib.pyplot as plt

#This program have been created for practice writing code in python
#Exercise from Udemy:
#https://www.udemy.com/course/learn-python-programming-a-step-by-step-course-to-beginners/learn/lecture/13722356#questions
#
#Create program to help the user type faster. Give him a word and ask him
#to write five times. Check how manny secounds it took him to type the word
#at each round.
print("Program to practice speed up typing words")
print("Try to type 'wodosplad' five times and do not make mistakes")
ready=input("Can we start?(Y?N)").lower()
x=[]
y=[1,2,3,4,5]
if ready == "y":
    print("start!")
    t.sleep(1)
    for fast in range(1,6):
        start=t.time()
        word=input("Roud "+str(fast)+": ")
        end=t.time()
        time=end-start
        x.append(time)
        if word == 'wodospad':
            print("Good work!\nYou can do it faster!")
        else:
            print("What a shame.\nTry again.")
        print("It took you {} sec.".format(round(time,2)
                                       ))
    print("You did it five times, how it feels?\n Let see your results!")
    plt.plot(x,y)
    plt.xlabel("sec")
    plt.ylabel("round")
    plt.title("Your Score")
    plt.show()
else:
    print("Mabe next time!")
    t.sleep(1)
    quit()
