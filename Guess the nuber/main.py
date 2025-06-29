import random
n = random.randint(1,100) # random number
a = -1 #We do this to make sure that a is not equal to n initially, so the loop runs at least once

Guesses = 0 # Initialize guess counter,Starts from 0 because the first guess will happen inside the loop.

while(a != n):
    a = int(input("Guess the number: ")) # any number entered by user
    if(a<n):
        print("Higher Number Please!!")
        Guesses +=1 

    elif(a>n):
        print("Lower Number Please")
        Guesses +=1


print(f"YAY!! you guessed the right number {n} in {Guesses} Guesses")

