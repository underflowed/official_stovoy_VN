init python:
    def sansvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.music.play("sansvoice.ogg", channel="sound", loop=True, tight=True, if_changed=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

define sv = Character("Sansvoy", color="#1E90FF", image="s", callback=sansvoice)
label taco_truck:
    scene bg tacotruck with fade
    show s worried at truecenter

    s "..."
    s "Well, what the fuck do I do now?"

    show s worried at left
    show m kukuru at right

    s "What the fuck are you doing here."
    m "ill be fucking honest with you i just want some tacos"
    m kukugun "also get the fuck back to streaming"
    s angry "Dude, fuck that shit. If I have to make snake..."
    s "One...{w} More...{w} Time..."
    s "I will commit seppuku."
    m "..."

    "IMPLEMENT SNAKE HERE IN THE FUTURE CANT FIND ANY RENPY CODE SO I MIGHT HAVE TO PROGRAM IT"
    "wait you werent supposed to see that"
    "uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh just pretend there's Snake here."


    s "Holy fucking shit."
    s "Why the hell did you even make this shitty fucking game."
    s "One of your programmers can't even implement Snake."
    s "I made it in fucking {w}{b}L O L C O D E{/b}"
    m "look bud not my fault the dudes dumb."
    s "..."
    m "..."

    menu:
        m "You wanna just get stoned?"

        "yeah fuck it":
            jump getstonedending
        "no dude i am a man of christ":
            s "Fuck that shit, I'm going home."
            m "fucker"
            jump endoftacosaga


label getstonedending:
        scene bg getstoned
        show s stoned at left
        show m stoned at right
        #I'll get on photoshop and edit up some pictures later tonight, im currently on a train to another city :^)
        s "Duuuuude... {w=1}what if I programmed snake with like... {w=1}Brainfuck... {w=1}right now..."
        m "You're a little too obssessed with making Snake dude this is getting out of hand"
        m "However NOW I can go for some fucking tacos."
        s "Sick bro... {w=1}I bought a stupid amount of taco making shit with my sweet lawsuit money."
        m "sick"
        show m eattaco at right
        m "{i}chomp{/i}"
        s "nice"
        show s eattaco at left
        s "{i}chomp{/i}"
        show black with fade
        "{b}Congratulations, you got the Stoned Devolper Ending!{/b}" #Jesus Christ this ending sucks
        return

label endoftacosaga:
    scene bg stovoysroom with fade
    show s tryhard at truecenter

    "The countless amounts of unimaginable perils that Stovoy has faced in this entire taco ordeal have left him tired, hungry, and alone."
    "So, he went home.  For shelter, comfort, and acceptence. Also he had to build a computer, and thus let us watch him build his PC, live on Twitch."

    s "Guys, I just got these new PC parts, and they're the fucking shit."
    t "dude why does the front io on your old motherboard look more modern than the new one"
    s "..."
    show ramfan at truecenter
    s "I got a RAM fan tho..."
    t "shit you right"
    hide ramfan
    s "I'm kinda stressed now however... Let's play some {nw}"
    play music "lofi.mp3"
    s "I'm kinda stressed now however... Let's play some {fast}{i}l o  -  f i{/i}"
    "Stovoy now spends a solid hour of his time replacing a motherboard.{p}Seriously though, 10 fucking minutes on a CPU power cable, like, my dude..."
    "{i}Stovoy pulls out a cable from the 90's{/i}"
    t "what the actual fuck"
    s "What?"
    t "your computer is WW2 era dude"
    s "This thing is a fucking beast, shut up."
    "{i}He then drops a whole ass CPU cooler on his new shit{/i}"
    stop music
    show s tryhard at truecenter
    with hpunch
    s "{b}FUCK{/b}"
    s "... OK I think its coo-"
    scene black with fade
    "His new motherboard began to release an engulfing darkness from the CPU socket."
    "The entire room was consumed."
    "Stovoy began to feel... something."
    "Maavrik and Hatkii bust through the door of his room."
    m "dude what the fuck I can't see anything"
    h "god why'd you have to drag me into this..."
    m "shut up hatkii"
    "Maavrik's eyes began to adjust to the darkness..."
    m "dude... I think I see something."
    m "..."
    m "......"
    m "what {w}the {w}fuck"
    "In the darkness, Maavrik made out a figure, of which no human should ever come across..."
    jump trueending

label trueending:
    play music "megalovania.mp3" #this don't loop properly lol
    show s sansvoy at truecenter:
        zoom 2.0 #adding this zoom effect because the image is too small
    with Fade(0.0, 0.0, 15.0)
    sv "{cps=20}Hey Maav... You're gonna have a bad time.{/cps}"
    show m kukuru at right
    m "JESUS CHRIST"
    m "JESUS CHRIST {fast}{nw}IT'S JASON BOURNE"
    m "dude what the fuck happened"
    sv "{cps=20}I have ascended beyond this plane of existence.{/cps}"
    sv "{cps=20}{b}NOTHING CAN STOP ME ANYMORE{/b}{/cps}"
    sv "{cps=20}Everyone will play Snake until they {w}{size=140}{b}{i}DIE{/i}{/b}{/size}{/cps}"
    m "I have to think of something before he makes everybody play that boring ass game..."
    m "or even worse, actually make people play Undertale in 2018..."
    m "well actually come to think of it its not that hard"
    $k = DblKlondike(1)
    call pre_start_game # :^)

    scene black with fade
    play music "<from 112.452 loop 0>megalovania.mp3"
    show s sansvoy at left:
        zoom 2
    show m kukuru at right
    sv "{cps=20}holy shit i beat that fucking solitaire meme{/cps}"
    sv "{cps=20}Now, for real this time, {p}{b}NOTHING CAN STOP ME ANYMORE{/b}{/cps}"
    sv "{cps=20}All you motherfuckers are gonna play some fucking {w}{size=140}{b}{i}SNAKE{/i}{/b}{/size}{/cps}"
    m kukugun "bye bye"
    scene black with None
    stop music
    play sound "gunshot.ogg"
    with Fade(0, 0, 5) #effectively pauses the game without me having to looking up how to pause the game in a more elegant manner

    scene bg room
    show s normal at left
    show m kukuru at right
    s "Uuuughh...{w=1} My everything hurts."
    s "Dude, what the hell happened?"
    m "..."
    m "well first summer proposed to make this stupid fucking game and then he made a github and i kinda got dragged into this then a bunch of shit happened and yeah you turned into sans from undertale"
    s "... wow"
    m "yeah."
    s "Uhh, well, I guess I'll go back to streaming."
    m "Well actually, there's a strong possibility that the person currently playing this is the real you"
    m "we are just a simulation, stovoy"
    s "What the fuck are you talking about."
    m "we are not the real representations of ourselves, rather we are purely data that is supposed to represent us in a fictional sense"
    s "Stop spouting nonsense."
    m "i assure you none of this is nonsense, and there is also a high chance that the real you is streaming this right now"
    s "Okay you know what just end this fucking game"

    show black with fade
    play sound "victory.mp3"
    "{b}Congratulations, you got the True Ending!{/b}"
    return
