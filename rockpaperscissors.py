import random
options = ['rock', 'paper', 'scissors']

choices = options[:]
while True:
#which option beats which
    def thinker (plr, comp):
        #print("player", plr, options.index(plr))
        #print("computer", comp, options.index(comp))
        result = options.index(plr) - options.index(comp)
        result = result % 3
        #print(choices)
        if result == 1:
            choices.remove(comp)
        elif result == 2:
            choices.append(comp)
        return result # 1 = player takes the dub, 2 = player takes the L, 0 = tie
    print("let's play rock/paper/scissors")
    print("rock smashes scissors, paper covers rock, scissors cut paper")

    #randomly choose one
    compchoice =  #random.choice(choices)

    #get input
    plrchoice = ""
    while plrchoice not in options:
        plrchoice = input("pick one(rock, paper, or scissors): ")
        plrchoice = plrchoice.lower()

    print("Computer", compchoice, "player", plrchoice)
    thinker(plrchoice, compchoice)
    print("")

