import random
print("Winning rule for RPS: \n"
      +"Rock Vs Paper --> Paper Wins \n"
      +"Rock Vs Scissor _---> Rock Wins \n"
      +"Scissor VS Paper ---> Scissior Wins \n")
while True:
    print("Enter Choice \n 1. Paper \n 2. Rock \n 3. Scissor \n")
    choice = int(input("User turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("Please Enter Valid input: "))
    if choice == 1:
        choice_name = 'Paper'
    elif choice == 2:
        choice_name = 'Rock'
    else:
        choice_name = 'Scissor'
    print("User choice is " + choice_name)
    print("\n Now its computer turn........")


    computer = random.randrange(1,4)

    while computer == choice:
        computer = random.randrange(1,4)
    if computer == 1:
        computer_name = "Paper"
    elif computer == 2:
        computer_name = "Rock"
    else:
        computer_name = "Scissor"
    print("Computer Choice is : " + computer_name)
    if (choice == 1 and computer == 2) or (choice == 2 and computer == 1):
        print("Paper Wins" , end = "")
        result = "Paper"
    elif (choice == 1 and computer == 3) or (choice == 3 and computer == 1):
        print("Scissor Wins ", end = "")
        result = "Scissor"
    else:
        print("Rock Wins ", end = "")
        result = "Rock"
    if result == choice_name:
        print("<=====USER WINS====>")
    else :
        print("\nComputer Wins")
    print("Do You want to play again (Y/N)")
    ans = input()
    if ans == 'n' or ans == "N":
        break

print("Thanks For Playing")