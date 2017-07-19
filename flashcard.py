import random

dictionarie = {}
with open ('state_capitals', 'r') as file:
    for line in file:
        splitLine = line.split(',')
        dictionarie[(splitLine[0])] = "".join(splitLine[1])
file.close()

game = True
score = 0
while True:
    randomState = random.choice(dictionarie.keys())
    capital = dictionarie.get(randomState).strip().lower()
    
    answare = raw_input("What is the capital of '" + randomState + "'? ").lower()
    if capital == answare:
        score +=1
        print ("That is correct! Your score is: {0}".format(score))
    else:
        score -=1
        print ("Please try again. Your score is: {0}".format(score))

    quit = raw_input("\nWhould you like to exit? 'y/n' ")
    if quit.strip() == "y":
        break
