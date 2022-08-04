import random

def coin_flip():
    return random.choice(["Heads", "Tails"])

#This flips a coin x times and then returns the results
def multi_flip(num):
    Heads = 0 
    Tails = 0
    #The difference between while loops and for loops is that while loops = condition 
    # while the for loops = exact number you want it to be
    for x in range(num):
        #The x in here could be any varialble
        if coin_flip()== ("Heads"):
            Heads = Heads + 1
        else:
            Tails = Tails + 1
    print("you flipped" + str(Heads) + " Heads and" + str(Tails) + "Tails.")
    #Calculates the percentage of heads and tails
    print ("percentage of Heads: " + 100*Heads / num + "%")
    print ("percentage of Tails: " + 100*Tails / num + "%")  

    if (Heads == Tails):
        print("You flippped the same number of Heads and Tails")
    elif(Heads> Tails):
        print("You flipped more heads than Tails")
    elif (Heads > Tails):
        print ("You flipped more tails than Heads")

def predict():
    num_guesses = 0
    while True:
        prediction = input ("Do you think the coin will flip Heads or Tails?")
        result = coin_flip()
        if (prediction == result):
            print ("You were right, the coin flipped" + result)
            num_guesses = num_guesses + 1
        else:
            print ("You were wrong, the coin flipped" + result)
            break
    print(" You guessed right " + str(num_guesses) + " times")





