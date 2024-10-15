import random
import time
from inputimeout import inputimeout, TimeoutOccurred


class GenerateMathQuiz:
    sign = ["+", "-", "×", "÷"]

    def __init__(self, qn):
        for i in range(1, qn+1):
            self.res = self.gen(i)
            print(self.res)

    def gen(self, n):
        s = random.choice(self.sign)
        if s == "×" or s == "÷":
            x = random.randint(1, 10000)
            y = random.randint(1, 10)
            ans = None

            if s == "÷":
                a = x // y
                print("Q.", +n, "What is", x, s, y, "?")
                try:
                    ans = int(
                        inputimeout(
                            prompt="Enter the ans You have 1 minute:- ", timeout=5
                        )
                    )  # timeout value in second
                except TimeoutOccurred:
                    return f"Time is over, right answer is:- {a}"

                if ans == a:
                    return f"very good! \n Answer is:- {a}"
                else:
                    return f"Your Answer is wrong and right ans is:- {a}"
            else:
                a = x * y
                print("Q.", +n, "What is", x, s, y, "?")
                try:
                    ans = int(
                        inputimeout(
                            prompt="Enter the ans You have 1 minute:- ", timeout=5
                        )
                    )  # timeout value in second
                except TimeoutOccurred:
                    return f"Time is over, right answer is:- {a}"
                if ans == a:
                    return f"very good! \n Answer is:- {a}"
                else:
                    return f"Your Answer is wrong and right ans is:- {a}"

        else:
            x = random.randint(1, 10000)
            y = random.randint(1, 10000)

            if s == "+":
                a = x + y
                print("Q.", +n, "What is", x, s, y, "?")
                try:
                    ans = int(
                        inputimeout(
                            prompt="Enter the ans You have 1 minute:- ", timeout=5
                        )
                    )  # timeout value in second
                except TimeoutOccurred:
                    return f"Time is over, right answer is:- {a}"
                if ans == a:
                    return f"very good! \n Answer is:- {a}"
                else:
                    return f"Your Answer is wrong and right ans is:- {a}"
            else:
                a = x - y
                print("Q.", +n, "What is", x, s, y, "?")
                try:
                    ans = int(
                        inputimeout(
                            prompt="Enter the ans You have 1 minute:- ", timeout=5
                        )
                    )  # timeout value in second
                except TimeoutOccurred:
                    return f"Time is over, right answer is:- {a}"
                if ans == a:
                    return f"very good! \n Answer is:- {a}"
                else:
                    return f"Your Answer is wrong and right ans is:- {a}"


# Driver code
if __name__ == "__main__":
    qn = None
    while True:
        try:
            qn = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Enter a number for count of queations")
       
    quiz_one = GenerateMathQuiz(qn)


