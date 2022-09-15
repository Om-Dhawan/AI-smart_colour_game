import random

print("Winning rules of the Colour game as follows: "+ "\nEnter a number from 1 to 5 and match computer choice to score a point")
com_s=0
ply_s=0

while True:
    print("red = 1 \nyellow = 2 \norange = 3 \ngreen = 4 \nblue = 5 \ntake a turn: ")

    p_choice=int(input("User turn: "))

    while p_choice>5 and p_choice<1:
        p_choice=int(input("Enter valid input: "))

    if p_choice==1:
        col='red'
    elif p_choice==2:
        col='yellow'
    elif p_choice==3:
        col='orange'
    elif p_choice==4:
        col='green'
    elif p_choice==5:
        col='blue'

    print("User choose colour = " + col)
    print("Now computer's turn")

    c_choice=random.randint(1,5)

    if c_choice==1:
        c_col='red'
    elif c_choice==2:
        c_col='yellow'
    elif c_choice==3:
        c_col='orange'
    elif c_choice==4:
        c_col='green'
    elif c_choice==5:
        c_col='blue'

    print("Computer choose colour = " + c_col)

    if(col==c_col):
        ply_s+=1
        print("Player Score: "+str(ply_s))
        print("Computer Score: "+str(com_s))
    else:
        com_s+=1
        print("Player Score: "+str(ply_s))
        print("Computer Score: "+str(com_s))

    print("Do you want to play again? (Y/N)")
    answer=input()

    if answer == 'n' or answer == 'N':
        break

if(com_s>ply_s):
    print("Better luck next time, Computer wins the game!")
elif(com_s<ply_s):
    print("Congo you win the game !!!")
else:
    print("Opps its a tie ;)")
print("Thanks for playing :)")
          
