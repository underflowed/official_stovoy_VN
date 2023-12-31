# Declare characters
define s = Character("Stovoy", color="#1E90FF", image="s")
define e = Character("Evades.io") #is this character necessary (as of dec 31 2023, yes)
define t = Character("Twitch Chat", color="#47d1d1")
define sumer = Character("Summerrocks", color="#EAB8AC", image="sumer")
define m = Character("Maavrik", color="#FF69B4", image="m")
define h = Character("Hatkii", color="#E961A5", image="h")
define p = Character("Polsaar", color="#4A8259", image="p")
# Declare flipped character images
image m kukuru flip = (im.Flip("m kukuru.png", horizontal=True))
image m kukukinu flip = (im.Flip("m kukukinu.png", horizontal=True))
# Declare variables
default tried_dev = None
# Redefine left/right pos for our assets, use truecenter for center
define left = Position(xpos=0.15, xanchor=0.0, ypos=0.5, yanchor=0.5)
define right = Position(xpos=0.95, xanchor=1.0, ypos=0.5, yanchor=0.5)
# Declare misc.
define black = "#000"

label start:
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .70

    scene bg room
    show s worried at truecenter
    with fade

    # Narrator introducing Stovoy after work
    "After coming home from his overly well paying Silicon Valley tech start-up job, Stovoy began streaming."
    "All 10 of his loyal followers logged onto Twitch, to watch him attempt to develop his pet project, Evades.io."
    "Day in and day out (Except for Mondays and Wednesdays), he would force himself into having to come back to these stupid idiots, thus halting any notion of the word \"productivity\"."
    "Stovoy himself and his 10 followers know that whenever he streams, any sense of productivity is futile."
    "We do as much programming as we do Brazilian Lap Dancing.{p}Which, to clarify, is none."
    "Let us join Stovoy now, as he begins his stream on Twitch."

    scene bg twitch with fade

    #Stovoy speaking to twitch chat
    s "H-hey guys! Can you hear me? I'm refactoring Evades.io to get the engine ready to accept new ma-"
    "Summerrocks joins the Twitch chat."

    show sumer gay at truecenter
    sumer "hello my sweet dev boi"
    sumer "i require knowledge of programming, feed me almighty developer"
    s   "Well, what do you wanna know..."
    sumer "everything"
    s   "{i}What's with this kid...?{/i}"
    show sumer at right with move

    show m kukuru at truecenter
    m   "{image=POGGERS.png} is that a fucking Hyper 212 Evo why the fuck is that cooler the most popular shit still this is ridiculous"
    m   "i have fucking x-ray vision and i can see into your case, nobody retroactively grab any screenshots of when we actually saw him open his pc on stream also fuck this vn"

    s   "{i}Well, not like my regulars are anymore sane than this new guy...{/i}"
    menu:
        s "{i}What should I do?{/i}"

        "Actually develop Evades.io":
            $tried_dev = True
            $ mp.vn1trieddev = True
            $ mp.save()
            s "{i}Well, it never works out, even when I tell myself to do that...{/i}"

        "I should talk to these idiots, my sub counts are low":
            $tried_dev = False
            $ mp.vn1trieddev = False
            $ mp.save()
            s "{i}Ugh... fine...{/i}"

label after_menu:
    s   "Alright, well, just... {w}Sit and watch me code... {w}I guess..."
    "Stovoy valiantly attempts to make progress on Evades.io, but as always, it was never meant to be..."

    m   "hey check out this worthless youtube video"
    python: #this should be replaced with something better, probably download the videos and store locally
        from webbrowser import open
        url = "https://www.youtube.com/watch?v=" #get beginning of YouTube URL
        vids = ["-5lzIZ0b2F8", "3Mb9iXrw8vs", "faU-lqGWgiM", "FwHmgFgm_fc"] #array of video IDs
        open(url + renpy.random.choice(vids), new=1, autoraise=True) #append random choice from vids array onto URL and open in new window (hopefully) and bring window to focus
    m   "that was a worthwhile use of your time, wasn't it? :^)"

    s   "Wow Maavrik, thanks! That video was pretty funny!"
    s   "{i}Why the actual fuck am I putting up with this.{/i}"
    "Countless hours go on, with little work on Evades.io and plenty of worthless YouTube videos, and a plethora of other distractions."
    "Finally, Stovoy was feeling his fatigue that night, and began to wind down." #should we add more useless banter before the story branches?
    s   "{i}Even after Evades.io development is finished, I can only make a copy of Snake using so many frameworks, what am I even gonna do...{/i}"

    menu:
        s "{i}I've got to figure something out...{/i}"

        "Abide by the punishment that has been placed upon me":
            s "Ugh... Time to make Snake in LOLCODE..."
            jump bad_end #bottom of this file

        "Fuck everything and go to sleep":
            s "Alright guys, today was a good stream, pretty long, but I'm gonna head off for today.{p}Hope to see you next stream!"
            scene black with fade
            if tried_dev is True:
                "Stovoy enjoyed a good sleep that night, knowing that despite his valiant efforts, he still attempted to develop Evades.io.{p}Inside, he knew was still a good person."
            else:
                "Stovoy was restless that night, as he couldn't shake the fact that he was slowly becoming a sellout Twitch shill.{p}Inside, he knew he was becoming a terrible person."
            scene black with fade
            jump hatstream #scriptwow.rpy

        "Drop this hobby and get into the Mexican Taco Truck Business":
            s "You know what? Fuck Snake and fuck you guys, I'm going into the Taco Trade."
            scene black with fade
            "And thus, Stovoy ended the stream, and instantly bought a Taco Truck with the infinite money he got by suing the people who made his parachute that failed when he went skydiving, with the settlement money he was awarded."
            jump taco_truck #scripttaco.rpy

        "Derail this fucking game so I can refactor Evades.io" if tried_dev is True:
            jump logomeme #scriptmaav.rpy

label bad_end:
    scene black with fade
    "{b}You suck.  You got the Bad Ending.{/b}{p}But at least you got a {a=https://github.com/Stovoy/LOLCODE-Snake}sick repo out of it!{/a}"
    call credits from _call_credits_3
    return
