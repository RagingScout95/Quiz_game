from os import system
import time

system('cls') # clearing terminal
print("\n========== Welcome to Python quiz ==========\n")

# Asking player if they want to play or not 
playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    print("\nOk Lets play later than Cya\n")
    quit() # this will terminate the whole program

print("\nOkay!! Let's play :) \n")

time.sleep(1) # 1sec delay
system('cls') # clearing terminal

score = 0
# ---------------QUESTION 1
ans = input("Q1) Who developed Python Programming language? \nA) Wick Van Rossum\nB) Rasmus Lerdorf\nC) Guido Van Rossum\nD) Niene Stom\n\n Answer : ")
if ans.lower() == "c":
    print("Correct!!\n\n")
    score += 1
else:
    print("Incorrect the answer is c")
    print("Explanation: Python language is designed by a Dutch programmer Guido van Rossum in the Netherlands.\n\n")

# ---------------QUESTION 2
ans = input("Q2) Which type of Programming does Python support? \nA) object-oriented programming\nB) structured programming\nC) functional programming\nD) all of the mentioned\n\n Answer : ")
if ans.lower() == "d":
    print("Correct!!\n\n")
    score += 1
else:
    print("Incorrect the answer is d")
    print("Explanation: Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.\n\n")

# ---------------QUESTION 3
ans = input("Q3) Which of the following is the correct extension of the Python file? \nA) .python\nB) .pl\nC) .py\nD) .p\n\n Answer : ")
if ans.lower() == "c":
    print("Correct!!\n\n")
    score += 1
else:
    print("Incorrect the answer is c")
    print("Explanation: '.py' is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension '.py'.\n\n")

# ---------------QUESTION 4
ans = input("Q4) Is Python code compiled or interpreted? \nA) Python code is both compiled and interpreted\nB) Python code is neither compiled nor interpreted\nC) Python code is only compiled\nD) Python code is only interpreted\n\n Answer : ")
if ans.lower() == "b":
    print("Correct!!\n\n")
    score += 1
else:
    print("Incorrect the answer is b")
    print("Explanation: Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python.\n\n")

# ---------------QUESTION 5
ans = input("Q5) What will be the value of the following Python expression?\n4 + 3 % 5 \nA) 7\nB) 2\nC) 4\nD) 1\n\n Answer : \n")
if ans.lower() == "a":
    print("Correct!!\n\n")
    score += 1
else:
    print("Incorrect the answer is a")
    print("Explanation: The order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.\n\n")

if score  == 5:
    print("Wow You got all correct answers!!\n\n")
else:
    print("you got {} out of 5 \n\n".format(score))
