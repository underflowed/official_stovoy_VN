#based on https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=50068&p=486361&hilit=minigames#p486361
init python:
    from datetime import datetime
    currentyear = datetime.now().year
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
default result = None
default selection = None
default pscore = 0
default cscore = 0
default ties = 0

label rps_select:
    show screen stats
    $result = renpy.random.choice([rock, paper, scissors])

    menu:
        h "Make your selection, fool!"

        "Rock":
            $selection = rock
        "Paper":
            $selection = paper
        "Scissors":
            $selection = scissors

label rps_results:
    #rock
    if result is rock:
        if selection is rock:
            jump rps_tie
        elif selection is paper:
            jump rps_win
        elif selection is scissors:
            jump rps_lose

    #paper
    elif result is paper:
        if selection is rock:
            jump rps_lose
        elif selection is paper:
            jump rps_tie
        elif selection is scissors:
            jump rps_win

    #scissors
    elif result is scissors:
        if selection is rock:
            jump rps_win
        elif selection is paper:
            jump rps_lose
        elif selection is scissors:
            jump rps_tie

label rps_tie:
    h "I picked {b}[result]{/b}, and you picked {b}[selection]{/b}, so we tied.  Your inevitable death has been delayed."
    $ties += 1
    jump rps_select

label rps_win:
    h "I picked {b}[result]{/b}, and you picked {b}[selection]{/b}, so you won.  Wait, WHAT"
    $pscore +=1
    if pscore >= 3:
        jump rps_winner
    jump rps_select

label rps_lose:
    h "I picked {b}[result]{/b}, and you picked {b}[selection]{/b}, so you lose.  You will die soon."
    $cscore += 1
    if cscore >= 3:
        jump rps_gameover
    jump rps_select

screen stats():
    modal False
    zorder 100
    vbox:
        xalign 0.5
        ypos 0.01
        text"{color=#fff}Hatkii: [cscore] | You: [pscore] | Ties: [ties]{/color}"
