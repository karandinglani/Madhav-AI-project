import random
computer = random.choice([1,-1,0]) # import from chatgpt
your_input = input("enter your choise: ")
yourdict = {"s":1,"w":-1,"g":0}
reversedict = {1:"snake",-1:"water",0:"gun"}

you = yourdict[your_input] # it will convert your input to numbers
# now we have 2 numbers: computer and your's

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}") #printing your's and computer's input

# we can use another method by observation
if((computer-you) == -1 or (computer-you) == 2):
    print("you loss!")
else:
    print("you win!")    