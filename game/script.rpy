# The script of the game goes in this file.

# Declare characters
define s = Character("Stovoy")
define e = Character("Evades.io")
define t = Character("Twitch Chat")
define sumer = Character("Summerrocks", color="#EAB8AC")
define m = Character("Maavrik", color="#FF69B4")
# Declare variables
define tried_dev = None
# Declare misc.
define black = "#000"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with fade #THIS IS A PLACEHOLDER IMAGE PLS FIX

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show s worried at truecenter #for proper cropping later

    # Narrator introducing Stovoy after work
    "After coming home from his overly well paying Silicon Valley tech start-up job, Stovoy began streaming."
    "All 10 of his loyal followers logged onto Twitch, to watch him attempt to develop his pet project, Evades.io."
    "Day in and day out (Except for Mondays and Wednesdays), he would force himself into having to come back to these stupid idiots, thut halting any notion of the word \"productivity\"."
    "However, his 10 regulars and Stovoy himself, know that this is futile."
    "We do as much coding as we do Brazilian Lap Dancing."
    "Which, to clarify, is none."

    scene bg twitch

    #Stovoy speaking to twitch chat
    s "H-hey guys! Can you hear me? I'm refactoring Evades.io to get the engine ready to accept new ma-"
    "Summerrocks joins the twitch chat."
    sumer "hello my sweet dev boi"
    sumer "i require knowledge of programming, feed me almighty developer"
    s   "Well, what do you wanna know..."
    sumer "everything"
    s   "What's with this kid...?"
    m   "POGGERS is that a fucking Hyper 212 Evo why the fuck is that cooler the most popular shit still this is ridiculous"
    m   "i have fucking x-ray vision and i can see into your case, nobody actually grabbed screenshots of when we actually saw him open his pc on stream also fuck this vn"
    s   "Well, not like my regulars are anymore sane than this new guy..."
    menu:
        "What should I do?"

        "actually develop evades.io":
            $tried_dev = True
            "Well, it never works out, even when I tell myself to do that..."

        "I should talk to these idiots, my sub counts are low":
            "Ugh... fine..."

label after_menu:
    s   "Alright, well, just... Sit and watch me code... I guess..."
    "Stovoy valiantly attempts to make progress on Evades.io, but as always, it was never meant to be..."
    m   "hey check out this worthless youtube video"
    python: #this should be replaced with something better, probably download the videos and store locally
        from webbrowser import open
        from random import choice as rand #choice is already a renpy function
        url = "https://www.youtube.com/watch?v=" #get beginning of YouTube URL
        vids = ["Vlnh0KLVJJ0", "0J4SCX-Beq4", "i9bkKw32dGw", "faU-lqGWgiM", "FwHmgFgm_fc"] #array of video IDs
        open(url + rand(vids), new=1, autoraise=True) #append random choice from vids array onto URL and open in new window (hopefully) and bring window to focus
    m   "that was a worthwhile use of your time wasn't it? :^)"
    s   "Why the actual fuck am I putting up with this."
    s   "Even after Evades.io development is finished, I can only make a copy of Snake using so many frameworks, what am I even gonna do..."

    menu taco_choice:
        s "I've got to figure something out..."

        "Drop this hobby and get into the Mexican Taco Truck Business":
            s "You know what? Fuck Snake and fuck you guys, I'm going into the Taco Trade"
            jump taco_truck

        "Abide by the punishment that has been placed upon me":
            s "Ugh... Time to make Snake in HTML5 Canvas..."
            jump bad_end

        "Derail this fucking game so I can program more maps for Evades.io" if tried_dev:
            jump rpymeme

label taco_truck:
    scene bg tacotruck
    s  "taco truck infinite loop by summer what a great dev he is" #:^)
    jump taco_truck

label bad_end:
    scene black with fade
    "You suck.  You got the Bad Ending." #make bad ending better? idk :^)
    return






    # This ends the game.

    return
