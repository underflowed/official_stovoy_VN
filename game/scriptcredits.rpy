init python: #bunny wanted to be credited as "Hakii"
    credits = (
    ("Writing", "Maavrik"),
    ("Writing", "MUDA (Summerrocks)"),
    ("Programming", "Maavrik"),
    ("Programming", "MUDA (Summerrocks)"),
    ("Artwork", "Hakii"), # this was bunny not hatkii, not a typo
    ("Music", "Clubhouse Games"),
    ("Music", "Gitaroo Man OST - Nuff Respect (feat. NAHKI)"),
    ("Music", "Half-Life 2 - Triage at Dawn"),
    ("Music", "Metal Gear Solid 2 - Arsenal's Guts"),
    ("Music", "Moby - Extreme Ways"),
    ("Music", "Sonic the Hedgehog 3 - Carnival Night Zone Act 1"),
    ("Music", "World of Warcraft - Ashenvale"),
    ("Music", "World of Warcraft - Dun Morogh"),
    ("Sound Effects", "Half-Life 2 (which itself used a generic sound bank)"),
    ("Sound Effects", "Wilhelm Scream"),
    ("Everything else", "Google"),
    ("Everything else", "YouTube")
    )
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()

label credits: #https://lemmasoft.renai.us/forums/viewtopic.php?t=22481
    $ credits_speed = 40
    play music "images/extremeways.mp3"
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}Thanks for Playing!", text_align = 0.5)
    image forever = Text("{size=40}Stovoy will (probably not) return...", text_align = 0.5)
    scene black with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(5)
    hide theend with dissolve
    show cred at Move((0.5, 2.9), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom") with Pause(credits_speed)
    stop music fadeout 4
    show forever:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide forever with dissolve
    with Pause(1)
    return
