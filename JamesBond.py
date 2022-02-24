'''
Write a program that gives information about James Bond films. The program gives you 4 chances to name an actor
who has played Bond and then say whether you are right or not.
They should use the text below in the messages output (up to the names of the actors and so films given).
Finally they should print how well you did giving a score out of 4.

The program should know that the following actors have played Bond in the given films:

(Sean Connery, From Russia With Love; Roger Moore, Live and Let Die; Pierce Brosnan, Die Another Day; Daniel Craig, Skyfall)
'''

score = 0
print("lets play the game.")

for i in range(1,   5):
    print("Attempt",    i,  end=" ")

    Attempti = input("enter actor name:")

    if Attempti.lower() == 'roger moore':
        print("Well done.roger Moore was Bond in Live and Let Die.")
        score = score+1
    elif Attempti.lower() == 'sean connery':
        print("Well done: sean connery was Bond in From Russia with Love.")
        score = score + 1
    elif Attempti.lower() == 'will smith':
        print("Sorry. will smith hasn’t played Bond as far as I know.")
        score = score + 1
    elif Attempti.lower() == 'daniel craig':
        print("Well done: daniel craig was Bond in Sky fall.")
        score = score + 1
    else:
        print("Not played")
print("score is ",  score)


