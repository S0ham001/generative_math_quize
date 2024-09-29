import random
import time

sign = ['+','-','×','÷']

queations = int(input("how many Queations do you want ? : "))
q = 1
score = 0
while q <= queations:
    s = random.choice(sign)
    q += 1
    
    
    if s == '×' or s == '÷':
        x = random.randint(1, 10000)
        y = random.randint(1,10)
        
        if s == "÷":
            a = x // y
            print('Q.',+q,'What is',x,s,y,'?')
            ans = int(input('ans > '))
            if ans == a:
                print('very good!')
                print('Answer is', a)
                score += 1
            else:
                print("Answer is",a)
        else:
            a = x * y
            print('Q.',+q,'What is',x,s,y,'?')
            ans = int(input('ans > '))
            if ans == a:
                print('wall done!')
                print('Answer is', a)
                score += 1
            else:
                print("Answer is",a)
            
    else:
        x = random.randint(1, 10000)
        y = random.randint(1, 10000)
        
        if s == "+":
            a = x + y
            print('Q.',+q,'What is',x,s,y,'?')
            ans = int(input('ans > '))
            if ans == a:
                print('keep it up!!')
                print('Answer is', a)
                score += 1
            else:
                print("Answer is",a)
        else:
            a = x - y
            print('Q.',+q,'What is',x,s,y,'?')
            ans = int(input('ans > '))
            if ans == a:
                print('correct!')
                print('Answer is', a)
                score += 1
            else:
                print("Answer is",a)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
# =============================================================================
# 
#     if queations >= 20:
#         if score >= queations//2:
#             
#             print('I see you are good at it so lets level up!!')
#             print('from now on you will have a time limit in each queation')
#             print('you will get 45 second for each queation')
#             
#             if s == '×' or s == '÷':
#                 x = random.randint(1, 10000)
#                 y = random.randint(1,10)
#                 
#                 if s == "÷":
#                     a = x // y
#                     print('Q.',+q,'What is',x,s,y,'?')
#                     ans = int(input('ans > '))
#                     if ans == a:
#                         print('very good!')
#                         print('Answer is', a)
#                         score += 1
#                     else:
#                         print("Answer is",a)
#                 else:
#                     a = x * y
#                     print('Q.',+q,'What is',x,s,y,'?')
#                     ans = int(input('ans > '))
#                     if ans == a:
#                         print('wall done!')
#                         print('Answer is', a)
#                         score += 1
#                     else:
#                         print("Answer is",a)
#                     
#             else:
#                 x = random.randint(1, 10000)
#                 y = random.randint(1, 10000)
#                 
#                 if s == "+":
#                     a = x + y
#                     print('Q.',+q,'What is',x,s,y,'?')
#                     ans = int(input('ans > '))
#                     if ans == a:
#                         print('keep it up!!')
#                         print('Answer is', a)
#                         score += 1
#                     else:
#                         print("Answer is",a)
#                 else:
#                     a = x - y
#                     print('Q.',+q,'What is',x,s,y,'?')
#                     ans = int(input('ans > '))
#                     if ans == a:
#                         print('correct!')
#                         print('Answer is', a)
#                         score += 1
#                     else:
#                         print("Answer is",a)
# 
# 
# 
# =============================================================================































