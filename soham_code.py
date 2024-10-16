import random
import time
from inputimeout import inputimeout, TimeoutOccurred

sign = ["+", "-", "×", "÷"]

# queations
while True:
    try:
        qn = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Enter a number for count of queations")


# main function
def gen(n):
    s = random.choice(sign)
    if s == "×" or s == "÷":
        x = random.randint(1, 10000)
        y = random.randint(1, 10)
        ans = None

        if s == "÷":
            a = x // y
            print("Q.", +n, "What is", x, s, y, "?")
            try:
                ans = int(inputimeout(prompt="Enter the ans You have 1 minute:- ", timeout=60))#timeout value in second
            except TimeoutOccurred:
                print("Time is over", TimeoutOccurred)
            n += 1
            if ans == a:
                print("very good!")
                print("Answer is", a)
            else:
                print("Answer is", a)
        else:
            a = x * y
            print("Q.", +n, "What is", x, s, y, "?")
            try:
                ans = int(inputimeout(prompt="Enter the ans You have 1 minute:- ", timeout=60))#timeout value in second
            except TimeoutOccurred:
                print("Time is over", TimeoutOccurred)
            n += 1
            if ans == a:
                print("wall done!")
                print("Answer is", a)
            else:
                print("Answer is", a)

    else:
        x = random.randint(1, 10000)
        y = random.randint(1, 10000)

        if s == "+":
            a = x + y
            print("Q.", +n, "What is", x, s, y, "?")
            try:
                ans = int(inputimeout(prompt="Enter the ans You have 1 minute:- ", timeout=60))#timeout value in second
            except TimeoutOccurred:
                print("Time is over")
            n += 1
            if ans == a:
                print("keep it up!!")
                print("Answer is", a)
            else:
                print("Answer is", a)
        else:
            a = x - y
            print("Q.", +n, "What is", x, s, y, "?")
            try:
                ans = int(inputimeout(prompt="Enter the ans You have 1 minute:- ", timeout=60))#timeout value in second
            except TimeoutOccurred:
                print("Time is over", TimeoutOccurred)
            n += 1
            if ans == a:
                print("correct!")
                print("Answer is", a)
            else:
                print("Answer is", a)


# driver code
for i in range(1, qn + 1, 1):
    gen(i)
