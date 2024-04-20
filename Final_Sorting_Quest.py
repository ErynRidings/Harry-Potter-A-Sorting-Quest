import datetime

def greeting():
    name = input("Enter your name here:- ")

    hour = int(datetime.datetime.now().hour)

    if hour>0 and hour<=12:
        print(f'Good Morning {name}, Welcome to Hogwarts and to the start of a new adventure')
    elif hour>12 and hour<=17:
        print(f"Good Afternoon {name}, Welcome to Hogwarts and to the start of a new adventure")
    else:
        print(f"Good Evening {name}, Welcome to Hogwarts and to the start of a new adventure")
#create a more magical welcoming , such as Welcome to Hogwarts, prepare to be sorted
#time of the day is not essential (possibly remove that from the code)

def main_quiz():


    Ravenclaw = 0
    Gryffindor = 0
    Hufflepuff = 0
    Slytherin = 0


    Question1 = ''' \nQ1-You are on the search for the sorcerer's stone and face many challenges. Which challenge do you accept?
    1. Playing in the life-size magical game of chess
    2. Flying around with magical keys
    3. Finding a way out of the strangling vines
    4. Having a facedown with your own professor'''
    print(Question1)

    user_answer = int(input('\nEnter the option number of the option which you choose:- '))

    if user_answer==1:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer==2:
        Gryffindor = Gryffindor + 1

    elif user_answer==3:
        Hufflepuff = Hufflepuff + 1

    elif user_answer==4:
        Slytherin = Slytherin + 1
    
    else:
        print('Please choose a valid option')
    
    Question2 = '''\n Q2- You arrive in the chamber of secrets and face off against the Basislisk. How will you defeat this magical beast? 
    1.With the sword of Gryffindor
    2.Entraping it within the chamber 
    3.With my trusty phoenix
    4.Speaking to the creature, making it my own'''
    print(Question2)
    user_answer2 = int(input('\nEnter the option number of the option which you choose:- ')) 

    if user_answer2==1:
        Gryffindor = Gryffindor + 1
    
    elif user_answer2==2:
        Ravenclaw = Ravenclaw +1 
    
    elif user_answer2==3:
        Hufflepuff = Hufflepuff +1
    
    elif user_answer2==4:
        Slytherin = Slytherin +1
    
    else:
        print("Please choose a valid option.....")
    
    Question3 = '''\nQ3- You are currently attending a magical beast class. There are four choices of beasts. What do you choose?
    1.Hypogriff
    2.Thestral
    3.Dragon
    4.Niffler

    print(Question3)
    user_answer3 = int(input("\nEnter the optin number of tje option which you choose:- "))

    if user_answer3==1:
        Gryffindor = Gryffindor +1
    
    elif user_answer3==2:
        Ravenclaw = Ravenclaw +1
    
    elif user_answer3==3:
        Slytherin = Slytherin + 1
    
    elif user_answer3==4:
        Hufflepuff = Hufflepuff + 1
    
    else:
        print("Please choose a valid option...")
    
    Question4 = '''\nQ4- You are thinking of enetering into the Triwizard tournement, what event do you believe you would win?
    1.Finding the egg while facing fierce dragons
    2.I would not compete because what's the point, I am the best
    3.The intricate never-ending maze
    4.Swimming in the lake to retrieve the one I lost'''

    print(Question4)
    user_answer4 = int(input('Enter the option number of the option which you choose:- '))

    if user_answer4==1:
        Gryffindor = Gryffindor + 1
    
    elif user_answer4==2:
        Slytherin = Slytherin + 1
    
    elif user_answer4==3:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer4==4:
        Hufflepuff = Hufflepuff + 1
    
    else:
        print("Please choose a valid option")
    
    Question5 ='''\nQ5- You are ion divintation class and peer into the crystal ball, what do you see?
    1.My friends
    2.Me as headmaster at Hogwarts
    3.A mysterious prophecy 
    4.Fortune in my vault at Gringotts'''

    print(Question5)
    user_answer5 = int(input('\nEnter the option number of the option which you choose:- '))

    if user_answer5==1:
        Hufflepuff = Hufflepuff + 1
    
    elif user_answer5==2:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer5==3:
        Gryffindor = Gryffindor + 1
    
    elif user_answer5==4:
        Slytherin = Slytherin + 1

    else:
        print("Please choose a valid option")
    
    Question6 = '''\nQ6- Its the beginning of your last year at Hogwarts, You have the option to take one class of your choosing. What do you choose?
    1.Magical Beast class
    2.Muggle Studies
    3.Defense Against the Dark Arts
    4.Potions class'''

    print(Question6)
    user_answer6 = int(input('Enter the option number of the option which you choose:- '))

    if user_answer6==1 or user_answer6==2 or user_answer6==3 or user_answer6==4:
        Hufflepuff = Hufflepuff + 1
        Ravenclaw = Ravenclaw + 1
        Gryffindor = Gryffindor + 1
        Slytherin = Slytherin + 1
    
    else:
        print('Please choose a valid option....')
    
    Question7 = '''\nQ7- At the end of you journey, you finally acquire the three deathly hallows. You can only choose to keep one, which do you decide?
    1.The Elder Wand
    2.The Invisibilty Cloak
    3.The Stone of Resurrection
    4.I would let them all go, they are too powerful for this world'''

    print(Question7)

    user_answer7 = int(input('Enter the option number of the option which you choose:- '))

    if user_answer7==1:
        Slytherin = Slytherin + 1

    elif user_answer7==2:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer7==3:
        Hufflepuff = Hufflepuff + 1
    
    elif user_answer7==4:
        Gryffindor = Gryffindor + 1
    
    else:
        print('Please choose a valid option....')
    
    Question8 = '''\nQ8- After graduating from Hogwarts, you look for a job. What job do you choose?
    1.Ministry Official
    2.Herbologist
    3.Teacher
    4.Professional quidditch player'''

    print(Question8)
    user_answer8 = int(input('Enter the option number of the option which you choose:- '))

    if user_answer8==1:
        Slytherin = Slytherin + 1
    
    elif user_answer8==2:
        Hufflepuff = Hufflepuff + 1
    
    elif user_answer8==3:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer8==4:
        Gryffindor = Gryffindor + 1

    else:
        print('Please choose a valid option....')
    
    Question9 = '''\nQ9- You're on vacation in the Forbidden Forrest and come along a beast. What beast appears before you?
    1.Acromantula
    2.Unicorn
    3.Demiguise
    4.Centaur'''

    print(Question9)
    user_answer9 = int(input('Enter the option number of the option which you choose:- '))

        if user_answer9==1:
        Slytherin = Slytherin + 1
    
    elif user_answer9==2:
        Hufflepuff = Hufflepuff + 1
    
    elif user_answer9==3:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer9==4:
        Gryffindor = Gryffindor + 1
    
    else:
        print('Please choose a valid option....')
    
    Question10 = '''And finally: We know that the Sorting Hat takes into account your preferences. So which Hogwarts house do you feel you identify with most closely?
    1.Gryffindor
    2.Hufflepuff
    3.Ravenclaw
    4.Slytherin'''

    print(Question10)
    user_answer10 = int(input("Enter the option number of the option which you choose:- "))

    if user_answer10==1:
        Gryffindor = Gryffindor + 1
    
    elif user_answer10==2:
        Hufflepuff = Hufflepuff + 1
    
    elif user_answer10==3:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer10==4:
        Slytherin = Slytherin + 1
    
    else:
        print("Please choose a valid option....")

    
    print(f"Ravenclaw - {(Ravenclaw/10)*100}%")
    print(f'Gryffindor - {(Gryffindor/10)*100}%')
    print(f'Hufflepuff - {(Hufflepuff/10)*100}%')
    print(f'Slytherin - {(Slytherin/10)*100}%')
# percentages are not as definitive as one, will show percentage but their main percentage of house will be boldened and a possble rough draft of their emblem will appear with their answer. 

greeting()
main_quiz()
# overall code is effective, remake small desgin choices, redo all questions and add a few more, etc.
