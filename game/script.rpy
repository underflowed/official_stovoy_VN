# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define s = Character("Stovoy")
define e = Character("evades.IO")
define t = Character("Twitch Chat")
define n = Character("Narrator")
define sum = Character("Summerrocks")


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
    n "Summerrocks joins the stream"
    sum "hello my sweet dev boi"

























    # This ends the game.

    return
