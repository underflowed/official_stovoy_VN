init python:
    mp = MultiPersistent("supersecretstovoykey")
    def sansvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.music.play("images/sansvoice.ogg", channel="sound", loop=True, tight=True, if_changed=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

define sv = Character("Sansvoy", color="#1E90FF", image="s", callback=sansvoice)
label taco_truck:
    scene bg tacotruck
    show s worried at truecenter
    with fade

    s "..."
    s "Well, what the fuck do I do now?"

    show s worried at left with move
    show m kukuru at right with dissolve

    s "What the fuck are you doing here."
    m "ill be honest with you, i just want some fucking tacos"
    m kukugun "also get the fuck back to streaming"
    show s angry:
        zoom 2.0
    s "Dude, fuck that shit. {p}If I have to make snake..."
    s "One...{w} More...{w} Time..."
    s "I will commit seppuku."
    m "..."

    "IMPLEMENT SNAKE HERE IN THE FUTURE CANT FIND ANY RENPY CODE SO I MIGHT HAVE TO PROGRAM IT"
    "wait you werent supposed to see that"
    "uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh just pretend there's Snake here."

    s "Holy fucking shit."
    s "Why the hell did you even make this shitty fucking game."
    s "One of your programmers can't even implement Snake."
    s "I made it in fucking {w}{b}{i}L O L C O D E{/i}{/b}"
    m "look bud not my fault the dudes dumb."
    s "..."
    m "..."

    menu:
        m "You wanna just get stoned?"

        "yeah fuck it":
            scene black with fade
            jump getstonedending
        "no dude i am a man of christ":
            s "Fuck that shit, I'm going home."
            m "fucker"
            scene black with fade
            jump endoftacosaga


label getstonedending:
        scene bg getstoned
        show s stoned at left:
            zoom 2.0
        show m stoned at right
        with fade
        play music "images/nuffrespect.mp3"
        #I'll get on photoshop and edit up some pictures later tonight, im currently on a train to another city :^)
        s "Duuuuude... {w=1}what if I programmed snake with like... {w=1}Brainfuck... {w=1}right now..."
        m "You're a little too obssessed with making Snake dude this is getting out of hand"
        m "However NOW I can go for some fucking tacos."
        s "Sick bro... {w=1}I bought a stupid amount of taco making shit with my sweet lawsuit money."
        m "sick"
        show m eattaco at right:
            zoom 2.0
        m "{i}chomp{/i}"
        s "nice"
        show s eattaco at left:
            zoom 2.0
        s "{i}chomp{/i}"
        scene black with fade
        stop music fadeout 5
        "{b}Congratulations, you got the Stoned Devolper Ending!{/b}" #Jesus Christ this ending sucks
        call credits from _call_credits_4
        return

label endoftacosaga:
    scene bg room
    show s tryhard at truecenter:
        zoom 2.0
    with fade

    "The countless amounts of unimaginable perils that Stovoy has faced in this entire taco ordeal have left him tired, hungry, and alone."
    "So, he went home.  For shelter, comfort, and acceptence.{p}Also he had to build a computer, and let us watch him build it live on Twitch."

    s "Guys, I just got these new PC parts, and they're the fucking shit."
    t "dude why does the front io on your old motherboard look more modern than the new one"
    s "..."
    show ramfan at truecenter
    s "I got a RAM fan tho..."
    t "shit you right"
    hide ramfan
    s "I'm kinda stressed now however... Let's play some {nw}"
    play music "images/lofi.mp3"
    s "I'm kinda stressed now however... Let's play some {fast}{i}l o  -  f i{/i}"
    "Stovoy now spends a solid two hours of his time replacing a motherboard.{p}Seriously though, 10 fucking minutes on a CPU power cable, like, my dude..."
    "{i}Stovoy pulls out a cable from the 90's{/i}"
    t "what the actual fuck"
    s "What?"
    t "your computer is WW2 era dude"
    s "This thing is a fucking beast, shut up."
    "{i}He then drops a whole ass CPU cooler on his new shit{/i}"
    stop music
    show s tryhard at truecenter with hpunch
    s "{b}FUCK{/b}"
    s "... Okay, {w}I think everything's coo-  {nw}"
    scene black with None
    play sound "images/thunder.ogg"
    play music "images/rainloop.mp3" fadein 8
    with Pause(4)
    "His new motherboard began to release an engulfing darkness from the CPU socket."
    "The entire room was consumed."
    "Stovoy began to feel... something."
    "Maavrik and Hatkii burst through Stovoy's room door."
    m "dude what the fuck I can't see anything"
    h "what the fuck, why is it raining inside..."
    h "god, {w=0.5}why'd you have to drag me into this..."
    m "shut up hatkii"
    "Maavrik's eyes began to adjust to the darkness..."
    m "dude... I think I see something."
    m "..."
    m "......"
    stop music fadeout 8
    m "what {w}the {w}fuck"
    "In the darkness, Maavrik made out a figure, of which no human should ever come across..."
    jump trueending

label trueending:
    play music "images/megalovania.mp3" #this don't loop properly lol
    show s sansvoy at truecenter:
        zoom 2.0 #adding this zoom effect because the image is too small
    with Fade(0.0, 0.0, 15.0)
    sv "{cps=20}Hey Maav... {w}You're gonna have a bad time.{/cps}"
    show m kukuru at right
    m "JESUS CHRIST"
    m "JESUS CHRIST {fast}{nw}IT'S JASON BOURNE"
    m "dude what the fuck happened"
    sv "{cps=20}I have ascended beyond this plane of existence.{/cps}"
    sv "{cps=20}{b}NOTHING CAN STOP ME ANYMORE{/b}{/cps}"
    sv "{cps=20}Everyone will play Snake until they {p}{size=140}{b}{i}DIE{/i}{/b}{/size}{/cps}"
    show h normal at left
    h "what the fuck, why is stovoy sans?"
    h "and why does he get the speech effect and i dont"
    sv "shut up hatkii"
    show h sad
    m "Hmm, I have to think of something before he makes everybody play that boring ass game..."
    m "or even worse, actually make people play Undertale in [currentyear]..."
    m "Well actually, come to think of it, I have the perfect way..."
    menu optional_name:
        m "But you might not be gamer enough to handle it.  Think you can handle Double Klondike Solitaire?"
        "no im bad at solitaire :(":
            $skippedSolitaire = True
            m "aww that's okay we won't belittle you for that at all :)"
            jump devjump # 5 years later putting this to good use
        "ya im a solitaire GOD":
            $skippedSolitaire = False
            pass
    call pre_start_game from _call_pre_start_game # :^), also i might make the start of the game more abrupt for humour

label devjump: #making this so i dont have to play fucking solitaire
    scene black with fade
    play music "<from 112.452 loop 0>images/megalovania.mp3"
    show s sansvoy at left:
        zoom 2
    show m kukuru at right
    with fade
    sv "{cps=20}holy shit i beat that fucking solitaire meme{/cps}"
    if skippedSolitaire is True:
        show m kukukinu at right
        m "actually YOU DID NOT{p}HOLY SHIT"
        m "6 YEARS LATER AND I'M PATCHING THIS DUMPSTER FIRE TO HAVE A BUILT-IN SOLITAIRE SKIP"
        m "YOU HAVE HAD 6 YEARS TO LEARN SOLITAIRE AND YOU{p}{size=140}{b}{i}DIDN'T{/i}{/b}{/size}"
        m "YOU THINK I ACTUALLY REMEMBER ANY PYTHON AT ALL? I USE POWERSHELL AT WORK I'M A WINDOWS SYSADMIN GOD DAMN IT"
        m "I TAUGHT MY DATACENTER SYSADMIN COUNTERPART PYTHON AND POWERSHELL THEN FORGOT PYTHON SINCE I NEVER USED IT"
        m "THIS TOOK ME HOURS TO IMPLEMENT I HOPE YOU'RE HAPPY"
        m "AND THEN I CAME ACROSS ALL THE BUGS WITH THE JUMP TO THE NEWER REN'PY VERSION"
        m "THANKS FOR REMINDING ME WHY I'M NOT A GAME DEV OR A REGULAR DEV"
        m "{fast}{nw}muda i hope school went well we should talk more :)"
        show sumer gay at left
        sumer "maav shut up sysadmins are dumb"
        m "YEAH JOKES ON YOU I HAVE TO SYSADMIN FOR DEVS NOW AND{p}{b}HOOOOOOOOOOOOOOOOOOOOOLY SHIT{/b} SOME OF THE SHIT THEY DO"
        sv "{cps=20}man whatever can we get back to the game you said you wouldn't belittle the player"
        m "ok fine"
        show m kukuru
        hide sumer gay
    sv "{cps=20}Now, for real this time, {p}{b}NOTHING CAN STOP ME ANYMORE{/b}{/cps}"
    sv "{cps=20}All you motherfuckers are gonna play some fucking {p}{size=140}{b}{i}SNAKE{/i}{/b}{/size}{/cps}"
    m kukugun "bye bye"
    scene black with None
    stop music
    play sound "images/gunshot.ogg"
    with Pause(5)

    scene bg room
    show s normal at truecenter:
        zoom 2.0
    show m kukuru at right
    with fade
    s "Uuuughh...{w=1} My everything hurts."
    s "Dude, what the hell happened?"
    m "..."
    m "well first summer proposed to make this stupid fucking game and then he made a github and i kinda got dragged into this then a bunch of shit happened and yeah you turned into sans from undertale"
    s "... wow"
    m "yeah."
    s "Uhh, well... {p}I guess I'll go back to streaming."
    m "Well actually, there's a strong possibility that the person currently playing this is the real you"
    play music "<to 126.124>images/arsenalsguts.ogg"
    m "we are just a simulation, stovoy"
    s "What the fuck are you talking about."
    m "we are not the real representations of ourselves, rather we are purely data that is supposed to represent us in a fictional sense"
    s "Stop spouting nonsense."
    m "i assure you none of this is nonsense, and there is also a high chance that the real you is streaming this right now"
    s "Are you kidding me?  What the fuck are you talking about?"
    show h normal at left with dissolve
    h "Rumors about petty issues, misinterpretations, slander..."
    m "All of this junk data preserved in an unfiltered state, growing at an alarming rate."
    h "It will only slow down social progress, reduce the rate of evolution."
    m "The digital society furthers human flaws and selectively rewards development of convenient half-truths."
    h "Everyone grows up being told the same thing."
    m "Be nice to other people."
    h "But beat out the competition!"
    m "\"You're special.\"{p}\"Believe in yourself and you will succeed.\""
    h "But it's obvious from the start that only a few can succeed..."
    play music "<from 126.200 to 281.995>images/arsenalsguts.ogg"
    scene black with Fade(1.0, 0.0, 0.0)
    show m kukuru at truecenter
    show h normal at right
    with dissolve
    m "You exercise your right to \"freedom\" and this is the result.{p}All rhetoric to avoid conflict and protect each other from hurt."
    m "The untested truths spun by different interests continue to churn and accumulate in the sandbox of political correctness and value systems."
    h "Everyone withdraws into their own small gated community, afraid of a larger forum.{p}They stay inside their little ponds, leaking whatever \"truth\" suits them into the growing cesspool of society at large."
    m "The different cardinal truths neither clash nor mesh.{p}No one is invalidated, but nobody is right."
    h "Not even natural selection can take place here.{p}The world is being engulfed in \"truth\"."
    m "And this is the way the world ends.{p}Not with a bang, {w}but a whimper."
    scene bg room
    stop music
    show s normal at truecenter:
        zoom 2.0
    s "Okay you know what just end this fucking game"
    if skippedSolitaire is True:
        show m kukuru at truecenter
        m "NO YOU SKIPPED SOLITAIRE LOL"
        e "LOL"
        t "LOL"
        show sumer gay at truecenter
        sumer "LOL"
        show h happy at truecenter
        h "LOL"
        show p bripo at truecenter
        p "LOL"



    scene black with fade
    play music "images/victory.mp3" noloop
    $mp.vn1trueending = True
    $mp.save()
    "{b}Congratulations, you got the True Ending!{/b}"
    call credits from _call_credits_5
    return
