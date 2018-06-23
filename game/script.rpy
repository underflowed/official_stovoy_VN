# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define s = Character("Stovoy")
define e = Character("Evades.io")
define t = Character("Twitch Chat")
define sumer = Character("Summerrocks")
define m = Character("Maavrik", color="#FF69B4")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room #THIS IS A PLACEHOLDER IMAGE PLS FIX

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show s worried

    # Narrator introducing Stovoy after work
    "After coming home from his overly well paying Silicon Valley tech start-up job, Stovoy began streaming."
    "All 10 of his loyal viewers logged onto Twitch, to watch him attempt to develop his pet project, Evades.io."
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
    m   "i have fucking x-ray vision and i can see into your case, nobody actually grab screenshots of when we actually saw him open his pc on stream also fuck this vn"
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
    m   "hey check out this worthless youtube video" #add a video here lmao idiot



    # This ends the game.

    return
