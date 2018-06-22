# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define s = Character("Stovoy")
define e = Character("evades.IO")
define t = Character("Twitch Chat")
define n = Character("Narrator")
define sumer = Character("Summerrocks")
define m = Character("Maavrik")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene placeholder

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show worried

    # Narrator introducing Stovoy after work
    n "After coming home from his overly well paying silicone valley tech start up job, Stovoy, began streaming."
    n "All 10 of his loyal viewers logged on to watch him attempt to develop evades.io."
    n "However, all 10 of his loyal followers, also know this is futile."
    n "We do as much coding as we do brazilian lap dancing."
    n "Which to clarify is none."

    scene twitch

    #Stovoy speaking to twitch chat
    s "h-hey guys! can you hear me? I'm refactoring evades.io to get the engine ready to accept new ma-"
    n "Summerrocks joins the twitch chat."
    sumer "hello my sweet dev boi"
    sumer "i require knowledge of programming, feed me almighty developer"
    s   "well what do you want to know..."
    sumer "everything"
    s   "Whats up with this kid...?"
    m   "POGGERS is that a fucking Hyper 212 Evo"
    s   "Well not like my regular viewers are anymore mentally sane"
    menu:
        "Should I actually develop evades.io":
            jump choice1_dev

        "I should talk to the dude my sub counts are low":
            jump choice2_onlychoice

    label choice1_dev:
        $menu_flag = False
        s "well, it never works out even when i tell myself that"

    label choice2_onlychoice:
        $menu_flag = True
        s "ugh... fine"
        jump choice1_done

    label choice1_done:
        s "alright well just... sit by and watch me code i guess..."
































    # This ends the game.

    return
